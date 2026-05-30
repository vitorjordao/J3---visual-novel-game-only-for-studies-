#!/usr/bin/env python3
"""
Recenter a sprite horizontally so the body's opaque bounding box is centered
in the canvas. Use case: regenerated sprites where character body is off-center.

Backs up original to _backups/<name>_recenter_<timestamp>.png.
"""
from __future__ import annotations

import argparse
import shutil
import sys
from datetime import datetime
from pathlib import Path

from PIL import Image


def opaque_bbox(img: Image.Image, alpha_threshold: int = 50):
    """Bbox of pixels with alpha > threshold (ignores faint noise pixels)."""
    alpha = img.split()[-1]
    mask = alpha.point(lambda a: 255 if a > alpha_threshold else 0)
    return mask.getbbox()


def recenter(path: Path, backup: bool = True) -> dict:
    img = Image.open(path).convert("RGBA")
    w, h = img.size
    bbox = opaque_bbox(img, alpha_threshold=50)
    if not bbox:
        return {"path": str(path), "status": "empty", "offset": 0}
    left, top, right, bottom = bbox
    body_cx = (left + right) // 2
    canvas_cx = w // 2
    offset = canvas_cx - body_cx
    if abs(offset) <= 2:
        return {"path": str(path), "status": "ok_no_change", "offset": offset,
                "body_bbox": list(bbox), "canvas": [w, h]}

    if backup:
        backup_dir = path.parent / "_backups"
        backup_dir.mkdir(exist_ok=True)
        stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_path = backup_dir / f"{path.stem}_{stamp}{path.suffix}"
        shutil.copy2(path, backup_path)
        backup_status = str(backup_path)
    else:
        backup_status = None

    new_canvas = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    # paste shifted by +offset (positive = shift right)
    new_canvas.paste(img, (offset, 0), img)
    new_canvas.save(path)
    return {
        "path": str(path),
        "status": "recentered",
        "offset_applied": offset,
        "backup": backup_status,
        "body_bbox_before": list(bbox),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("paths", nargs="+", type=Path, help="PNG files to recenter")
    parser.add_argument("--no-backup", action="store_true")
    args = parser.parse_args()
    for p in args.paths:
        result = recenter(p, backup=not args.no_backup)
        print(result)
    return 0


if __name__ == "__main__":
    sys.exit(main())
