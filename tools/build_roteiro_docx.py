#!/usr/bin/env python3
"""
Build a single combined roteiro markdown from the index + Dia files,
then convert to docx via md_to_docx.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROTEIRO_DIR_DEFAULT = Path("Roteiro")
INDEX_FILE = "J3 - Roteiro.md"
DIA_FILES = [
    "Dia 1 - A Avenida.md",
    "Dia 2 - O Fliperama.md",
    "Dia 3 - O Beco.md",
    "Dia 4 - O Refúgio.md",
    "Dia 5 - O Cerco.md",
    "Dia 6 - A Revelação.md",
    "Dia 7 - O Final.md",
]


def normalize_headings(text: str, base_level_shift: int = 0) -> str:
    if base_level_shift <= 0:
        return text
    out = []
    for line in text.splitlines():
        m = re.match(r"^(#{1,5})(\s+)(.*)$", line)
        if m:
            new_level = min(6, len(m.group(1)) + base_level_shift)
            line = ("#" * new_level) + m.group(2) + m.group(3)
        out.append(line)
    return "\n".join(out)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--roteiro-dir", type=Path, default=ROTEIRO_DIR_DEFAULT)
    parser.add_argument("--out-md", type=Path,
                        default=Path("Documentação/Roteiro - J3 Completo.md"))
    parser.add_argument("--out-docx", type=Path,
                        default=Path("Documentação/Roteiro - J3 Completo.docx"))
    args = parser.parse_args()

    roteiro_dir: Path = args.roteiro_dir.resolve()
    if not roteiro_dir.exists():
        print(f"ERROR: {roteiro_dir} nao existe", file=sys.stderr)
        return 2

    index_path = roteiro_dir / INDEX_FILE
    index_text = index_path.read_text(encoding="utf-8")

    cut_pattern = re.compile(r"^##\s+Dias Dispon.?veis", re.MULTILINE)
    cut_match = cut_pattern.search(index_text)
    if cut_match:
        header = index_text[: cut_match.start()].rstrip()
    else:
        header = index_text.rstrip()

    parts = [header, ""]
    parts.append("---")
    parts.append("")
    parts.append("# Roteiro por Dia")
    parts.append("")
    parts.append("Os 7 dias do jogo na ordem em que sao jogados. Cada dia foi escrito"
                 " em markdown separado em `Roteiro/Dias/` e consolidado aqui para"
                 " entrega/revisao em um documento unico.")
    parts.append("")

    dia_dir = roteiro_dir / "Dias"
    for dia_name in DIA_FILES:
        dia_path = dia_dir / dia_name
        if not dia_path.exists():
            print(f"  WARN: {dia_path} nao encontrado", file=sys.stderr)
            continue
        dia_text = dia_path.read_text(encoding="utf-8")
        dia_text = normalize_headings(dia_text, base_level_shift=1)
        parts.append("---")
        parts.append("")
        parts.append(dia_text.rstrip())
        parts.append("")

    combined = "\n".join(parts).rstrip() + "\n"
    args.out_md.parent.mkdir(parents=True, exist_ok=True)
    args.out_md.write_text(combined, encoding="utf-8")
    print(f"Combined md saved: {args.out_md} ({len(combined.splitlines())} lines)")

    tools_dir = Path(__file__).resolve().parent
    sys.path.insert(0, str(tools_dir))
    import md_to_docx  # noqa: E402

    md_to_docx.convert(args.out_md.resolve(), args.out_docx.resolve(),
                       base_dir=args.out_md.parent.resolve())
    return 0


if __name__ == "__main__":
    sys.exit(main())
