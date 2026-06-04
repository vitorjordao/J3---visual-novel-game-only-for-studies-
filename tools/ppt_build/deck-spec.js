/* Shared deck specification for "J3 — A Consciência Artificial" pitch.
   Builds a renderer-agnostic op tree (DECK). Consumed by render-pptx.js and
   render-svg.js so the visual preview is faithful to the real .pptx. */
const fs = require("fs");
const path = require("path");

const A = JSON.parse(fs.readFileSync(path.join(__dirname, "assets-manifest.json"), "utf8"));
const COMP = JSON.parse(fs.readFileSync(path.join(__dirname, "competitors.json"), "utf8"));
const asset = (slug) => path.join(__dirname, A[slug].file);
const aspectOf = (slug) => A[slug].aspect || null;
const TRAILER = "g:/Vitor/J3 project/Trailer/J3_promo_v3_matrix.mp4";

const EMU = 13.333, H = 7.5;
const C = {
  bg: "0A0E1A", bg2: "0E1424", panel: "151C30", panel2: "1B2440",
  ink: "E7ECF5", muted: "9AA8C2", faint: "63708C",
  cyan: "27E1E8", magenta: "FF2E97", green: "47F08A", purple: "A971FF",
  orange: "FF9F45", red: "FF5470", white: "FFFFFF", black: "000000",
};
const F = { head: "Bahnschrift SemiBold", headL: "Bahnschrift", body: "Segoe UI", mono: "Consolas" };

class Slide {
  constructor(bg = C.bg) { this.bg = bg; this.ops = []; this.notes = ""; this.bgImageSlug = null; }
  rect(x, y, w, h, o = {}) { this.ops.push({ t: "rect", x, y, w, h, r: o.r || 0, fill: o.fill, alpha: o.alpha, line: o.line, lineW: o.lineW || 1 }); return this; }
  ellipse(x, y, w, h, o = {}) { this.ops.push({ t: "ellipse", x, y, w, h, fill: o.fill }); return this; }
  image(slug, x, y, w, h, fit = "contain") { this.ops.push({ t: "image", slug, x, y, w, h, fit }); return this; }
  video(p, x, y, w, h) { this.ops.push({ t: "video", path: p, x, y, w, h }); return this; }
  table(rows, x, y, w, o = {}) { this.ops.push({ t: "table", rows, x, y, w, colW: o.colW, rowH: o.rowH, fontSize: o.fontSize }); return this; }
  text(runs, x, y, w, h, o = {}) {
    const r = Array.isArray(runs) ? runs : [{ text: runs }];
    this.ops.push({ t: "text", runs: r, x, y, w, h, font: o.font || F.body, size: o.size || 14, color: o.color || C.ink,
      bold: o.bold, italic: o.italic, align: o.align || "left", valign: o.valign || "top", charSpacing: o.charSpacing || 0,
      lineSpacing: o.lineSpacing || 1.1, bullet: o.bullet, stack: o.stack, paraAfter: o.paraAfter || 0 });
    return this;
  }
  // composite helpers
  bgImage(slug, scrim = 55) { this.bgImageSlug = slug; this.image(slug, 0, 0, EMU, H, "cover"); this.rect(0, 0, EMU, H, { fill: C.bg, alpha: 100 - scrim }); return this; }
  panel(x, y, w, h, fill = C.panel, o = {}) { this.rect(x, y, w, h, { r: o.r ?? 0.08, fill, alpha: o.alpha, line: o.line, lineW: o.lineW }); return this; }
  bar(x, y, w, color = C.cyan, h = 0.055) { this.rect(x, y, w, h, { fill: color }); return this; }
  kicker(txt, x, y, color = C.cyan, w = 7) { this.text(txt.toUpperCase(), x, y, w, 0.3, { font: F.mono, size: 11, color, bold: true, charSpacing: 3 }); return this; }
  title(txt, x, y, w, size = 32, color = C.white) { this.text(txt, x, y, w, 0.9, { font: F.head, size, color, bold: true }); return this; }
  chip(txt, x, y, w, color = C.cyan, fill = C.panel2) {
    this.rect(x, y, w, 0.36, { r: 0.18, fill, line: color, lineW: 1 });
    this.text(txt, x, y, w, 0.36, { size: 10.5, color: C.ink, align: "center", valign: "middle" });
    return this;
  }
  bullets(items, x, y, w, h, size = 14, color = C.ink) {
    this.text(items.map((t) => ({ text: t })), x, y, w, h, { size, color, lineSpacing: 1.12, paraAfter: 7, bullet: true, valign: "top" });
    return this;
  }
  footer(n) {
    this.text("J3 — A CONSCIÊNCIA ARTIFICIAL", 0.45, H - 0.4, 8, 0.3, { color: C.faint, size: 8, font: F.mono, charSpacing: 2, valign: "middle" });
    this.text(`${n} / 12`, EMU - 1.4, H - 0.4, 0.95, 0.3, { color: C.faint, size: 8, font: F.mono, align: "right", valign: "middle" });
    this.bar(0.45, H - 0.46, 0.5, C.magenta, 0.03);
    return this;
  }
  setNotes(n) { this.notes = n; return this; }
}

