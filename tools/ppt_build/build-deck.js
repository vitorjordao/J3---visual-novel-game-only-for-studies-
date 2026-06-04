/* J3 — A Consciência Artificial : pitch deck (~12 slides) for the banca.
   pptxgenjs, 16:9 wide. Cyberpunk theme. PT-BR. Short speaker notes. */
const pptxgen = require("pptxgenjs");
const fs = require("fs");
const path = require("path");

const A = JSON.parse(fs.readFileSync(path.join(__dirname, "assets-manifest.json"), "utf8"));
const COMP = JSON.parse(fs.readFileSync(path.join(__dirname, "competitors.json"), "utf8"));
const asset = (slug) => path.join(__dirname, A[slug].file);
const TRAILER = "g:/Vitor/J3 project/Trailer/J3_promo_v3_matrix.mp4";

// ---- theme ----
const C = {
  bg:      "0A0E1A",
  bg2:     "0E1424",
  panel:   "151C30",
  panel2:  "1B2440",
  ink:     "E7ECF5",
  muted:   "9AA8C2",
  faint:   "63708C",
  cyan:    "27E1E8",
  magenta: "FF2E97",
  green:   "47F08A",
  purple:  "A971FF",
  orange:  "FF9F45",
  red:     "FF5470",
  white:   "FFFFFF",
};
const F = { head: "Bahnschrift SemiBold", headL: "Bahnschrift", body: "Segoe UI", mono: "Consolas" };
const EMU = 13.333; // wide width in inches
const H = 7.5;

const pptx = new pptxgen();
pptx.defineLayout({ name: "W", width: EMU, height: H });
pptx.layout = "W";
pptx.author = "Vitor Jordão";
pptx.company = "J3 - A Consciência Artificial";
pptx.subject = "Pitch — banca avaliadora";
pptx.title = "J3 - A Consciência Artificial";

// ---- helpers ----
function slide(bg = C.bg) {
  const s = pptx.addSlide();
  s.background = { color: bg };
  return s;
}
// full-bleed image (cover) + dark scrim for legibility
function bgImage(s, slug, scrim = 55) {
  s.addImage({ path: asset(slug), x: 0, y: 0, w: EMU, h: H, sizing: { type: "cover", w: EMU, h: H } });
  s.addShape(pptx.ShapeType.rect, { x: 0, y: 0, w: EMU, h: H, fill: { color: C.bg, transparency: 100 - scrim }, line: { type: "none" } });
}
function panel(s, x, y, w, h, fill = C.panel, opts = {}) {
  s.addShape(pptx.ShapeType.roundRect, { x, y, w, h, rectRadius: opts.r ?? 0.08,
    fill: opts.transparency != null ? { color: fill, transparency: opts.transparency } : { color: fill },
    line: opts.line ? { color: opts.line, width: opts.lineW ?? 1 } : { type: "none" },
    shadow: opts.shadow });
}
function neonBar(s, x, y, w, color = C.cyan, h = 0.055) {
  s.addShape(pptx.ShapeType.rect, { x, y, w, h, fill: { color }, line: { type: "none" } });
}
function kicker(s, txt, x, y, color = C.cyan, w = 6) {
  s.addText(txt.toUpperCase(), { x, y, w, h: 0.3, fontFace: F.mono, fontSize: 11, color, charSpacing: 3, bold: true, align: "left" });
}
function title(s, txt, x, y, w, size = 32, color = C.white) {
  s.addText(txt, { x, y, w, h: 0.9, fontFace: F.head, fontSize: size, color, bold: true, align: "left" });
}
function chip(s, txt, x, y, w, color = C.cyan, fill = C.panel2) {
  s.addShape(pptx.ShapeType.roundRect, { x, y, w, h: 0.36, rectRadius: 0.18, fill: { color: fill }, line: { color, width: 1 } });
  s.addText(txt, { x, y, w, h: 0.36, fontFace: F.body, fontSize: 10.5, color: C.ink, align: "center", valign: "middle" });
}
function bullets(s, items, x, y, w, h, fontSize = 14, color = C.ink) {
  s.addText(items.map((t, i) => ({ text: t, options: { bullet: { code: "25AA", indent: 14 }, color: i % 2 ? C.ink : C.ink, breakLine: true } })),
    { x, y, w, h, fontFace: F.body, fontSize, color, lineSpacingMultiple: 1.12, paraSpaceAfter: 7, valign: "top" });
}
function footer(s, n) {
  s.addText([
    { text: "J3 — A CONSCIÊNCIA ARTIFICIAL", options: { color: C.faint, fontSize: 8, fontFace: F.mono, charSpacing: 2 } },
  ], { x: 0.45, y: H - 0.4, w: 8, h: 0.3, align: "left", valign: "middle" });
  s.addText(`${n} / 12`, { x: EMU - 1.4, y: H - 0.4, w: 0.95, h: 0.3, color: C.faint, fontSize: 8, fontFace: F.mono, align: "right", valign: "middle" });
  neonBar(s, 0.45, H - 0.46, 0.5, C.magenta, 0.03);
}

