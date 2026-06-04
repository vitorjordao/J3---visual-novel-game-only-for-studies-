// Copies the images the deck needs into ./assets with extensions matching their
// TRUE format (several source "*.png" backgrounds are actually JPEG). pptxgenjs
// infers MIME from the extension, so a JPEG named .png renders blank in PowerPoint.
const fs = require("fs");
const path = require("path");

const GAME = "g:/Vitor/J3 project/Projeto/J3 Project/game";
const OUT = path.join(__dirname, "assets");
fs.mkdirSync(OUT, { recursive: true });

function detect(buf) {
  if (buf[0] === 0x89 && buf[1] === 0x50) return "png";
  if (buf[0] === 0xff && buf[1] === 0xd8) return "jpg";
  if (buf.slice(0, 4).toString() === "RIFF") return "webp";
  if (buf.slice(0, 3).toString() === "GIF") return "gif";
  return null;
}
function pngHasAlpha(buf) {
  // IHDR color type byte is at IHDR data offset+9 (length4+type4 then width4 height4 bitdepth1 colortype1)
  const j = buf.indexOf("IHDR");
  if (j < 0) return false;
  const colorType = buf[j + 4 + 9]; // 4=tag already counted by indexOf? indexOf gives start of "IHDR"
  // buf[j..j+3]="IHDR"; data starts at j+4; width(4)height(4)bitdepth(1)colortype(1)
  const ct = buf[j + 4 + 8 + 1];
  return ct === 6 || ct === 4; // RGBA or grayscale+alpha
}

// slug -> source relative path
const WANT = {
  bg_avenue: "backgrounds/day1/avenue_night.png",
  bg_arcade: "backgrounds/day2/arcade_night.png",
  bg_alley: "backgrounds/day3/alley_night.png",
  bg_refuge: "backgrounds/day4/refuge_underground.png",
  bg_siege: "backgrounds/day5/refuge_siege.png",
  bg_lab: "backgrounds/day6/abandoned_lab.png",
  bg_crossroads: "backgrounds/day7/neutral_crossroads.png",
  bg_coexist: "backgrounds/day7/coexistence_scene.png",
  bg_control: "backgrounds/day7/control_center.png",
  char_j3: "characters/j3/J3.png",
  char_maya: "characters/maya/maya.png",
  char_elias: "characters/elias/Elias.png",
  char_unit7: "characters/unit7/unity 7.png",
  char_elena: "characters/elena/elena.png",
  char_commander: "characters/commander/commander.png",
  char_protester: "characters/protester/protester.png",
  char_maria: "characters/maria/maria.png",
  char_synth_army: "characters/synth_army/synth_army.png",
};

const manifest = {};
for (const [slug, rel] of Object.entries(WANT)) {
  const src = path.join(GAME, rel);
  if (!fs.existsSync(src)) { console.error("MISSING", rel); continue; }
  const buf = fs.readFileSync(src);
  const ext = detect(buf);
  if (!ext) { console.error("UNKNOWN FORMAT", rel); continue; }
  const dest = path.join(OUT, `${slug}.${ext}`);
  fs.writeFileSync(dest, buf);
  manifest[slug] = { file: `assets/${slug}.${ext}`, ext, alpha: ext === "png" ? pngHasAlpha(buf) : false, bytes: buf.length };
}
fs.writeFileSync(path.join(__dirname, "assets-manifest.json"), JSON.stringify(manifest, null, 2));
for (const [k, v] of Object.entries(manifest)) console.log(k.padEnd(16), v.ext.padEnd(4), (v.alpha ? "alpha" : "     "), (v.bytes / 1024).toFixed(0) + "KB", v.file);
console.log("\nWrote", Object.keys(manifest).length, "assets + assets-manifest.json");