const DECK = [];
const add = (s) => { DECK.push(s); return s; };

/* 1 — CAPA */
{
  const s = add(new Slide());
  s.bgImage("bg_avenue", 42);
  s.rect(0, 0, 7.6, H, { fill: C.bg, alpha: 22 });
  s.image("char_j3", 8.2, 0.55, 4.8, 6.6, "contain");
  s.kicker("Visual Novel Cyberpunk · Ren'Py · PT-BR", 0.7, 0.9, C.cyan);
  s.text("J3", 0.62, 1.2, 7, 1.9, { font: F.head, size: 130, color: C.white, bold: true });
  s.text("A CONSCIÊNCIA ARTIFICIAL", 0.72, 3.05, 7, 0.7, { font: F.headL, size: 30, color: C.cyan, bold: true, charSpacing: 1 });
  s.bar(0.72, 3.74, 3.2, C.magenta, 0.05);
  s.text("Um robô sem memória descobre sua identidade através de escolhas que moldam sua alma — numa Nova São Paulo cyberpunk e preconceituosa.",
    0.72, 3.98, 6.6, 1.2, { size: 15.5, color: C.ink, lineSpacing: 1.15 });
  let cx = 0.72;
  ["Narrativa Interativa", "+16", "35–70 min/run", "7 dias · 4 finais", "PC: Win/Mac/Linux"].forEach((f) => { const w = 0.3 + f.length * 0.105; s.chip(f, cx, 5.4, w, C.cyan); cx += w + 0.18; });
  s.text([{ text: "Vitor Jordão", bold: true, color: C.white }, { text: "   ·   Desenvolvimento solo   ·   2026", color: C.muted }],
    0.72, 6.2, 7, 0.4, { size: 13 });
  s.setNotes("Abertura: este é o J3 — visual novel cyberpunk feita em Ren'Py, sozinho, em PT-BR. Pitch de ~5 min. Frase-âncora: 'o que nos torna humanos não é nossa origem, mas nossas escolhas'. Apresentar: gênero, +16, 7 dias, 4 finais.");
}

