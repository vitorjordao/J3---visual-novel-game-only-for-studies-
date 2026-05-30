#!/usr/bin/env python3
"""
Sprite Composite QA — gera renders visuais de sprites em escala efetiva
emulando o que sprite_norm + transforms left/center/right produzem em runtime.

Sem precisar do Ren'Py rodando. Saida: tools/qa/composites/.

Outputs:
- sprite_grid.png: todos os personagens em escala uniforme (validacao de proporcao).
- scene_*.png: emulacao de cenas-chave (Dia 1 Maria, Dia 5 synth_angry, etc.)
- composite_findings.json: anomalias detectadas (sprite muito grande/pequeno relativo a outros).
"""
from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass, asdict
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

# Replicates _char_map from images.rpy (tag -> sprite path).
CHAR_MAP = {
    "j3": "characters/j3/J3.png",
    "j3_revolutionary": "characters/j3/J3.png",
    "j3_serving": "characters/j3/J3.png",
    "j3_empty": "characters/j3/J3.png",
    "j3_hacker": "characters/j3/J3.png",
    "elena_scientist": "characters/elena/elena.png",
    "maya": "characters/maya/maya.png",
    "elias": "characters/elias/Elias.png",
    "elena": "characters/elena/elena.png",
    "unit7": "characters/unit7/unity 7.png",
    "damaged_bot": "characters/damaged_bot/damaged_bot.png",
    "synth1": "characters/synth1/synth1.png",
    "synth2": "characters/synth2/synth2.png",
    "child_curious": "characters/child_curious/child_curious.png",
    "synth_army": "characters/synth_army/synth_army.png",
    "drone_captor": "characters/drone_captor/drone_captor.png",
    "security": "characters/security/security.png",
    "mother": "characters/mother/mother.png",
    "thug1": "characters/thug1/thug1.png",
    "thug2": "characters/thug2/thug2.png",
    "owner": "characters/owner/owner.png",
    "homeless_woman": "characters/homeless_woman/homeless_woman.png",
    "synth_fearful": "characters/synth_fearful/synth_fearful.png",
    "synth_angry": "characters/synth_angry/synth_angry.png",
    "commander": "characters/commander/commander.png",
    "synth_survivor": "characters/synth_survivor/synth_survivor.png",
    "protester": "characters/protester/protester.png",
    "maria": "characters/maria/maria.png",
    "patrol_drone": "characters/patrol_drone/patrol_drone.png",
    "news_vendor": "characters/news_vendor/news_vendor.png",
}

SPRITE_SCALE = {"maria": 0.65, "child_curious": 0.65, "synth_army": 2.2}
SPRITE_NO_NORM = {"patrol_drone"}

# Screen + bbox + transform geometry replicates images.rpy + sistema_j3.rpy
SCREEN_W = 1920
SCREEN_H = 1080
BBOX_W = 2000
BBOX_H = 1080

# transforms in images.rpy:
#   left:   xcenter 0.15  zoom 0.85  yalign 1.0
#   center: xcenter 0.50  zoom 0.85  yalign 1.0
#   right:  xcenter 0.85  zoom 0.85  yalign 1.0
#   far_left:  xcenter 0.10 zoom 0.75 yalign 1.0
#   far_right: xcenter 0.90 zoom 0.75 yalign 1.0
TRANSFORMS = {
    "left":      {"xcenter": 0.15, "yalign": 1.0, "zoom": 0.85},
    "center":    {"xcenter": 0.50, "yalign": 1.0, "zoom": 0.85},
    "right":     {"xcenter": 0.85, "yalign": 1.0, "zoom": 0.85},
    "far_left":  {"xcenter": 0.10, "yalign": 1.0, "zoom": 0.75},
    "far_right": {"xcenter": 0.90, "yalign": 1.0, "zoom": 0.75},
    "small_bot_center": {"xcenter": 0.50, "yanchor": 1.0, "ypos": 0.74, "zoom": 1.2},
}


