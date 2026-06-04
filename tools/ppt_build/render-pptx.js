/* Consumes DECK (deck-spec.js) -> real .pptx via pptxgenjs. */
const pptxgen = require("pptxgenjs");
const fs = require("fs");
const path = require("path");
const { DECK, EMU, H, asset } = require("./deck-spec");

const pptx = new pptxgen();
pptx.defineLayout({ name: "W", width: EMU, height: H });
pptx.layout = "W";
pptx.author = "Vitor Jordão";
pptx.company = "J3 - A Consciência Artificial";
pptx.subject = "Pitch — banca avaliadora";
pptx.title = "J3 - A Consciência Artificial";

const clean = (o) => { const r = {}; for (const k in o) if (o[k] !== undefined) r[k] = o[k]; return r; };

for (const sp of DECK) {
  const s = pptx.addSlide();
  s.background = { color: sp.bg };
  for (const op of sp.ops) {
    if (op.t === "image") {
      s.addImage({ path: asset(op.slug), x: op.x, y: op.y, w: op.w, h: op.h, sizing: { type: op.fit === "cover" ? "cover" : "contain", w: op.w, h: op.h } });
    } else if (op.t === "rect") {
      const shape = op.r > 0 ? pptx.ShapeType.roundRect : pptx.ShapeType.rect;
      s.addShape(shape, clean({
        x: op.x, y: op.y, w: op.w, h: op.h, rectRadius: op.r > 0 ? op.r : undefined,
        fill: op.fill ? (op.alpha != null ? { color: op.fill, transparency: op.alpha } : { color: op.fill }) : undefined,
        line: op.line ? { color: op.line, width: op.lineW } : { type: "none" },
      }));
    } else if (op.t === "ellipse") {
      s.addShape(pptx.ShapeType.ellipse, { x: op.x, y: op.y, w: op.w, h: op.h, fill: { color: op.fill }, line: { type: "none" } });
    } else if (op.t === "video") {
      s.addMedia({ type: "video", path: op.path, x: op.x, y: op.y, w: op.w, h: op.h });
    } else if (op.t === "text") {
      const runs = op.runs.map((r) => ({
        text: r.text,
        options: clean({ color: r.color, bold: r.bold, italic: r.italic, fontSize: r.size, fontFace: r.font, charSpacing: r.charSpacing,
          breakLine: (op.bullet || op.stack) ? true : undefined,
          bullet: op.bullet ? { code: "25AA", indent: 14 } : undefined }),
      }));
      s.addText(runs, clean({
        x: op.x, y: op.y, w: op.w, h: op.h, align: op.align, valign: op.valign,
        fontFace: op.font, fontSize: op.size, color: op.color, bold: op.bold, italic: op.italic,
        charSpacing: op.charSpacing || undefined, lineSpacingMultiple: op.lineSpacing, paraSpaceAfter: op.paraAfter || undefined, margin: 0,
      }));
    } else if (op.t === "table") {
      const colW = op.colW;
      const rows = op.rows.map((row) => row.map((c) => ({
        text: c.text,
        options: clean({ fill: c.fill ? { color: c.fill } : undefined, color: c.color, bold: c.bold, italic: c.italic,
          fontFace: c.font, fontSize: c.size || op.fontSize, align: c.align || "left", valign: "middle", margin: [3, 4, 3, 4] }),
      })));
      s.addTable(rows, { x: op.x, y: op.y, w: op.w, colW, rowH: op.rowH, valign: "middle", border: { type: "solid", color: sp.bg, pt: 1.5 } });
    }
  }
  if (sp.notes) s.addNotes(sp.notes);
}

const OUT = path.join(__dirname, "J3 - Apresentacao Banca.pptx");
pptx.writeFile({ fileName: OUT }).then(() => {
  console.log("OK ->", OUT, `(${(fs.statSync(OUT).size / 1048576).toFixed(1)} MB)`);
}).catch((e) => { console.error("FAIL", e); process.exit(1); });