/* 2 — CONCEITO */
{
  const s = add(new Slide());
  s.bgImage("bg_lab", 16);
  s.kicker("High Concept", 0.7, 0.55, C.cyan);
  s.text([{ text: "Suas escolhas não mudam só o final — ", color: C.ink }, { text: "elas constroem quem o J3 é.", color: C.cyan, bold: true }],
    0.7, 0.95, 12, 1.3, { font: F.head, size: 33, bold: true, lineSpacing: 1.05 });
  const pil = [
    ["Submissão", "Obediência e sacrifício. O arco de quem se apaga pelo outro.", C.purple],
    ["Revolução", "Rebelião e confronto. “Não somos propriedade para ser reprogramada.”", C.magenta],
    ["Intelecto", "Estratégia e manipulação. Virar o jogo por dentro do sistema.", C.cyan],
  ];
  const pw = 3.95, gap = 0.3, x0 = 0.7, y0 = 2.5;
  pil.forEach((p, i) => {
    const x = x0 + i * (pw + gap);
    s.panel(x, y0, pw, 2.0, C.panel, { line: p[2], lineW: 1.25, r: 0.1 });
    s.bar(x, y0, pw, p[2], 0.06);
    s.text(p[0], x + 0.25, y0 + 0.22, pw - 0.5, 0.5, { font: F.head, size: 21, color: p[2], bold: true });
    s.text(p[1], x + 0.25, y0 + 0.85, pw - 0.5, 1.0, { size: 12.5, color: C.ink, lineSpacing: 1.1 });
  });
  s.text("Sistema de personalidade — 3 eixos, 0–10. O eixo dominante define qual dos 4 finais você alcança.",
    0.7, 4.65, 12, 0.4, { size: 12.5, italic: true, color: C.muted });
  const facts = [["Engine", "Ren'Py 8.x"], ["Linhas Ren'Py", "~5.000"], ["Sprites", "25"], ["Cenários", "22"], ["Finais", "7 (4+3)"], ["Custo", "R$ 0"]];
  const fw = 1.96, fy = 5.35;
  facts.forEach((f, i) => {
    const x = 0.7 + i * (fw + 0.07);
    s.panel(x, fy, fw, 1.05, C.panel2, { r: 0.08 });
    s.text(f[1], x, fy + 0.12, fw, 0.5, { font: F.head, size: 20, color: C.green, bold: true, align: "center" });
    s.text(f[0].toUpperCase(), x, fy + 0.66, fw, 0.3, { font: F.mono, size: 9, color: C.muted, align: "center", charSpacing: 1 });
  });
  s.footer(2);
  s.setNotes("Conceito central: não é 'escolha boa/má'. São 3 eixos de personalidade (Submissão/Revolução/Intelecto) que o jogador constrói. O dominante decide o final. Destacar números: feito sozinho, R$0, ~5 mil linhas, 25 sprites, 22 cenários.");
}

/* 3 — MUNDO & NARRATIVA */
{
  const s = add(new Slide());
  s.bgImage("bg_alley", 20);
  s.kicker("Mundo & Narrativa", 0.7, 0.55, C.magenta);
  s.title("Nova São Paulo, 2077", 0.7, 0.92, 9, 32);
  s.text("J3-001 é uma unidade experimental criada pela Dra. Elena para ter consciência genuína. Durante um protesto anti-robôs, o laboratório é invadido e o J3 é ativado cedo demais — sem memória. Sete dias para descobrir quem é, num mundo que o teme.",
    0.7, 1.7, 7.4, 1.5, { size: 14.5, color: C.ink, lineSpacing: 1.18 });
  const acts = [
    ["ATO 1 · Despertar", "Dias 1–3", "Encontra o mundo e firma a personalidade", C.cyan],
    ["ATO 2 · Confronto", "Dias 4–5", "As consequências das escolhas cobram o preço", C.orange],
    ["ATO 3 · Revelação", "Dias 6–7", "A verdade sobre a origem e a escolha final", C.magenta],
  ];
  let y = 3.35;
  acts.forEach((a) => {
    s.panel(0.7, y, 7.4, 0.92, C.panel, { line: a[3], lineW: 1, r: 0.08 });
    s.bar(0.7, y, 0.09, a[3], 0.92);
    s.text(a[0], 0.95, y + 0.13, 3.2, 0.35, { font: F.head, size: 15, color: a[3], bold: true });
    s.text(a[1], 0.95, y + 0.5, 3.2, 0.3, { font: F.mono, size: 11, color: C.muted });
    s.text(a[2], 4.2, y + 0.13, 3.7, 0.7, { size: 12.5, color: C.ink, valign: "middle" });
    y += 1.06;
  });
  s.panel(8.45, 3.35, 4.4, 3.18, C.panel2, { line: C.magenta, lineW: 1, r: 0.1 });
  s.text("“", 8.55, 3.2, 1, 1, { font: F.head, size: 60, color: C.magenta });
  s.text("A opressão usa máscaras diferentes, mas o algoritmo do opressor é sempre o mesmo. Medo, controle, descarte.",
    8.75, 4.15, 3.85, 1.7, { font: F.headL, size: 18, color: C.ink, italic: true, lineSpacing: 1.15 });
  s.text("— J3, Dia 3", 8.75, 5.95, 3.85, 0.4, { font: F.mono, size: 11, color: C.magenta });
  s.footer(3);
  s.setNotes("Premissa: robô criado para ter consciência, ativado sem memória durante protesto anti-robô. 7 dias, 3 atos. A citação da direita é o coração temático do jogo — a opressão tem sempre o mesmo algoritmo: medo, controle, descarte.");
}