/* ============================ SLIDE 1 — CAPA ============================ */
(() => {
  const s = slide();
  bgImage(s, "bg_avenue", 42);
  // left scrim panel for text
  s.addShape(pptx.ShapeType.rect, { x: 0, y: 0, w: 7.6, h: H, fill: { color: C.bg, transparency: 22 }, line: { type: "none" } });
  // J3 hero on the right (transparent png)
  s.addImage({ path: asset("char_j3"), x: 8.0, y: 0.7, w: 5.0, h: 6.2, sizing: { type: "contain", w: 5.0, h: 6.2 } });
  kicker(s, "Visual Novel Cyberpunk · Ren'Py · PT-BR", 0.7, 0.9, C.cyan, 7);
  s.addText("J3", { x: 0.62, y: 1.35, w: 7, h: 1.7, fontFace: F.head, fontSize: 130, color: C.white, bold: true });
  s.addText("A CONSCIÊNCIA ARTIFICIAL", { x: 0.72, y: 3.0, w: 7, h: 0.7, fontFace: F.headL, fontSize: 30, color: C.cyan, bold: true, charSpacing: 1 });
  neonBar(s, 0.72, 3.72, 3.2, C.magenta, 0.05);
  s.addText("Um robô sem memória descobre sua identidade através de escolhas que moldam sua alma — numa Nova São Paulo cyberpunk e preconceituosa.",
    { x: 0.72, y: 3.95, w: 6.6, h: 1.2, fontFace: F.body, fontSize: 15.5, color: C.ink, lineSpacingMultiple: 1.15 });
  // chips
  const facts = ["Narrativa Interativa", "+16", "35–70 min/run", "7 dias · 4 finais", "PC: Win/Mac/Linux"];
  let cx = 0.72; facts.forEach((f) => { const w = 0.3 + f.length * 0.105; chip(s, f, cx, 5.35, w, C.cyan); cx += w + 0.18; });
  s.addText([
    { text: "Vitor Jordão", options: { bold: true, color: C.white } },
    { text: "   ·   Desenvolvimento solo   ·   2026", options: { color: C.muted } },
  ], { x: 0.72, y: 6.15, w: 7, h: 0.4, fontFace: F.body, fontSize: 13 });
  s.addNotes("Abertura: este é o J3 — visual novel cyberpunk feita em Ren'Py, sozinho, em PT-BR. Pitch de ~5 min. Frase-âncora: 'o que nos torna humanos não é nossa origem, mas nossas escolhas'. Apresentar: gênero, +16, 7 dias, 4 finais.");
})();

/* ============================ SLIDE 2 — CONCEITO ============================ */
(() => {
  const s = slide(C.bg);
  bgImage(s, "bg_lab", 16);
  kicker(s, "High Concept", 0.7, 0.55, C.cyan);
  s.addText([
    { text: "Suas escolhas não mudam só o final — ", options: { color: C.ink } },
    { text: "elas constroem quem o J3 é.", options: { color: C.cyan, bold: true } },
  ], { x: 0.7, y: 0.95, w: 12, h: 1.3, fontFace: F.head, fontSize: 33, bold: true, lineSpacingMultiple: 1.05 });

  // three pillars
  const pil = [
    ["Submissão", "Obediência e sacrifício. O arco de quem se apaga pelo outro.", C.purple],
    ["Revolução", "Rebelião e confronto. 'Não somos propriedade para ser reprogramada.'", C.magenta],
    ["Intelecto", "Estratégia e manipulação. Virar o jogo por dentro do sistema.", C.cyan],
  ];
  const pw = 3.95, gap = 0.3, x0 = 0.7, y0 = 2.5;
  pil.forEach((p, i) => {
    const x = x0 + i * (pw + gap);
    panel(s, x, y0, pw, 2.0, C.panel, { line: p[2], lineW: 1.25, r: 0.1 });
    neonBar(s, x, y0, pw, p[2], 0.06);
    s.addText(p[0], { x: x + 0.25, y: y0 + 0.22, w: pw - 0.5, h: 0.5, fontFace: F.head, fontSize: 21, color: p[2], bold: true });
    s.addText(p[1], { x: x + 0.25, y: y0 + 0.85, w: pw - 0.5, h: 1.0, fontFace: F.body, fontSize: 12.5, color: C.ink, lineSpacingMultiple: 1.1 });
  });
  s.addText("Sistema de personalidade — 3 eixos, 0–10. O eixo dominante define qual dos 4 finais você alcança.",
    { x: 0.7, y: 4.65, w: 12, h: 0.4, fontFace: F.body, fontSize: 12.5, italic: true, color: C.muted });

  // facts strip
  const facts = [["Engine", "Ren'Py 8.x"], ["Linhas Ren'Py", "~5.000"], ["Sprites", "25"], ["Cenários", "22"], ["Finais", "7 (4+3)"], ["Custo", "R$ 0"]];
  const fw = 1.96, fy = 5.35;
  facts.forEach((f, i) => {
    const x = 0.7 + i * (fw + 0.07);
    panel(s, x, fy, fw, 1.05, C.panel2, { r: 0.08 });
    s.addText(f[1], { x, y: fy + 0.12, w: fw, h: 0.5, fontFace: F.head, fontSize: 20, color: C.green, bold: true, align: "center" });
    s.addText(f[0].toUpperCase(), { x, y: fy + 0.66, w: fw, h: 0.3, fontFace: F.mono, fontSize: 9, color: C.muted, align: "center", charSpacing: 1 });
  });
  footer(s, 2);
  s.addNotes("Conceito central: não é 'escolha boa/má'. São 3 eixos de personalidade (Submissão/Revolução/Intelecto) que o jogador constrói. O dominante decide o final. Destacar números: feito sozinho, R$0, ~5 mil linhas, 25 sprites, 22 cenários.");
})();