@dataclass
class Finding:
    severity: str
    check: str
    sprite: str
    message: str

    def as_dict(self):
        return asdict(self)


def normalize_sprite(img: Image.Image, tag: str) -> Image.Image:
    """Replicate sprite_norm(path, tag) from images.rpy."""
    if tag in SPRITE_NO_NORM:
        return img
    scale = SPRITE_SCALE.get(tag, 1.0)
    bw = int(BBOX_W * scale)
    bh = int(BBOX_H * scale)
    # fit="contain": preserve aspect, contain inside bbox, center.
    src_w, src_h = img.size
    sx = bw / src_w
    sy = bh / src_h
    s = min(sx, sy)
    new_w = max(1, int(src_w * s))
    new_h = max(1, int(src_h * s))
    scaled = img.resize((new_w, new_h), Image.LANCZOS)
    canvas = Image.new("RGBA", (bw, bh), (0, 0, 0, 0))
    canvas.paste(scaled, ((bw - new_w) // 2, (bh - new_h) // 2), scaled)
    return canvas


def apply_transform(img: Image.Image, transform: str) -> tuple[Image.Image, int, int]:
    """Apply a positional transform. Returns (transformed_img, x_offset, y_offset)
    where offsets are top-left of img on the 1920x1080 screen."""
    t = TRANSFORMS[transform]
    zoom = t["zoom"]
    w, h = img.size
    nw, nh = int(w * zoom), int(h * zoom)
    scaled = img.resize((nw, nh), Image.LANCZOS)
    if "xcenter" in t:
        cx = int(SCREEN_W * t["xcenter"])
        x = cx - nw // 2
    else:
        x = 0
    if "yalign" in t:
        # bottom of image at yalign*screen_h
        y = int(SCREEN_H * t["yalign"]) - nh
    elif "ypos" in t and "yanchor" in t:
        # yanchor 1.0 + ypos 0.74 = bottom of image at 0.74*screen_h
        y = int(SCREEN_H * t["ypos"]) - int(nh * t["yanchor"])
    else:
        y = 0
    return scaled, x, y


def opaque_bbox(img: Image.Image) -> tuple[int, int, int, int] | None:
    """Bounding box of non-transparent pixels."""
    if img.mode != "RGBA":
        img = img.convert("RGBA")
    return img.getbbox()


def measure_body(img: Image.Image, tag: str) -> dict:
    """Measure body content: opaque bbox after normalization."""
    norm = normalize_sprite(img, tag)
    bbox = opaque_bbox(norm)
    if not bbox:
        return {"tag": tag, "body_w": 0, "body_h": 0, "norm_w": norm.size[0], "norm_h": norm.size[1]}
    l, t, r, b = bbox
    return {
        "tag": tag,
        "body_w": r - l,
        "body_h": b - t,
        "norm_w": norm.size[0],
        "norm_h": norm.size[1],
        "body_x_center_offset": ((l + r) // 2) - norm.size[0] // 2,
    }


def render_scene(sprite_imgs: list[tuple[Image.Image, str, str]], bg_color=(20, 20, 40, 255)) -> Image.Image:
    """Render simulated scene. sprite_imgs: list of (img, tag, transform)."""
    screen = Image.new("RGBA", (SCREEN_W, SCREEN_H), bg_color)
    # Draw textbox simulator
    draw = ImageDraw.Draw(screen)
    draw.rectangle([(0, 800), (SCREEN_W, SCREEN_H)], fill=(0, 0, 0, 180))
    draw.rectangle([(0, 800), (SCREEN_W, 805)], fill=(0, 255, 204, 255))
    # Composite sprites
    for img, tag, transform in sprite_imgs:
        norm = normalize_sprite(img, tag)
        scaled, x, y = apply_transform(norm, transform)
        screen.paste(scaled, (x, y), scaled)
    return screen


def label_scene(img: Image.Image, title: str, notes: list[str]) -> Image.Image:
    """Add title and notes to scene image."""
    out = Image.new("RGBA", (img.size[0], img.size[1] + 80), (10, 10, 10, 255))
    out.paste(img, (0, 80))
    draw = ImageDraw.Draw(out)
    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 24)
        small = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 14)
    except OSError:
        font = ImageFont.load_default()
        small = ImageFont.load_default()
    draw.text((20, 15), title, fill=(0, 255, 204), font=font)
    y = 45
    for note in notes:
        draw.text((20, y), note, fill=(200, 200, 200), font=small)
        y += 18
    return out


def build_sprite_grid(sprite_root: Path, out_path: Path) -> dict:
    """Render all chars in a grid showing effective normalized height."""
    measurements = []
    norm_imgs = []
    cell_w = 200
    cell_h = 320
    cols = 6
    for tag, rel in sorted(CHAR_MAP.items()):
        path = sprite_root / rel
        if not path.exists():
            continue
        try:
            img = Image.open(path).convert("RGBA")
        except Exception as e:
            print(f"  fail to load {tag}: {e}", file=sys.stderr)
            continue
        m = measure_body(img, tag)
        m["path"] = str(rel)
        m["src_w"], m["src_h"] = img.size
        measurements.append(m)

        norm = normalize_sprite(img, tag)
        # Display: scale to cell_h max
        s = (cell_h - 30) / norm.size[1]
        new_w = int(norm.size[0] * s)
        new_h = int(norm.size[1] * s)
        thumb = norm.resize((new_w, new_h), Image.LANCZOS)
        norm_imgs.append((tag, thumb, m))

    rows = (len(norm_imgs) + cols - 1) // cols
    grid_w = cell_w * cols + 20
    grid_h = cell_h * rows + 60
    grid = Image.new("RGBA", (grid_w, grid_h), (15, 15, 25, 255))
    draw = ImageDraw.Draw(grid)
    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 18)
        small = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 11)
    except OSError:
        font = ImageFont.load_default()
        small = ImageFont.load_default()
    draw.text((10, 10), "J3 Sprite Grid — escala efetiva apos sprite_norm (altura normalizada relativa)",
              fill=(0, 255, 204), font=font)
    for i, (tag, thumb, m) in enumerate(norm_imgs):
        col = i % cols
        row = i // cols
        cx = 10 + col * cell_w + cell_w // 2
        cy = 50 + row * cell_h + cell_h - 15
        # Paste thumbnail centered horizontally, anchored to bottom
        tx = cx - thumb.size[0] // 2
        ty = cy - thumb.size[1]
        grid.paste(thumb, (tx, ty), thumb)
        # Label
        draw.text((10 + col * cell_w + 5, 50 + row * cell_h),
                  f"{tag}", fill=(255, 255, 255), font=font)
        # Stats
        info = f"{m['src_w']}x{m['src_h']} -> {m['norm_w']}x{m['norm_h']}"
        draw.text((10 + col * cell_w + 5, 50 + row * cell_h + 20),
                  info, fill=(180, 180, 180), font=small)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    grid.save(out_path)
    return {"path": str(out_path), "sprites": measurements}