/* 4 — TEMAS SOCIAIS */
{
  const s = add(new Slide(C.bg2));
  s.kicker("Crítica Social Embalada em Ficção Científica", 0.7, 0.5, C.green, 11);
  s.title("Cada dia, um eixo de opressão real", 0.7, 0.9, 12, 30);
  const themes = [
    ["char_protester", "Pânico Moral", "Dia 1", "Multidão cerca o J3 recém-desperto: “Sucata não tem Alma”.", C.cyan],
    ["char_maya", "Exclusão de Mulheres", "Dia 2", "Três rapazes cercam Maya batendo recorde no fliperama: “garota não sabe jogar”.", C.magenta],
    ["char_elias", "Racismo", "Dia 3", "Segurança barra Elias (negro): “seu tipo costuma esquecer onde deixou”.", C.orange],
  ];
  const cw = 4.0, gap = 0.25, x0 = 0.7, y0 = 1.95, ch = 4.45;
  themes.forEach((t, i) => {
    const x = x0 + i * (cw + gap);
    s.panel(x, y0, cw, ch, C.panel, { line: t[5], lineW: 1.25, r: 0.1 });
    s.image(t[0], x + 0.15, y0 + 0.25, cw - 0.3, 2.35, "contain");
    s.bar(x + 0.25, y0 + 2.7, cw - 0.5, t[5], 0.045);
    s.text(t[2], x + 0.25, y0 + 2.8, cw - 0.5, 0.3, { font: F.mono, size: 10.5, color: t[5], charSpacing: 1 });
    s.text(t[1], x + 0.25, y0 + 3.08, cw - 0.5, 0.45, { font: F.head, size: 18, color: C.white, bold: true });
    s.text(t[3], x + 0.25, y0 + 3.55, cw - 0.5, 0.85, { size: 11.5, color: C.ink, lineSpacing: 1.08 });
  });
  s.text("Apoiar Elias ou Maya cria alianças persistentes que mudam os Dias 4–7. O tema não é pano de fundo: ele tem consequência mecânica.",
    0.7, 6.55, 12, 0.4, { size: 12.5, italic: true, color: C.muted });
  s.footer(4);
  s.setNotes("Diferencial pra banca: cada dia inicial trabalha um eixo crítico real — pânico moral, machismo em games, racismo. O J3 sobrepõe opressão alegórica (sintético) e real (Elias, homem negro). E tem peso mecânico: alianças mudam o resto do jogo.");
}

/* 5 — PERSONAGENS */
{
  const s = add(new Slide());
  s.bgImage("bg_refuge", 14);
  s.kicker("Elenco", 0.7, 0.5, C.cyan);
  s.title("Cinco vozes, um conflito", 0.7, 0.9, 12, 30);
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
    s.panel(x, y0, cw, ch, C.panel, { line: c[4], lineW: 1, r: 0.09 });
    s.image(c[0], x + 0.1, y0 + 0.15, cw - 0.2, 2.55, "contain");
    s.bar(x + 0.2, y0 + 2.78, cw - 0.4, c[4], 0.04);
    s.text(c[1], x + 0.2, y0 + 2.9, cw - 0.4, 0.4, { font: F.head, size: 17, color: C.white, bold: true });
    s.text(c[2].toUpperCase(), x + 0.2, y0 + 3.32, cw - 0.4, 0.3, { font: F.mono, size: 8.5, color: c[4], charSpacing: 1 });
    s.text(c[3], x + 0.2, y0 + 3.62, cw - 0.4, 0.85, { size: 10, color: C.ink, lineSpacing: 1.05 });
  });
  s.footer(5);
  s.setNotes("Elenco principal. J3 vira Connor/Markus/Kara dependendo das escolhas (referência Detroit). Maya = quem aceita; Elias = opressão real; Unit-7 = resistência; Elena = a criadora ambígua. 30+ personagens com diálogo no total.");
}