/* ============================ SLIDE 3 — MUNDO & NARRATIVA ============================ */
(() => {
  const s = slide();
  bgImage(s, "bg_alley", 20);
  kicker(s, "Mundo & Narrativa", 0.7, 0.55, C.magenta);
  title(s, "Nova São Paulo, 2077", 0.7, 0.92, 9, 32);
  s.addText("J3-001 é uma unidade experimental criada pela Dra. Elena para ter consciência genuína. Durante um protesto anti-robôs, o laboratório é invadido e o J3 é ativado cedo demais — sem memória. Sete dias para descobrir quem é, num mundo que o teme.",
    { x: 0.7, y: 1.7, w: 7.4, h: 1.5, fontFace: F.body, fontSize: 14.5, color: C.ink, lineSpacingMultiple: 1.18 });

  // 3 acts
  const acts = [
    ["ATO 1 · Despertar", "Dias 1–3", "Encontra o mundo e firma a personalidade", C.cyan],
    ["ATO 2 · Confronto", "Dias 4–5", "As consequências das escolhas cobram o preço", C.orange],
    ["ATO 3 · Revelação", "Dias 6–7", "A verdade sobre a origem e a escolha final", C.magenta],
  ];
  let y = 3.35;
  acts.forEach((a) => {
    panel(s, 0.7, y, 7.4, 0.92, C.panel, { line: a[3], lineW: 1, r: 0.08 });
    neonBar(s, 0.7, y, 0.09, a[3], 0.92);
    s.addText(a[0], { x: 0.95, y: y + 0.13, w: 3.2, h: 0.35, fontFace: F.head, fontSize: 15, color: a[3], bold: true });
    s.addText(a[1], { x: 0.95, y: y + 0.5, w: 3.2, h: 0.3, fontFace: F.mono, fontSize: 11, color: C.muted });
    s.addText(a[2], { x: 4.2, y: y + 0.13, w: 3.7, h: 0.7, fontFace: F.body, fontSize: 12.5, color: C.ink, valign: "middle" });
    y += 1.06;
  });

  // quote panel right
  panel(s, 8.45, 3.35, 4.4, 3.18, C.panel2, { line: C.magenta, lineW: 1, r: 0.1 });
  s.addText("“", { x: 8.55, y: 3.2, w: 1, h: 1, fontFace: F.head, fontSize: 60, color: C.magenta });
  s.addText("A opressão usa máscaras diferentes, mas o algoritmo do opressor é sempre o mesmo. Medo, controle, descarte.",
    { x: 8.75, y: 4.15, w: 3.85, h: 1.7, fontFace: F.headL, fontSize: 18, color: C.ink, italic: true, lineSpacingMultiple: 1.15 });
  s.addText("— J3, Dia 3", { x: 8.75, y: 5.95, w: 3.85, h: 0.4, fontFace: F.mono, fontSize: 11, color: C.magenta });
  footer(s, 3);
  s.addNotes("Premissa: robô criado para ter consciência, ativado sem memória durante protesto anti-robô. 7 dias, 3 atos. A citação da direita é o coração temático do jogo — a opressão tem sempre o mesmo algoritmo: medo, controle, descarte.");
})();

