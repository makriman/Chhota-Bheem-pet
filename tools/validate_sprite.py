#!/usr/bin/env python3
"""Check Chotu's encoded atlas geometry; visual/motion review is also required."""

import argparse
import hashlib
import json
from pathlib import Path
from statistics import median

from PIL import Image

CELL = (192, 208)
COUNTS = [6, 8, 8, 4, 5, 8, 6, 6, 6]


def validate(path):
    raw = path.read_bytes()
    errors = []
    with Image.open(path) as opened:
        image = opened.convert("RGBA")
        image_format = opened.format
    if image_format not in {"PNG", "WEBP"}:
        errors.append("Expected a PNG or WebP image")
    if len(raw) > 20 * 1024 * 1024:
        errors.append("Image exceeds 20 MiB")
    residue = sum(1 for red, green, blue, alpha in image.getdata()
                  if alpha == 0 and (red or green or blue))
    if residue:
        errors.append(f"{residue} transparent pixels retain hidden RGB values")
    if image.size not in {(1536, 1872), (1536, 2288)}:
        errors.append(f"Unsupported dimensions: {image.size}")
        return {"ok": False, "errors": errors}
    version = 2 if image.height == 2288 else 1
    counts = COUNTS + ([8, 8] if version == 2 else [])
    bounds = {}
    for row, count in enumerate(counts):
        for col in range(8):
            cell = image.crop((col * 192, row * 208, (col + 1) * 192, (row + 1) * 208))
            box = cell.getchannel("A").getbbox()
            bounds[row, col] = box
            if col < count and box is None:
                errors.append(f"Missing artwork at row {row}, column {col}")
            if col >= count and box is not None:
                errors.append(f"Unused cell contains artwork: row {row}, column {col}")
            if box and cell.getchannel("A").getextrema()[0] > 0:
                errors.append(f"Cell has no transparent background: row {row}, column {col}")
    idle = [bounds[0, col] for col in range(6)]
    jumping = [bounds[4, col] for col in range(5)]
    motion = None
    if all(idle + jumping):
        baseline = round(median(box[3] for box in idle))
        feet = [box[3] for box in jumping]
        motion = {"idle_baseline": baseline, "jump_baselines": feet,
                  "lift_pixels": max(feet) - min(feet), "landing_delta_pixels": abs(feet[-1] - baseline)}
        if motion["lift_pixels"] < 8:
            errors.append("Jump has less than 8px of airborne lift")
        if motion["landing_delta_pixels"] > 12:
            errors.append("Jump landing differs from idle baseline by more than 12px")
    return {"ok": not errors, "file": str(path), "sha256": hashlib.sha256(raw).hexdigest(),
            "encoded_bytes": len(raw), "format": image_format, "size": list(image.size),
            "transparent_rgb_residue_pixels": residue,
            "sprite_version": version, "frames_per_row": counts, "motion_geometry": motion,
            "errors": errors, "scope": "Pixel geometry only. Direction meaning, identity, and playback require visual review."}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("atlas", type=Path)
    parser.add_argument("--json-out", type=Path)
    args = parser.parse_args()
    report = validate(args.atlas)
    encoded = json.dumps(report, indent=2) + "\n"
    if args.json_out:
        args.json_out.parent.mkdir(parents=True, exist_ok=True)
        args.json_out.write_text(encoded)
    print(encoded, end="")
    raise SystemExit(0 if report["ok"] else 1)


if __name__ == "__main__":
    main()