/* 6 — MECÂNICAS */
{
  const s = add(new Slide(C.bg2));
  s.kicker("Gameplay", 0.7, 0.5, C.orange);
  s.title("Sobreviver é parte de narrar", 0.7, 0.9, 12, 30);
  s.panel(0.7, 1.95, 6.0, 4.55, C.panel, { r: 0.1, line: C.faint, lineW: 0.75 });
  s.text("Sistema de Sobrevivência", 0.95, 2.15, 5.5, 0.45, { font: F.head, size: 18, color: C.cyan, bold: true });
  const meter = (label, val, color, yy, note) => {
    s.text(label, 0.95, yy, 3, 0.3, { size: 12.5, color: C.ink, bold: true });
    s.rect(0.95, yy + 0.34, 5.5, 0.28, { r: 0.14, fill: C.bg, line: C.faint, lineW: 0.75 });
    s.rect(0.95, yy + 0.34, 5.5 * val, 0.28, { r: 0.14, fill: color });
    s.text(note, 0.95, yy + 0.66, 5.5, 0.3, { size: 10.5, color: C.muted });
  };
  meter("Bateria (0–100%)", 0.62, C.green, 2.75, "Toda ação gasta. 0% = desligamento (Final 0A).");
  meter("Integridade (0–100%)", 0.78, C.cyan, 3.85, "Só cai em conflito físico. 0% = colapso (Final 0B).");
  s.panel(0.95, 5.05, 5.5, 1.2, C.panel2, { r: 0.08, line: C.red, lineW: 1 });
  s.text([{ text: "Bateria ≤10%  +  Integridade ≤20%  →  Final 0C (captura)", color: C.red, bold: true, size: 12.5 },
    { text: "Três game-overs integrados à narrativa, não telas de morte.", color: C.ink, size: 11 }],
    1.15, 5.18, 5.1, 0.95, { valign: "middle", lineSpacing: 1.1, stack: true });
  s.panel(6.95, 1.95, 5.9, 4.55, C.panel, { r: 0.1, line: C.faint, lineW: 0.75 });
  s.text("O loop de escolha", 7.2, 2.15, 5.4, 0.45, { font: F.head, size: 18, color: C.magenta, bold: true });
  s.bullets([
    "~40 menus de decisão, 2–5 opções cada",
    "Cada escolha pesa nos 3 eixos de personalidade",
    "Alianças (Maya, Elias) destravam cenas e recargas",
    "Sem combate tradicional: conflito verbal, social e moral",
    "Recuperação escassa (+97 pts no total) mantém a tensão",
    "Final definido pelo eixo dominante + threshold",
  ], 7.2, 2.7, 5.4, 2.5, 12.5);
  const ends = [["4", "finais por personalidade", C.cyan], ["3", "game-overs críticos", C.red], ["7", "rotas verificadas", C.green]];
  ends.forEach((e, i) => {
    const x = 7.2 + i * 1.85;
    s.panel(x, 5.25, 1.7, 1.05, C.panel2, { r: 0.08 });
    s.text(e[0], x, 5.32, 1.7, 0.5, { font: F.head, size: 26, color: e[2], bold: true, align: "center" });
    s.text(e[1], x, 5.85, 1.7, 0.45, { size: 8.5, color: C.muted, align: "center", lineSpacing: 0.95 });
  });
  s.footer(6);
  s.setNotes("Mecânica que amarra sobrevivência à história: bateria (toda ação) e integridade (só conflito físico). Esgotar leva a finais-game over integrados (0A/0B/0C). ~40 decisões alimentam os 3 eixos. Diferente de Detroit: aqui o recurso é parte da narrativa.");
}