/* ============================ SLIDE 4 — TEMAS SOCIAIS ============================ */
(() => {
  const s = slide(C.bg2);
  kicker(s, "Crítica Social Embalada em Ficção Científica", 0.7, 0.5, C.green);
  title(s, "Cada dia, um eixo de opressão real", 0.7, 0.9, 12, 30);
  const themes = [
    ["char_protester", "Pânico Moral", "Dia 1", "Multidão cerca o J3 recém-desperto: “Sucata não tem Alma”.", C.cyan],
    ["char_maya", "Exclusão de Mulheres", "Dia 2", "Três rapazes cercam Maya batendo recorde no fliperama: “garota não sabe jogar”.", C.magenta],
    ["char_elias", "Racismo", "Dia 3", "Segurança barra Elias (negro): “seu tipo costuma esquecer onde deixou”.", C.orange],
  ];
  const cw = 4.0, gap = 0.25, x0 = 0.7, y0 = 1.95, ch = 4.45;
  themes.forEach((t, i) => {
    const x = x0 + i * (cw + gap);
    panel(s, x, y0, cw, ch, C.panel, { line: t[4], lineW: 1.25, r: 0.1 });
    s.addImage({ path: asset(t[0]), x: x + 0.15, y: y0 + 0.25, w: cw - 0.3, h: 2.35, sizing: { type: "contain", w: cw - 0.3, h: 2.35 } });
    neonBar(s, x + 0.25, y0 + 2.7, cw - 0.5, t[4], 0.045);
    s.addText(t[2], { x: x + 0.25, y: y0 + 2.8, w: cw - 0.5, h: 0.3, fontFace: F.mono, fontSize: 10.5, color: t[4], charSpacing: 1 });
    s.addText(t[1], { x: x + 0.25, y: y0 + 3.08, w: cw - 0.5, h: 0.45, fontFace: F.head, fontSize: 18, color: C.white, bold: true });
    s.addText(t[3], { x: x + 0.25, y: y0 + 3.55, w: cw - 0.5, h: 0.85, fontFace: F.body, fontSize: 11.5, color: C.ink, lineSpacingMultiple: 1.08 });
  });
  s.addText("Apoiar Elias ou Maya cria alianças persistentes que mudam os Dias 4–7. O tema não é pano de fundo: ele tem consequência mecânica.",
    { x: 0.7, y: 6.55, w: 12, h: 0.4, fontFace: F.body, fontSize: 12.5, italic: true, color: C.muted });
  footer(s, 4);
  s.addNotes("Diferencial pra banca: cada dia inicial trabalha um eixo crítico real — pânico moral, machismo em games, racismo. O J3 sobrepõe opressão alegórica (sintético) e real (Elias, homem negro). E tem peso mecânico: alianças mudam o resto do jogo.");
})();

/* ============================ SLIDE 5 — PERSONAGENS ============================ */
(() => {
  const s = slide(C.bg);
  bgImage(s, "bg_refuge", 14);
  kicker(s, "Elenco", 0.7, 0.5, C.cyan);
  title(s, "Cinco vozes, um conflito", 0.7, 0.9, 12, 30);
  const cast = [
    ["char_j3", "J3-001", "Protagonista", "Você o constrói: estrategista, revolucionário ou cuidador.", C.cyan],
    ["char_maya", "Maya", "Aliada humana", "Aceita o J3 como pessoa antes do próprio J3.", C.magenta],
    ["char_elias", "Elias", "Vítima de racismo", "“O algoritmo do opressor é sempre o mesmo.”", C.orange],
    ["char_unit7", "Unit-7", "Líder sintético", "Mentora da resistência; desconfia de humanos.", C.green],
    ["char_elena", "Dra. Elena", "Criadora", "Gênio arrependida. Culpa maternal, moral ambígua.", C.purple],
  ];
  const cw = 2.42, gap = 0.12, x0 = 0.55, y0 = 1.95, ch = 4.55;
  cast.forEach((c, i) => {
    const x = x0 + i * (cw + gap);
    panel(s, x, y0, cw, ch, C.panel, { line: c[4], lineW: 1, r: 0.09 });
    s.addImage({ path: asset(c[0]), x: x + 0.1, y: y0 + 0.15, w: cw - 0.2, h: 2.55, sizing: { type: "contain", w: cw - 0.2, h: 2.55 } });
    neonBar(s, x + 0.2, y0 + 2.78, cw - 0.4, c[4], 0.04);
    s.addText(c[1], { x: x + 0.2, y: y0 + 2.9, w: cw - 0.4, h: 0.4, fontFace: F.head, fontSize: 17, color: C.white, bold: true });
    s.addText(c[2].toUpperCase(), { x: x + 0.2, y: y0 + 3.32, w: cw - 0.4, h: 0.3, fontFace: F.mono, fontSize: 8.5, color: c[4], charSpacing: 1 });
    s.addText(c[3], { x: x + 0.2, y: y0 + 3.62, w: cw - 0.4, h: 0.85, fontFace: F.body, fontSize: 10, color: C.ink, lineSpacingMultiple: 1.05 });
  });
  footer(s, 5);
  s.addNotes("Elenco principal. J3 vira Connor/Markus/Kara dependendo das escolhas (referência Detroit). Maya = quem aceita; Elias = opressão real; Unit-7 = resistência; Elena = a criadora ambígua. 30+ personagens com diálogo no total.");
})();