def detect_size_outliers(measurements: list[dict]) -> list[Finding]:
    """Flag sprites whose body height deviates >25% from group median."""
    findings = []
    if not measurements:
        return findings
    heights_adult = [m["body_h"] for m in measurements
                     if m["tag"] not in ("maria", "child_curious", "damaged_bot",
                                          "patrol_drone", "drone_captor")]
    if not heights_adult:
        return findings
    sorted_h = sorted(heights_adult)
    median = sorted_h[len(sorted_h) // 2]
    for m in measurements:
        if m["tag"] in ("maria", "child_curious"):
            # Expected ~65% of adult
            expected = median * 0.65
            ratio = m["body_h"] / expected if expected else 1
            if abs(ratio - 1) > 0.35:
                findings.append(Finding(
                    severity="minor",
                    check="child_height_deviation",
                    sprite=m["tag"],
                    message=f"Body height {m['body_h']}px vs esperado ~{int(expected)}px (sprite_norm scale 0.65). Pode necessitar ajuste de _sprite_scale.",
                ))
            continue
        if m["tag"] in ("damaged_bot", "patrol_drone", "drone_captor"):
            continue
        if m["tag"] == "synth_army":
            # Upscaled via _sprite_scale 2.2 to render as background army.
            continue
        ratio = m["body_h"] / median if median else 1
        if ratio < 0.6:
            findings.append(Finding(
                severity="major",
                check="sprite_too_short",
                sprite=m["tag"],
                message=f"Body height {m['body_h']}px e {int(ratio*100)}% da mediana adulta ({median}px). Pode aparecer encolhido em cena multi-personagem.",
            ))
        elif ratio > 1.4:
            findings.append(Finding(
                severity="major",
                check="sprite_too_tall",
                sprite=m["tag"],
                message=f"Body height {m['body_h']}px e {int(ratio*100)}% da mediana adulta ({median}px). Pode aparecer gigante em cena multi-personagem.",
            ))
    # Body horizontal centering
    for m in measurements:
        offset = m.get("body_x_center_offset", 0)
        norm_w = m["norm_w"]
        if norm_w and abs(offset) > norm_w * 0.10:
            findings.append(Finding(
                severity="minor",
                check="sprite_body_off_center",
                sprite=m["tag"],
                message=f"Corpo do personagem desviado {offset:+d}px do centro do canvas. xcenter dos transforms vai posicionar a borda da imagem em vez do corpo.",
            ))
    return findings


def render_key_scenes(sprite_root: Path, out_dir: Path) -> list[dict]:
    """Render emulations of representative scenes from each day."""
    out_dir.mkdir(parents=True, exist_ok=True)
    scenes = []
    plan = [
        ("day1_protester", "Dia 1 cena 1.2 — protester at left, j3 at center",
         [("protester", "left"), ("j3", "center")],
         ["Validar: J3 deve ser maior que protester (J3 e adulto + center zoom 0.85, protester e adulto + left zoom 0.85; mesma altura).",
          "Body J3 deve estar em xcenter 0.5 = pixel 960."]),
        ("day1_maria_scene", "Dia 1 cena 1.3 — j3 at left, mother at right, maria at center",
         [("j3", "left"), ("mother", "right"), ("maria", "center")],
         ["TESTE CRITICO: Maria deve ser ~65% da altura de J3 e mae (criança 7 anos).",
          "Pego pelo override _sprite_scale = 0.65 em images.rpy."]),
        ("day2_thug_owner", "Dia 2 cena 2.5 — owner at left, thug1 at right",
         [("owner", "left"), ("thug1", "right")],
         ["Validar: ambos adultos, mesma altura."]),
        ("day3_security", "Dia 3 cena 3.4 — elias at center, security at left",
         [("security", "left"), ("elias", "center")],
         ["Validar: security e elias adultos."]),
        ("day4_damaged_bot", "Dia 4 cena 4.1 — damaged_bot at small_bot_center",
         [("damaged_bot", "small_bot_center")],
         ["Bot pequeno na parte de cima (acima do textbox).",
          "Usa small_bot_center transform (ypos 0.74)."]),
        ("day4_unit7_synth", "Dia 4 cena 4.2 — unit7 at center, synth_survivor at right",
         [("unit7", "center"), ("synth_survivor", "right")],
         ["Validar: ambos adultos."]),
        ("day4_synths", "Dia 4 cena 4.4 — synth1 at left, synth2 at right",
         [("synth1", "left"), ("synth2", "right")],
         ["Validar: synth1 (regenerado paisagem) e synth2 (retrato 800x1080) na mesma altura."]),
        ("day5_synth_battle", "Dia 5 cena 5.1 — synth_fearful at left, unit7 at center, synth_angry at right",
         [("synth_fearful", "left"), ("unit7", "center"), ("synth_angry", "right")],
         ["TESTE CRITICO: synth_angry tem aspect 1.83 (paisagem 1408x768).",
          "Apos fit=contain dentro de bbox 2000x1080, deve aparecer com aspect natural — nao espremido."]),
        ("day5_commander", "Dia 5 cena 5.6 — unit7 at center, commander at right",
         [("unit7", "center"), ("commander", "right")],
         ["Adultos militares — mesma altura."]),
        ("day6_elena", "Dia 6 cena 6.1 — elena_scientist at center, synth_survivor at center",
         [("elena", "center")],
         ["Elena (retrato 800x1080)."]),
        ("day7_revolution", "Dia 7 final revolucao — synth_army at center BEHIND, commander at center, j3 at left",
         [("synth_army", "center"), ("commander", "center"), ("j3_revolutionary", "left")],
         ["synth_army upscaled (scale 2.2) renderiza como exercito de fundo.",
          "Em runtime, day7.rpy usa 'show synth_army at center zorder -10' = fica atras dos outros.",
          "j3_revolutionary alias de J3.png."]),
        ("day7_balanced", "Dia 7 final balanceado — maya at left, elias at right, elena_scientist at center",
         [("maya", "left"), ("elena", "center"), ("elias", "right")],
         ["Tres adultos. Centro Elena = altura igual aos laterais."]),
        ("day7_serving_child", "Dia 7 final sacrificio — j3_serving (= J3 sprite) at far_right, child_curious at far_left, mother at center",
         [("j3", "far_right"), ("child_curious", "far_left"), ("mother", "center")],
         ["TESTE CRITICO: child_curious deve ser ~65% da altura de mother/j3."]),
    ]
    for slug, title, sprites, notes in plan:
        sprite_imgs = []
        missing = []
        for tag, transform in sprites:
            if tag not in CHAR_MAP:
                missing.append(tag)
                continue
            p = sprite_root / CHAR_MAP[tag]
            if not p.exists():
                missing.append(tag)
                continue
            sprite_imgs.append((Image.open(p).convert("RGBA"), tag, transform))
        if not sprite_imgs:
            continue
        scene = render_scene(sprite_imgs)
        # Sprite labels overlay
        draw = ImageDraw.Draw(scene)
        try:
            font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 16)
        except OSError:
            font = ImageFont.load_default()
        for img, tag, transform in sprite_imgs:
            t = TRANSFORMS[transform]
            cx = int(SCREEN_W * t.get("xcenter", 0.5))
            draw.text((cx - 40, 820), f"{tag} @ {transform}", fill=(255, 255, 255), font=font)
        notes_full = notes + ([f"AVISO: sprites ausentes: {missing}"] if missing else [])
        labelled = label_scene(scene, title, notes_full)
        out_path = out_dir / f"{slug}.png"
        labelled.save(out_path)
        scenes.append({"slug": slug, "title": title, "path": str(out_path), "missing": missing})
    return scenes


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--sprite-root", type=Path,
                        default=Path("Projeto/J3 Project/game"))
    parser.add_argument("--out", type=Path, default=Path("tools/qa/composites"))
    args = parser.parse_args()

    sprite_root: Path = args.sprite_root.resolve()
    out_dir: Path = args.out.resolve()
    out_dir.mkdir(parents=True, exist_ok=True)

    print(f"Building sprite grid from {sprite_root}...")
    grid_info = build_sprite_grid(sprite_root, out_dir / "sprite_grid.png")
    print(f"  Grid: {grid_info['path']} ({len(grid_info['sprites'])} sprites)")

    print("Detecting size outliers...")
    findings = detect_size_outliers(grid_info["sprites"])
    print(f"  Findings: {len(findings)}")

    print("Rendering key scenes...")
    scenes = render_key_scenes(sprite_root, out_dir / "scenes")
    print(f"  Scenes: {len(scenes)}")

    summary = {
        "version": "1.0",
        "grid": grid_info,
        "scenes": scenes,
        "findings": [f.as_dict() for f in findings],
    }
    summary_path = out_dir / "composite_findings.json"
    summary_path.write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"  Summary: {summary_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