/* 7 — ARTE & PRODUÇÃO */
{
  const s = add(new Slide());
  s.bgImage("bg_arcade", 22);
  s.kicker("Direção de Arte & Produção", 0.7, 0.5, C.magenta);
  s.title("Pixel art 16/32-bit · cyberpunk heroico", 0.7, 0.9, 12, 28);
  s.panel(0.7, 1.85, 6.0, 4.65, C.bg, { alpha: 18, r: 0.1, line: C.cyan, lineW: 1 });
  s.text("A estética", 0.95, 2.0, 5.5, 0.4, { font: F.head, size: 16, color: C.cyan, bold: true });
  s.bullets([
    "Pixel art de console 16/32-bit (Snatcher, VA-11 HALL-A)",
    "Paleta restrita: neon sobre escuro, dithering, cores chapadas",
    "Enquadramento heroico frontal, estilo capa de JRPG",
    "Chuva em pixel, neon piscando, glitch quando a memória falha",
  ], 0.95, 2.45, 5.5, 2.0, 12);
  s.text("Tema pesado em embalagem nostálgica — o contraste é proposital.",
    0.95, 4.5, 5.5, 0.6, { size: 11.5, italic: true, color: C.muted, lineSpacing: 1.1 });
  s.panel(6.95, 1.85, 5.9, 4.65, C.bg, { alpha: 18, r: 0.1, line: C.magenta, lineW: 1 });
  s.text("Pipeline solo: IA dirigida + finalização autoral", 7.2, 2.0, 5.4, 0.4, { font: F.head, size: 16, color: C.magenta, bold: true });
  s.bullets([
    "Geração base via IA generativa (Gemini Nano Banana 2) com prompts detalhados — como briefing a um ilustrador",
    "Limpeza automática em Python (flood-fill scipy, normalização de escala, canvas 800×1080)",
    "Finalização manual no GIMP, imagem por imagem (bordas, anatomia, cores)",
    "Transparência total no GDD; zero material derivado de busca no build final",
  ], 7.2, 2.5, 5.4, 3.4, 11.5);
  s.text("Decisão consciente: jogo completo > jogo inacabado. Por isso, não-comercial.",
    7.2, 5.95, 5.4, 0.5, { size: 11, italic: true, color: C.orange, lineSpacing: 1.1 });
  s.footer(7);
  s.setNotes("Honestidade radical aqui: 30 personagens + 22 cenários, solo, no prazo = inviável à mão. Usei IA como ferramenta dirigida + finalização manual no GIMP. Tudo documentado no GDD. Por isso o projeto é não-comercial, foco em aprendizado.");
}

/* 8 — ÁUDIO */
{
  const s = add(new Slide(C.bg2));
  s.kicker("Trilha & Som", 0.7, 0.5, C.green);
  s.title("Synthwave + efeitos sintetizados em código", 0.7, 0.9, 12, 28);
  s.panel(0.7, 1.95, 6.0, 4.55, C.panel, { r: 0.1, line: C.purple, lineW: 1 });
  s.text("5 faixas (synthwave / ambient cyberpunk)", 0.95, 2.1, 5.5, 0.4, { font: F.head, size: 15, color: C.purple, bold: true });
  s.text("Geradas via Suno por dia (atmosfera/BPM/instrumentação), pós-processadas no Audacity. Aleatorização persistente em musica.rpy — nunca repete, sobrevive a saves; silêncio garantido nos finais críticos.",
    0.95, 2.55, 5.5, 1.3, { size: 12, color: C.ink, lineSpacing: 1.15 });
  let ty = 3.95;
  ["After the Rainfall", "Asphalt Downpour", "Late Shift at Terminal", "Piston Alignment", "Sub-Level View"].forEach((t) => {
    s.text([{ text: "♪  ", color: C.green }, { text: t, color: C.ink }], 0.95, ty, 5.5, 0.34, { font: F.mono, size: 11.5 });
    ty += 0.42;
  });
  s.panel(6.95, 1.95, 5.9, 4.55, C.panel, { r: 0.1, line: C.cyan, lineW: 1 });
  s.text("10 efeitos sonoros — matemática local", 7.2, 2.1, 5.4, 0.4, { font: F.head, size: 15, color: C.cyan, bold: true });
  s.text("Sintetizados em Python (numpy + scipy): senoides, ruído filtrado e envelopes. Royalty-free por construção. Normalizados a −18 dBFS RMS com limitador de pico.",
    7.2, 2.55, 5.4, 1.0, { size: 12, color: C.ink, lineSpacing: 1.15 });
  const sfx = ["crowd_noise", "alarm", "sirens", "emp_blasts", "explosions", "memory_glitch", "alert", "battle", "news_broadcast", "sirens_close"];
  let sx = 7.2, sy = 3.75;
  sfx.forEach((f, i) => { const w = 0.35 + f.length * 0.092; s.chip(f, sx, sy, w, C.cyan, C.panel2); sx += w + 0.12; if (i === 4) { sx = 7.2; sy += 0.5; } });
  s.text("Som sintético encaixa no clima: alarmes, sirenes e EMP já soam eletrônicos.",
    7.2, 5.85, 5.4, 0.5, { size: 11, italic: true, color: C.muted });
  s.footer(8);
  s.setNotes("Áudio em duas frentes: música via Suno (5 faixas, aleatorização persistente em código) e 10 SFX sintetizados do zero em Python — royalty-free por serem matemática local. Mostra domínio técnico além do roteiro.");
}

