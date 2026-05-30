#!/usr/bin/env python3
"""
Convert GDD markdown to a clean .docx with consistent formatting.

Uses python-docx + markdown + BeautifulSoup. Handles headings, paragraphs
with inline bold/italic/code, bullet/numbered lists, tables, images, code
blocks, blockquotes.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path
from urllib.parse import unquote

import markdown as md
from bs4 import BeautifulSoup, NavigableString
from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches, Pt, RGBColor

DOCX_HEADING_STYLES = {
    "h1": "Title",
    "h2": "Heading 1",
    "h3": "Heading 2",
    "h4": "Heading 3",
    "h5": "Heading 4",
}


def add_inline_runs(paragraph, element):
    for node in element.children if hasattr(element, "children") else [element]:
        if isinstance(node, NavigableString):
            text = str(node)
            if text:
                paragraph.add_run(text)
            continue
        name = node.name
        if name in ("strong", "b"):
            run = paragraph.add_run(node.get_text())
            run.bold = True
        elif name in ("em", "i"):
            run = paragraph.add_run(node.get_text())
            run.italic = True
        elif name == "code":
            run = paragraph.add_run(node.get_text())
            run.font.name = "Consolas"
            run.font.size = Pt(10)
        elif name == "a":
            run = paragraph.add_run(node.get_text())
            run.font.color.rgb = RGBColor(0x00, 0x4C, 0x99)
            run.underline = True
        elif name == "br":
            paragraph.add_run().add_break()
        else:
            add_inline_runs(paragraph, node)


def add_paragraph(doc, element, style="Normal"):
    p = doc.add_paragraph(style=style)
    add_inline_runs(p, element)
    return p


def add_code_block(doc, text):
    p = doc.add_paragraph()
    run = p.add_run(text.rstrip("\n"))
    run.font.name = "Consolas"
    run.font.size = Pt(9)
    p_pr = p._p.get_or_add_pPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:fill"), "F2F2F2")
    p_pr.append(shd)


def add_list_item(doc, element, ordered=False):
    style = "List Number" if ordered else "List Bullet"
    p = doc.add_paragraph(style=style)
    add_inline_runs(p, element)
    return p


def add_table(doc, table_el):
    rows = table_el.find_all("tr")
    if not rows:
        return
    headers = rows[0].find_all(["th", "td"])
    cols = len(headers)
    if cols == 0:
        return
    docx_table = doc.add_table(rows=len(rows), cols=cols)
    try:
        docx_table.style = "Light Grid Accent 1"
    except KeyError:
        docx_table.style = "Table Grid"
    for r_idx, tr in enumerate(rows):
        cells = tr.find_all(["th", "td"])
        for c_idx, td in enumerate(cells):
            if c_idx >= cols:
                continue
            cell = docx_table.cell(r_idx, c_idx)
            cell.text = ""
            p = cell.paragraphs[0]
            add_inline_runs(p, td)
            if r_idx == 0 or td.name == "th":
                for run in p.runs:
                    run.bold = True


def add_image(doc, img_el, base_dir):
    src = img_el.get("src", "")
    alt = img_el.get("alt", "")
    src = unquote(src)
    img_path = (base_dir / src).resolve()
    if img_path.exists() and img_path.is_file():
        try:
            doc.add_picture(str(img_path), width=Inches(5.0))
            if alt:
                caption = doc.add_paragraph(alt, style="Caption")
                caption.alignment = WD_ALIGN_PARAGRAPH.CENTER
            return
        except Exception as e:
            print(f"  WARN: nao consegui inserir imagem {img_path}: {e}", file=sys.stderr)
    p = doc.add_paragraph()
    run = p.add_run(f"[Imagem: {alt or src}]")
    run.italic = True
    run.font.color.rgb = RGBColor(0x80, 0x80, 0x80)


def add_blockquote(doc, element):
    try:
        p = doc.add_paragraph(style="Intense Quote")
    except KeyError:
        p = doc.add_paragraph()
    add_inline_runs(p, element)


def convert(md_path, docx_path, base_dir=None):
    if base_dir is None:
        base_dir = md_path.parent
    text = md_path.read_text(encoding="utf-8")
    html = md.markdown(text, extensions=["tables", "fenced_code", "sane_lists", "attr_list"])
    soup = BeautifulSoup(html, "html.parser")

    doc = Document()
    for section in doc.sections:
        section.page_width = Inches(8.27)
        section.page_height = Inches(11.69)
        section.left_margin = Inches(0.9)
        section.right_margin = Inches(0.9)
        section.top_margin = Inches(0.9)
        section.bottom_margin = Inches(0.9)
    style = doc.styles["Normal"]
    style.font.name = "Calibri"
    style.font.size = Pt(11)

    for child in soup.children:
        if isinstance(child, NavigableString):
            continue
        name = child.name
        if name in DOCX_HEADING_STYLES:
            heading_style = DOCX_HEADING_STYLES[name]
            if heading_style == "Title":
                doc.add_heading(child.get_text(), level=0)
            else:
                level = int(name[1:]) - 1
                doc.add_heading(child.get_text(), level=level)
        elif name == "p":
            imgs = child.find_all("img", recursive=False)
            if len(imgs) == 1 and child.get_text().strip() == "":
                add_image(doc, imgs[0], base_dir)
            else:
                for img in child.find_all("img"):
                    add_image(doc, img, base_dir)
                    img.decompose()
                if child.get_text().strip():
                    add_paragraph(doc, child)
        elif name == "ul":
            for li in child.find_all("li", recursive=False):
                add_list_item(doc, li, ordered=False)
        elif name == "ol":
            for li in child.find_all("li", recursive=False):
                add_list_item(doc, li, ordered=True)
        elif name == "table":
            add_table(doc, child)
        elif name == "pre":
            code = child.find("code")
            text_content = code.get_text() if code else child.get_text()
            add_code_block(doc, text_content)
        elif name == "blockquote":
            for sub in child.find_all("p"):
                add_blockquote(doc, sub)
        elif name == "hr":
            doc.add_paragraph()
        else:
            if child.get_text().strip():
                add_paragraph(doc, child)

    doc.save(str(docx_path))
    print(f"Saved: {docx_path}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("md", type=Path)
    parser.add_argument("docx", type=Path)
    parser.add_argument("--base-dir", type=Path, default=None,
                        help="Diretorio para resolver caminhos de imagem")
    args = parser.parse_args()
    convert(args.md.resolve(), args.docx.resolve(),
            args.base_dir.resolve() if args.base_dir else None)
    return 0


if __name__ == "__main__":
    sys.exit(main())