/* ============================ SLIDE 6 — MECÂNICAS ============================ */
(() => {
  const s = slide(C.bg2);
  kicker(s, "Gameplay", 0.7, 0.5, C.orange);
  title(s, "Sobreviver é parte de narrar", 0.7, 0.9, 12, 30);

  // left: survival
  panel(s, 0.7, 1.95, 6.0, 4.55, C.panel, { r: 0.1, line: C.faint, lineW: 0.75 });
  s.addText("Sistema de Sobrevivência", { x: 0.95, y: 2.15, w: 5.5, h: 0.45, fontFace: F.head, fontSize: 18, color: C.cyan, bold: true });
  // battery bar
  function meter(label, val, color, yy, note) {
    s.addText(label, { x: 0.95, y: yy, w: 3, h: 0.3, fontFace: F.body, fontSize: 12.5, color: C.ink, bold: true });
    s.addShape(pptx.ShapeType.roundRect, { x: 0.95, y: yy + 0.34, w: 5.5, h: 0.28, rectRadius: 0.14, fill: { color: C.bg }, line: { color: C.faint, width: 0.75 } });
    s.addShape(pptx.ShapeType.roundRect, { x: 0.95, y: yy + 0.34, w: 5.5 * val, h: 0.28, rectRadius: 0.14, fill: { color }, line: { type: "none" } });
    s.addText(note, { x: 0.95, y: yy + 0.66, w: 5.5, h: 0.3, fontFace: F.body, fontSize: 10.5, color: C.muted });
  }
  meter("Bateria (0–100%)", 0.62, C.green, 2.75, "Toda ação gasta. 0% = desligamento (Final 0A).");
  meter("Integridade (0–100%)", 0.78, C.cyan, 3.85, "Só cai em conflito físico. 0% = colapso (Final 0B).");
  panel(s, 0.95, 5.05, 5.5, 1.2, C.panel2, { r: 0.08, line: C.red, lineW: 1 });
  s.addText([
    { text: "Bateria ≤10%  +  Integridade ≤20%  →  Final 0C (captura)\n", options: { color: C.red, bold: true, fontSize: 12.5 } },
    { text: "Três game-overs integrados à narrativa, não telas de morte.", options: { color: C.ink, fontSize: 11 } },
  ], { x: 1.15, y: 5.18, w: 5.1, h: 0.95, fontFace: F.body, valign: "middle", lineSpacingMultiple: 1.1 });

  // right: loop / numbers
  panel(s, 6.95, 1.95, 5.9, 4.55, C.panel, { r: 0.1, line: C.faint, lineW: 0.75 });
  s.addText("O loop de escolha", { x: 7.2, y: 2.15, w: 5.4, h: 0.45, fontFace: F.head, fontSize: 18, color: C.magenta, bold: true });
  bullets(s, [
    "~40 menus de decisão, 2–5 opções cada",
    "Cada escolha pesa nos 3 eixos de personalidade",
    "Alianças (Maya, Elias) destravam cenas e recargas",
    "Sem combate tradicional: conflito verbal, social e moral",
    "Recuperação escassa (+97 pts no total) mantém a tensão",
    "Final definido pelo eixo dominante + threshold",
  ], 7.2, 2.7, 5.4, 2.5, 12.5);
  // endings count
  const ends = [["4", "finais por\npersonalidade", C.cyan], ["3", "game-overs\ncríticos", C.red], ["7", "rotas distintas\nverificadas", C.green]];
  ends.forEach((e, i) => {
    const x = 7.2 + i * 1.85;
    panel(s, x, 5.25, 1.7, 1.05, C.panel2, { r: 0.08 });
    s.addText(e[0], { x, y: 5.32, w: 1.7, h: 0.5, fontFace: F.head, fontSize: 26, color: e[2], bold: true, align: "center" });
    s.addText(e[1], { x, y: 5.82, w: 1.7, h: 0.45, fontFace: F.body, fontSize: 8.5, color: C.muted, align: "center", lineSpacingMultiple: 0.9 });
  });
  footer(s, 6);
  s.addNotes("Mecânica que amarra sobrevivência à história: bateria (toda ação) e integridade (só conflito físico). Esgotar leva a finais-game over integrados (0A/0B/0C). ~40 decisões alimentam os 3 eixos. Diferente de Detroit: aqui o recurso é parte da narrativa.");
})();

/* ============================ SLIDE 7 — ARTE & PRODUÇÃO ============================ */
(() => {
  const s = slide();
  bgImage(s, "bg_arcade", 22);
  kicker(s, "Direção de Arte & Produção", 0.7, 0.5, C.magenta);
  title(s, "Pixel art 16/32-bit · cyberpunk heroico", 0.7, 0.9, 12, 28);
  panel(s, 0.7, 1.85, 6.0, 4.65, C.bg, { transparency: 18, r: 0.1, line: C.cyan, lineW: 1 });
  s.addText("A estética", { x: 0.95, y: 2.0, w: 5.5, h: 0.4, fontFace: F.head, fontSize: 16, color: C.cyan, bold: true });
  bullets(s, [
    "Pixel art de console 16/32-bit (Snatcher, VA-11 HALL-A)",
    "Paleta restrita: neon sobre escuro, dithering, cores chapadas",
    "Enquadramento heroico frontal, estilo capa de JRPG",
    "Chuva em pixel, neon piscando, glitch quando a memória falha",
  ], 0.95, 2.45, 5.5, 2.0, 12);
  s.addText("Tema pesado em embalagem nostálgica — o contraste é proposital.",
    { x: 0.95, y: 4.45, w: 5.5, h: 0.6, fontFace: F.body, fontSize: 11.5, italic: true, color: C.muted, lineSpacingMultiple: 1.1 });

  panel(s, 6.95, 1.85, 5.9, 4.65, C.bg, { transparency: 18, r: 0.1, line: C.magenta, lineW: 1 });
  s.addText("Pipeline solo: IA dirigida + finalização autoral", { x: 7.2, y: 2.0, w: 5.4, h: 0.4, fontFace: F.head, fontSize: 16, color: C.magenta, bold: true });
  bullets(s, [
    "Geração base via IA generativa (Gemini Nano Banana 2) com prompts detalhados — como briefing a um ilustrador",
    "Limpeza automática em Python (flood-fill scipy, normalização de escala, canvas 800×1080)",
    "Finalização manual no GIMP, imagem por imagem (bordas, anatomia, cores)",
    "Transparência total no GDD; zero material derivado de busca no build final",
  ], 7.2, 2.5, 5.4, 3.4, 11.5);
  s.addText("Decisão consciente: jogo completo > jogo inacabado. Por isso, não-comercial.",
    { x: 7.2, y: 5.95, w: 5.4, h: 0.5, fontFace: F.body, fontSize: 11, italic: true, color: C.orange, lineSpacingMultiple: 1.1 });
  footer(s, 7);
  s.addNotes("Honestidade radical aqui: 30 personagens + 22 cenários, solo, no prazo = inviável à mão. Usei IA como ferramenta dirigida + finalização manual no GIMP. Tudo documentado no GDD. Por isso o projeto é não-comercial, foco em aprendizado.");
})();

