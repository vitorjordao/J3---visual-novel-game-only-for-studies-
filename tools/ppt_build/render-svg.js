/* Consumes DECK -> approximate SVG -> PNG via sharp, for visual verification.
   Not pixel-identical to PowerPoint (fonts differ), but faithful in geometry:
   image boxes, panels, table grid, text positions & wrapping -> catches overflow/overlap. */
const fs = require("fs");
const path = require("path");
const sharp = require("sharp");
const { DECK, EMU, H, asset, aspectOf, A } = require("./deck-spec");

const SC = 100; // px per inch
const W = Math.round(EMU * SC), HT = Math.round(H * SC);
const OUTDIR = path.join(__dirname, "preview");
fs.mkdirSync(OUTDIR, { recursive: true });

const esc = (t) => String(t).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
const mime = (p) => (/\.png$/i.test(p) ? "image/png" : "image/jpeg");
const dataURI = (p) => `data:${mime(p)};base64,${fs.readFileSync(p).toString("base64")}`;

// crude width estimate per glyph (em fraction)
function textW(str, size, mono) {
  return str.length * size * (mono ? 0.55 : 0.50);
}
// flow runs -> array of lines; each line = [{text,color,size,bold,font,mono}]
function flow(op, boxW) {
  const maxW = boxW * SC - (op.bullet ? 16 : 0);
  const lines = [];
  let cur = [], curW = 0;
  const pushLine = () => { lines.push(cur); cur = []; curW = 0; };
  op.runs.forEach((r, ri) => {
    const size = (r.size || op.size);
    const mono = (r.font || op.font || "").includes("Consolas");
    const color = r.color || op.color;
    const bold = r.bold != null ? r.bold : op.bold;
    if ((op.stack || op.bullet) && ri > 0) pushLine();
    const parts = r.text.split(/(\s+)/);
    for (const tok of parts) {
      if (tok === "") continue;
      if (tok === "\n") { pushLine(); continue; }
      const tw = textW(tok, size, mono);
      if (curW + tw > maxW && curW > 0 && tok.trim() !== "") pushLine();
      cur.push({ text: tok, color, size, bold, mono });
      curW += tw;
    }
  });
  if (cur.length) pushLine();
  // strip leading spaces per line
  return lines.map((ln) => { while (ln.length && ln[0].text.trim() === "") ln.shift(); return ln; }).filter((ln) => ln.length);
}

function renderText(op) {
  const lines = flow(op, op.w);
  const maxSize = Math.max(...op.runs.map((r) => r.size || op.size));
  const lineH = maxSize * (op.lineSpacing || 1.1) * 1.15;
  const totalH = lines.length * lineH;
  const boxX = op.x * SC, boxY = op.y * SC, boxW = op.w * SC, boxH = op.h * SC;
  let startY;
  if (op.valign === "middle") startY = boxY + (boxH - totalH) / 2 + maxSize;
  else startY = boxY + maxSize; // top
  let svg = "";
  lines.forEach((ln, li) => {
    let anchor = "start", ax = boxX + (op.bullet ? 16 : 0);
    if (op.align === "center") { anchor = "middle"; ax = boxX + boxW / 2; }
    else if (op.align === "right") { anchor = "end"; ax = boxX + boxW; }
    const y = startY + li * lineH;
    if (op.bullet && anchor === "start") {
      svg += `<text x="${boxX}" y="${y}" font-size="${op.size * 0.9}" fill="#${ln[0].color}" font-family="Segoe UI, sans-serif">▪</text>`;
    }
    // merge adjacent tokens sharing style so interior spaces survive
    const merged = [];
    ln.forEach((t) => {
      const last = merged[merged.length - 1];
      if (last && last.color === t.color && last.size === t.size && last.bold === t.bold) last.text += t.text;
      else merged.push({ ...t });
    });
    let inner = "";
    merged.forEach((t) => { inner += `<tspan font-size="${t.size}" fill="#${t.color}" font-weight="${t.bold ? 700 : 400}">${esc(t.text)}</tspan>`; });
    svg += `<text x="${ax}" y="${y}" xml:space="preserve" text-anchor="${anchor}" font-family="Segoe UI, Arial, sans-serif">${inner}</text>`;
  });
  return svg;
}

