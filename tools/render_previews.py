#!/usr/bin/env python3
"""Render previews from the actual encoded atlas without redrawing the character."""

import argparse
from pathlib import Path

from PIL import Image, ImageDraw

STATES = [("idle", 6), ("running-right", 8), ("running-left", 8),
          ("waving", 4), ("jumping", 5), ("failed", 8),
          ("waiting", 6), ("running", 6), ("review", 6)]


def cell(atlas, row, column):
    return atlas.crop((column * 192, row * 208, (column + 1) * 192, (row + 1) * 208))


def preview(frame, label):
    canvas = Image.new("RGBA", (256, 256), "#eef0f3")
    canvas.alpha_composite(frame, (32, 34))
    ImageDraw.Draw(canvas).text((12, 10), label, fill="#19212b")
    return canvas.convert("RGB")


def gif(frames, path, duration=150):
    frames[0].save(path, save_all=True, append_images=frames[1:],
                   duration=duration, loop=0, disposal=2, optimize=False)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("atlas", type=Path)
    parser.add_argument("--output-dir", type=Path, default=Path("preview"))
    parser.add_argument("--mp4", action="store_true", help="Requires optional imageio-ffmpeg")
    args = parser.parse_args()
    atlas = Image.open(args.atlas).convert("RGBA")
    if atlas.size not in {(1536, 1872), (1536, 2288)}:
        parser.error("Expected a supported v1/v2 atlas")
    out = args.output_dir
    out.mkdir(parents=True, exist_ok=True)
    cell(atlas, 0, 0).save(out / "chotu-icon.png")
    all_frames = []
    for row, (state, count) in enumerate(STATES):
        frames = [preview(cell(atlas, row, col), state) for col in range(count)]
        gif(frames, out / f"{state}.gif")
        all_frames.extend(frames)
    gif(all_frames, out / "all-states.gif")
    jump_transition = ([preview(cell(atlas, 0, col), "idle") for col in range(6)]
                       + [preview(cell(atlas, 4, col), "jumping") for col in range(5)]
                       + [preview(cell(atlas, 0, col), "idle") for col in range(6)])
    gif(jump_transition, out / "idle-jump-idle.gif")
    stills = Image.new("RGB", (1024, 256), "#eef0f3")
    for index, (row, col, label) in enumerate([(0, 0, "Idle"), (4, 1, "Rising"),
                                             (4, 2, "Airborne"), (4, 4, "Landed")]):
        still = preview(cell(atlas, row, col), label)
        still.save(out / f"jump-still-{index + 1}.png")
        stills.paste(still, (index * 256, 0))
    stills.save(out / "jump-transition.png")
    if atlas.height == 2288:
        gif([preview(cell(atlas, 9 + n // 8, n % 8), f"Look {n * 22.5:g} degrees")
             for n in range(16)], out / "look-loop.gif", duration=240)
    if args.mp4:
        import imageio_ffmpeg
        writer = imageio_ffmpeg.write_frames(str(out / "all-states.mp4"), (256, 256),
                                             fps=20, codec="libx264", pix_fmt_in="rgb24",
                                             pix_fmt_out="yuv420p")
        writer.send(None)
        for frame in all_frames:
            for _ in range(3):
                writer.send(frame.tobytes())
        writer.close()


if __name__ == "__main__":
    main()