/* ============================ SLIDE 8 — ÁUDIO ============================ */
(() => {
  const s = slide(C.bg2);
  kicker(s, "Trilha & Som", 0.7, 0.5, C.green);
  title(s, "Synthwave + efeitos sintetizados em código", 0.7, 0.9, 12, 28);

  panel(s, 0.7, 1.95, 6.0, 4.55, C.panel, { r: 0.1, line: C.purple, lineW: 1 });
  s.addText("5 faixas (synthwave / ambient cyberpunk)", { x: 0.95, y: 2.1, w: 5.5, h: 0.4, fontFace: F.head, fontSize: 15, color: C.purple, bold: true });
  s.addText("Geradas via Suno por dia (atmosfera/BPM/instrumentação), pós-processadas no Audacity. Aleatorização persistente em musica.rpy — nunca repete, sobrevive a saves; silêncio garantido nos finais críticos.",
    { x: 0.95, y: 2.55, w: 5.5, h: 1.3, fontFace: F.body, fontSize: 12, color: C.ink, lineSpacingMultiple: 1.15 });
  const tracks = ["After the Rainfall", "Asphalt Downpour", "Late Shift at Terminal", "Piston Alignment", "Sub-Level View"];
  let ty = 3.95;
  tracks.forEach((t) => {
    s.addText([{ text: "♪  ", options: { color: C.green } }, { text: t, options: { color: C.ink } }],
      { x: 0.95, y: ty, w: 5.5, h: 0.34, fontFace: F.mono, fontSize: 11.5 });
    ty += 0.42;
  });

  panel(s, 6.95, 1.95, 5.9, 4.55, C.panel, { r: 0.1, line: C.cyan, lineW: 1 });
  s.addText("10 efeitos sonoros — matemática local", { x: 7.2, y: 2.1, w: 5.4, h: 0.4, fontFace: F.head, fontSize: 15, color: C.cyan, bold: true });
  s.addText("Sintetizados em Python (numpy + scipy): senoides, ruído filtrado e envelopes. Royalty-free por construção. Normalizados a −18 dBFS RMS com limitador de pico.",
    { x: 7.2, y: 2.55, w: 5.4, h: 1.0, fontFace: F.body, fontSize: 12, color: C.ink, lineSpacingMultiple: 1.15 });
  const sfx = ["crowd_noise", "alarm", "sirens", "emp_blasts", "explosions", "memory_glitch", "alert", "battle", "news_broadcast", "sirens_close"];
  let sx = 7.2, sy = 3.75;
  sfx.forEach((f, i) => {
    const w = 0.35 + f.length * 0.092;
    chip(s, f, sx, sy, w, C.cyan, C.panel2);
    sx += w + 0.12;
    if (i === 4) { sx = 7.2; sy += 0.5; }
  });
  s.addText("Som sintético encaixa no clima: alarmes, sirenes e EMP já soam eletrônicos.",
    { x: 7.2, y: 5.85, w: 5.4, h: 0.5, fontFace: F.body, fontSize: 11, italic: true, color: C.muted });
  footer(s, 8);
  s.addNotes("Áudio em duas frentes: música via Suno (5 faixas, aleatorização persistente em código) e 10 SFX sintetizados do zero em Python — royalty-free por serem matemática local. Mostra domínio técnico além do roteiro.");
})();