function renderSlide(sp) {
  let svg = `<svg xmlns="http://www.w3.org/2000/svg" width="${W}" height="${HT}" viewBox="0 0 ${W} ${HT}">`;
  svg += `<rect x="0" y="0" width="${W}" height="${HT}" fill="#${sp.bg}"/>`;
  for (const op of sp.ops) {
    const x = op.x * SC, y = op.y * SC, w = op.w * SC, h = op.h * SC;
    if (op.t === "image") {
      const par = op.fit === "cover" ? "xMidYMid slice" : "xMidYMid meet";
      svg += `<image x="${x}" y="${y}" width="${w}" height="${h}" preserveAspectRatio="${par}" href="${dataURI(asset(op.slug))}"/>`;
    } else if (op.t === "rect") {
      const rx = (op.r || 0) * SC;
      const op_ = op.alpha != null ? (100 - op.alpha) / 100 : 1;
      const fill = op.fill ? `#${op.fill}` : "none";
      const stroke = op.line ? `stroke="#${op.line}" stroke-width="${op.lineW}"` : "";
      svg += `<rect x="${x}" y="${y}" width="${w}" height="${h}" rx="${rx}" ry="${rx}" fill="${fill}" fill-opacity="${op_}" ${stroke}/>`;
    } else if (op.t === "ellipse") {
      svg += `<ellipse cx="${x + w / 2}" cy="${y + h / 2}" rx="${w / 2}" ry="${h / 2}" fill="#${op.fill}"/>`;
    } else if (op.t === "video") {
      svg += `<rect x="${x}" y="${y}" width="${w}" height="${h}" fill="#05070d" stroke="#27E1E8" stroke-width="2"/>`;
      svg += `<circle cx="${x + w / 2}" cy="${y + h / 2}" r="34" fill="#27E1E8" fill-opacity="0.9"/>`;
      svg += `<path d="M ${x + w / 2 - 11} ${y + h / 2 - 16} L ${x + w / 2 + 19} ${y + h / 2} L ${x + w / 2 - 11} ${y + h / 2 + 16} Z" fill="#0A0E1A"/>`;
      svg += `<text x="${x + w / 2}" y="${y + h / 2 + 70}" text-anchor="middle" font-size="16" fill="#9AA8C2" font-family="Consolas,monospace">[ vídeo embutido ]</text>`;
    } else if (op.t === "text") {
      svg += renderText(op);
    } else if (op.t === "table") {
      let cy = y;
      const cols = op.colW.map((c) => c * SC);
      op.rows.forEach((row) => {
        let cx = x;
        const rh = op.rowH * SC;
        row.forEach((cell, ci) => {
          const cwp = cols[ci];
          svg += `<rect x="${cx}" y="${cy}" width="${cwp}" height="${rh}" fill="${cell.fill ? "#" + cell.fill : "none"}" stroke="#${sp.bg}" stroke-width="1.5"/>`;
          // wrap cell text
          const tlines = flow({ runs: [{ text: cell.text }], size: cell.size || op.fontSize, font: cell.font || "", align: cell.align || "left", color: cell.color, bold: cell.bold }, op.colW[ci] - 0.1);
          const fs2 = cell.size || op.fontSize;
          const lh = fs2 * 1.18;
          let ty = cy + rh / 2 - ((tlines.length - 1) * lh) / 2 + fs2 * 0.35;
          tlines.forEach((ln) => {
            const txt = ln.map((t) => t.text).join("");
            const anchor = (cell.align === "center") ? "middle" : "start";
            const tx = anchor === "middle" ? cx + cwp / 2 : cx + 6;
            svg += `<text x="${tx}" y="${ty}" text-anchor="${anchor}" font-size="${fs2}" fill="#${cell.color || "E7ECF5"}" font-weight="${cell.bold ? 700 : 400}" font-family="Segoe UI, Arial, sans-serif">${esc(txt)}</text>`;
            ty += lh;
          });
          cx += cwp;
        });
        cy += op.rowH * SC;
      });
    }
  }
  svg += `</svg>`;
  return svg;
}

(async () => {
  const pngs = [];
  for (let i = 0; i < DECK.length; i++) {
    const svg = renderSlide(DECK[i]);
    const out = path.join(OUTDIR, `slide${String(i + 1).padStart(2, "0")}.png`);
    await sharp(Buffer.from(svg)).png().toFile(out);
    pngs.push(out);
    console.log("rendered", path.basename(out));
  }
  // montage 3 cols x 4 rows, each slide scaled to 600x338 (+labels gap)
  const cw = 640, ch = 360, cols = 3, rows = Math.ceil(pngs.length / cols), pad = 12;
  const MW = cols * cw + (cols + 1) * pad, MH = rows * ch + (rows + 1) * pad;
  const tiles = [];
  for (let i = 0; i < pngs.length; i++) {
    const r = Math.floor(i / cols), c = i % cols;
    const buf = await sharp(pngs[i]).resize(cw, ch, { fit: "contain", background: "#000" }).png().toBuffer();
    tiles.push({ input: buf, left: pad + c * (cw + pad), top: pad + r * (ch + pad) });
  }
  await sharp({ create: { width: MW, height: MH, channels: 3, background: "#1a1a1a" } })
    .composite(tiles).png().toFile(path.join(OUTDIR, "_montage.png"));
  console.log("montage ->", path.join(OUTDIR, "_montage.png"));
})();