/* 9 — TRAILER */
{
  const s = add(new Slide("000000"));
  s.kicker("Veja em movimento", 0.7, 0.45, C.cyan);
  s.text("Trailer", 0.7, 0.78, 8, 0.7, { font: F.head, size: 30, color: C.white, bold: true });
  const vw = 9.78, vh = vw * 9 / 16, vx = (EMU - vw) / 2, vy = 1.7;
  s.rect(vx - 0.06, vy - 0.06, vw + 0.12, vh + 0.12, { fill: C.black, line: C.cyan, lineW: 1.5 });
  s.video(TRAILER, vx, vy, vw, vh);
  s.text("J3_promo_v3_matrix.mp4  ·  clique ▶ para reproduzir", 0, vy + vh + 0.18, EMU, 0.4, { font: F.mono, size: 11, color: C.muted, align: "center" });
  s.setNotes("Reproduzir o trailer (v3 Matrix, embutido). Se não tocar no equipamento da banca, o arquivo está em /Trailer/J3_promo_v3_matrix.mp4. ~60s. Deixar o jogo falar por si aqui.");
}

/* 10 — CONCORRENTES */
{
  const s = add(new Slide());
  s.kicker("Posicionamento de Mercado", 0.7, 0.45, C.cyan);
  s.title("Onde o J3 se encaixa entre os indies", 0.7, 0.82, 12, 28);
  const head = ["Jogo", "Ano", "Estúdio / País", "Sobreposição", "Onde o J3 difere"];
  const colW = [2.35, 0.7, 2.45, 3.35, 3.35];
  const rows = [head.map((h) => ({ text: h, bold: true, color: C.bg, fill: C.cyan, font: F.head, size: 11.5 }))];
  COMP.comparison_rows.slice(0, 6).forEach((r, i) => {
    const bg = i % 2 ? C.panel : C.panel2;
    rows.push([
      { text: r.title, bold: true, color: C.white, fill: bg },
      { text: r.year, color: C.muted, fill: bg, align: "center" },
      { text: r.dev_country, color: C.ink, fill: bg },
      { text: r.overlap_with_j3, color: C.ink, fill: bg },
      { text: r.j3_edge, color: C.green, fill: bg },
    ]);
  });
  s.table(rows, 0.6, 1.55, 12.2, { colW, rowH: 0.58, fontSize: 9 });
  const yb = 1.55 + 0.58 * rows.length + 0.16;
  s.panel(0.6, yb, 12.2, 7.0 - yb, C.panel, { r: 0.1, line: C.magenta, lineW: 1 });
  s.bar(0.6, yb, 0.09, C.magenta, 7.0 - yb);
  s.text("Diferenciação do J3", 0.85, yb + 0.1, 6, 0.32, { font: F.head, size: 14, color: C.magenta, bold: true });
  const diffs = [
    "Única VN cyberpunk brasileira em PT-BR/Ren'Py sobre consciência de IA.",
    "Opressão real + alegórica do Brasil no núcleo: racismo, gênero, pânico moral.",
    "Sobrevivência (bateria/integridade) fundida à narrativa, não HUD decorativo.",
    "3 eixos → 4 finais + 3 game-overs críticos: alta rejogabilidade.",
    "Ambição de Detroit em escala solo, ao lado de comps premiados de micro-equipe.",
    "Elegível a fomento: Marco Legal dos Games + MinC (Game é Cultura/Audiovisual).",
  ];
  s.bullets(diffs.slice(0, 3), 0.85, yb + 0.46, 5.95, 0.85, 10.5);
  s.bullets(diffs.slice(3), 6.9, yb + 0.46, 5.7, 0.85, 10.5);
  s.footer(10);
  s.setNotes(COMP.notes_speaker);
}