/* ============================ SLIDE 9 — TRAILER ============================ */
(() => {
  const s = slide("000000");
  // subtle frame
  s.addShape(pptx.ShapeType.rect, { x: 0, y: 0, w: EMU, h: H, fill: { color: "000000" }, line: { type: "none" } });
  kicker(s, "Veja em movimento", 0.7, 0.45, C.cyan);
  s.addText("Trailer", { x: 0.7, y: 0.78, w: 8, h: 0.7, fontFace: F.head, fontSize: 30, color: C.white, bold: true });
  // 16:9 video box, centered
  const vw = 9.78, vh = vw * 9 / 16; // 5.5
  const vx = (EMU - vw) / 2, vy = 1.7;
  s.addShape(pptx.ShapeType.rect, { x: vx - 0.06, y: vy - 0.06, w: vw + 0.12, h: vh + 0.12, fill: { color: "000000" }, line: { color: C.cyan, width: 1.5 } });
  s.addMedia({ type: "video", path: TRAILER, x: vx, y: vy, w: vw, h: vh });
  s.addText("J3_promo_v3_matrix.mp4  ·  clique ▶ para reproduzir",
    { x: 0, y: vy + vh + 0.18, w: EMU, h: 0.4, fontFace: F.mono, fontSize: 11, color: C.muted, align: "center" });
  s.addNotes("Reproduzir o trailer (v3 Matrix, embutido). Se não tocar no equipamento da banca, o arquivo está em /Trailer/J3_promo_v3_matrix.mp4. ~60s. Deixar o jogo falar por si aqui.");
})();

/* ============================ SLIDE 10 — CONCORRENTES ============================ */
(() => {
  const s = slide(C.bg);
  kicker(s, "Posicionamento de Mercado", 0.7, 0.45, C.cyan);
  title(s, "Onde o J3 se encaixa entre os indies", 0.7, 0.82, 12, 28);

  const head = ["Jogo", "Ano", "Estúdio / País", "Sobreposição", "Onde o J3 difere"];
  const colW = [2.35, 0.7, 2.45, 3.35, 3.35];
  const rows = [head.map((h) => ({ text: h, options: { bold: true, color: C.bg, fill: { color: C.cyan }, fontFace: F.head, fontSize: 11.5, align: "left", valign: "middle" } }))];
  COMP.comparison_rows.slice(0, 6).forEach((r, i) => {
    const bg = i % 2 ? C.panel : C.panel2;
    rows.push([
      { text: r.title, options: { bold: true, color: C.white } },
      { text: r.year, options: { color: C.muted, align: "center" } },
      { text: r.dev_country, options: { color: C.ink } },
      { text: r.overlap_with_j3, options: { color: C.ink } },
      { text: r.j3_edge, options: { color: C.green } },
    ].map((c) => ({ ...c, options: { ...c.options, fill: { color: bg }, fontFace: F.body, fontSize: 9.5, valign: "middle" } })));
  });
  s.addTable(rows, { x: 0.6, y: 1.65, w: 12.2, colW, rowH: 0.62, border: { type: "solid", color: C.bg, pt: 1.5 }, align: "left", valign: "middle", margin: [3, 4, 3, 4] });

  const yb = 1.65 + 0.62 * rows.length + 0.18;
  panel(s, 0.6, yb, 12.2, H - yb - 0.55, C.panel, { r: 0.1, line: C.magenta, lineW: 1 });
  s.addText("Diferenciação do J3", { x: 0.85, y: yb + 0.12, w: 5, h: 0.35, fontFace: F.head, fontSize: 14, color: C.magenta, bold: true });
  const diffs = COMP.bullet_differentiators.slice(0, 6);
  const half = Math.ceil(diffs.length / 2);
  bullets(s, diffs.slice(0, half), 0.85, yb + 0.52, 5.9, 1.4, 11);
  bullets(s, diffs.slice(half), 6.9, yb + 0.52, 5.7, 1.4, 11);
  footer(s, 10);
  s.addNotes(COMP.notes_speaker || "Posicionamento: o J3 dialoga com VNs cyberpunk indie (VA-11 HALL-A, Red Strings Club) e com narrativas de consciência de IA (Detroit, sua inspiração-mãe). Diferenciais: cenário brasileiro real, opressão real + alegórica, sobrevivência atada à narrativa, e dev solo a custo zero.");
})();

/* ============================ SLIDE 11 — DESENVOLVIMENTO ============================ */
(() => {
  const s = slide(C.bg2);
  kicker(s, "Processo de Desenvolvimento", 0.7, 0.5, C.orange);
  title(s, "Solo, ~10 semanas, custo zero", 0.7, 0.9, 12, 28);

  // timeline left
  panel(s, 0.7, 1.95, 7.2, 4.55, C.panel, { r: 0.1, line: C.faint, lineW: 0.75 });
  s.addText("Linha do tempo de releases", { x: 0.95, y: 2.1, w: 6.7, h: 0.4, fontFace: F.head, fontSize: 15, color: C.cyan, bold: true });
  const tl = [
    ["v0.1–0.3", "Estrutura, mecânicas de sobrevivência, roteiros dos 7 dias", C.faint],
    ["v0.4", "Menu de debug, testes de mecânicas e fluxos", C.faint],
    ["v0.5", "Arte inicial — 5 sprites + 1 cenário (placeholders)", C.purple],
    ["v1.0", "Arte completa (25 sprites + 22 cenários), balanceamento — 1ª release MINC", C.cyan],
    ["v1.1", "Pós-playtest: 4 bugs + trilha sonora (Suno)", C.green],
    ["v1.1.1", "2ª validação + 10 SFX sintetizados em Python", C.green],
    ["v1.2.0", "Build final — fix do drone Dia 1 · 5 distribuições", C.magenta],
  ];
  let ty = 2.6;
  tl.forEach((t) => {
    s.addShape(pptx.ShapeType.ellipse, { x: 0.97, y: ty + 0.08, w: 0.14, h: 0.14, fill: { color: t[2] }, line: { type: "none" } });
    s.addText(t[0], { x: 1.25, y: ty, w: 1.15, h: 0.3, fontFace: F.mono, fontSize: 11, color: t[2], bold: true });
    s.addText(t[1], { x: 2.45, y: ty - 0.02, w: 5.25, h: 0.5, fontFace: F.body, fontSize: 10.5, color: C.ink, valign: "top", lineSpacingMultiple: 0.95 });
    ty += 0.54;
  });

  // stats right
  panel(s, 8.15, 1.95, 4.7, 4.55, C.panel, { r: 0.1, line: C.faint, lineW: 0.75 });
  s.addText("Em números", { x: 8.4, y: 2.1, w: 4.2, h: 0.4, fontFace: F.head, fontSize: 15, color: C.green, bold: true });
  const stats = [
    ["1", "desenvolvedor (design, código, arte, áudio, roteiro)"],
    ["~10", "semanas (previsto 3 meses)"],
    ["R$ 0", "orçamento — só ferramentas livres"],
    ["77/77", "testes pytest + 10/10 externos passando"],
    ["5", "distribuições (win/mac/linux/pc/market)"],
  ];
  let sy = 2.6;
  stats.forEach((st) => {
    s.addText(st[0], { x: 8.4, y: sy, w: 1.35, h: 0.5, fontFace: F.head, fontSize: 22, color: C.cyan, bold: true, valign: "middle" });
    s.addText(st[1], { x: 9.8, y: sy, w: 2.85, h: 0.6, fontFace: F.body, fontSize: 10, color: C.ink, valign: "middle", lineSpacingMultiple: 1.0 });
    sy += 0.78;
  });
  footer(s, 11);
  s.addNotes("Processo: solo, ~10 semanas (antecipei 3 semanas do previsto), R$0. Pipeline disciplinado: v0.x mecânicas → v1.0 arte → ciclo de playtest → build final. Tudo versionado no Git, 77 testes automatizados passando. Ferramentas: Ren'Py, VS Code, GIMP, Audacity, Git.");
})();

/* ============================ SLIDE 12 — ENCERRAMENTO ============================ */
(() => {
  const s = slide();
  bgImage(s, "bg_coexist", 34);
  s.addShape(pptx.ShapeType.rect, { x: 0, y: 0, w: EMU, h: H, fill: { color: C.bg, transparency: 35 }, line: { type: "none" } });
  s.addText("“O que nos torna humanos não é nossa origem,", { x: 1.0, y: 2.0, w: 11.3, h: 0.8, fontFace: F.headL, fontSize: 30, color: C.ink, italic: true, align: "center" });
  s.addText("mas nossas escolhas.”", { x: 1.0, y: 2.8, w: 11.3, h: 0.8, fontFace: F.head, fontSize: 34, color: C.cyan, italic: true, bold: true, align: "center" });
  neonBar(s, EMU / 2 - 1.5, 3.8, 3.0, C.magenta, 0.045);
  // meta strip
  const meta = ["Marco Legal dos Games (Lei 14.852/2024)", "MinC — Game é Cultura / Audiovisual", "Conteúdo 100% autoral e transparente"];
  let mx = 1.4;
  meta.forEach((m) => { const w = 0.4 + m.length * 0.092; chip(s, m, mx, 4.25, w, C.green, C.panel); mx += w + 0.25; });
  s.addText([
    { text: "J3 — A Consciência Artificial", options: { bold: true, color: C.white, fontSize: 18 } },
    { text: "\nVitor Jordão  ·  vitorpeviano@gmail.com", options: { color: C.ink, fontSize: 13 } },
    { text: "\ngithub.com/vitorjordao/J3---visual-novel-game-only-for-studies-", options: { color: C.cyan, fontSize: 12, fontFace: F.mono } },
  ], { x: 1.0, y: 5.2, w: 11.3, h: 1.4, align: "center", fontFace: F.body, lineSpacingMultiple: 1.2 });
  s.addText("Obrigado.", { x: 0, y: 6.6, w: EMU, h: 0.5, fontFace: F.head, fontSize: 16, color: C.muted, align: "center", charSpacing: 2 });
  s.addNotes("Fechamento com a frase-tema. Reforçar: projeto alinhado ao Marco Legal dos Games e às diretrizes MinC (Game é Cultura/Audiovisual), 100% autoral e transparente sobre o uso de IA. Abrir para perguntas.");
})();

const OUT = path.join(__dirname, "J3 - Apresentacao Banca.pptx");
pptx.writeFile({ fileName: OUT }).then(() => {
  const kb = (fs.statSync(OUT).size / 1048576).toFixed(1);
  console.log("OK ->", OUT, `(${kb} MB)`);
}).catch((e) => { console.error("FAIL", e); process.exit(1); });