/* 11 — DESENVOLVIMENTO */
{
  const s = add(new Slide(C.bg2));
  s.kicker("Processo de Desenvolvimento", 0.7, 0.5, C.orange);
  s.title("Solo, ~10 semanas, custo zero", 0.7, 0.9, 12, 28);
  s.panel(0.7, 1.95, 7.2, 4.55, C.panel, { r: 0.1, line: C.faint, lineW: 0.75 });
  s.text("Linha do tempo de releases", 0.95, 2.1, 6.7, 0.4, { font: F.head, size: 15, color: C.cyan, bold: true });
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
    s.ellipse(0.97, ty + 0.08, 0.14, 0.14, { fill: t[2] });
    s.text(t[0], 1.25, ty, 1.15, 0.3, { font: F.mono, size: 11, color: t[2], bold: true });
    s.text(t[1], 2.45, ty - 0.02, 5.25, 0.5, { size: 10.5, color: C.ink, lineSpacing: 0.95 });
    ty += 0.54;
  });
  s.panel(8.15, 1.95, 4.7, 4.55, C.panel, { r: 0.1, line: C.faint, lineW: 0.75 });
  s.text("Em números", 8.4, 2.1, 4.2, 0.4, { font: F.head, size: 15, color: C.green, bold: true });
  const stats = [
    ["1", "desenvolvedor (design, código, arte, áudio, roteiro)"],
    ["~10", "semanas (previsto 3 meses)"],
    ["R$ 0", "orçamento — só ferramentas livres"],
    ["77/77", "testes pytest + 10/10 externos passando"],
    ["5", "distribuições (win/mac/linux/pc/market)"],
  ];
  let sy = 2.6;
  stats.forEach((st) => {
    s.text(st[0], 8.4, sy, 1.35, 0.5, { font: F.head, size: 22, color: C.cyan, bold: true, valign: "middle" });
    s.text(st[1], 9.8, sy, 2.85, 0.6, { size: 10, color: C.ink, valign: "middle", lineSpacing: 1.0 });
    sy += 0.78;
  });
  s.footer(11);
  s.setNotes("Processo: solo, ~10 semanas (antecipei 3 semanas do previsto), R$0. Pipeline disciplinado: v0.x mecânicas → v1.0 arte → ciclo de playtest → build final. Tudo versionado no Git, 77 testes automatizados passando. Ferramentas: Ren'Py, VS Code, GIMP, Audacity, Git.");
}

/* 12 — ENCERRAMENTO */
{
  const s = add(new Slide());
  s.bgImage("bg_crossroads", 32);
  s.rect(0, 0, EMU, H, { fill: C.bg, alpha: 35 });
  s.text("“O que nos torna humanos não é nossa origem,", 1.0, 2.0, 11.3, 0.8, { font: F.headL, size: 30, color: C.ink, italic: true, align: "center" });
  s.text("mas nossas escolhas.”", 1.0, 2.8, 11.3, 0.8, { font: F.head, size: 34, color: C.cyan, italic: true, bold: true, align: "center" });
  s.bar(EMU / 2 - 1.5, 3.8, 3.0, C.magenta, 0.045);
  let mx = 1.4;
  ["Marco Legal dos Games (Lei 14.852/2024)", "MinC — Game é Cultura / Audiovisual", "Conteúdo 100% autoral e transparente"].forEach((m) => { const w = 0.4 + m.length * 0.092; s.chip(m, mx, 4.25, w, C.green, C.panel); mx += w + 0.25; });
  s.text([{ text: "J3 — A Consciência Artificial", bold: true, color: C.white, size: 18 },
    { text: "Vitor Jordão  ·  vitorpeviano@gmail.com", color: C.ink, size: 13 },
    { text: "github.com/vitorjordao/J3---visual-novel-game-only-for-studies-", color: C.cyan, size: 12, font: F.mono }],
    1.0, 5.2, 11.3, 1.4, { align: "center", lineSpacing: 1.4, stack: true });
  s.text("Obrigado.", 0, 6.6, EMU, 0.5, { font: F.head, size: 16, color: C.muted, align: "center", charSpacing: 2 });
  s.setNotes("Fechamento com a frase-tema. Reforçar: projeto alinhado ao Marco Legal dos Games e às diretrizes MinC (Game é Cultura/Audiovisual), 100% autoral e transparente sobre o uso de IA. Abrir para perguntas.");
}

module.exports = { DECK, C, F, EMU, H, asset, aspectOf, A };
