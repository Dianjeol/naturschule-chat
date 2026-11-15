#!/usr/bin/env python3
"""Generate square app icons (.png, .ico, .icns) from logo.png."""

from __future__ import annotations

import struct
from io import BytesIO
from pathlib import Path
from PIL import Image


def make_square_icon(src: Image.Image, canvas_size: int = 1024, padding_ratio: float = 0.08) -> Image.Image:
    """Fit an RGBA image centered onto a transparent square canvas."""
    rgba = src.convert("RGBA")
    bbox = rgba.getbbox()
    if bbox:
        rgba = rgba.crop(bbox)

    max_dim = int(canvas_size * (1.0 - 2.0 * padding_ratio))
    scale = min(max_dim / rgba.width, max_dim / rgba.height)
    new_size = (max(1, round(rgba.width * scale)), max(1, round(rgba.height * scale)))
    resized = rgba.resize(new_size, Image.Resampling.LANCZOS)

    canvas = Image.new("RGBA", (canvas_size, canvas_size), (0, 0, 0, 0))
    offset = ((canvas_size - new_size[0]) // 2, (canvas_size - new_size[1]) // 2)
    canvas.paste(resized, offset, resized)
    return canvas


def save_icns(square: Image.Image, out_path: Path) -> None:
    """Write a macOS .icns file containing PNG-compressed icon chunks."""
    chunk_types = [
        (b"ic07", 128),
        (b"ic08", 256),
        (b"ic09", 512),
        (b"ic10", 1024),
    ]
    chunks: list[bytes] = []
    for ostype, size in chunk_types:
        resized = square.resize((size, size), Image.Resampling.LANCZOS)
        buf = BytesIO()
        resized.save(buf, format="PNG")
        png_data = buf.getvalue()
        chunks.append(ostype + struct.pack(">I", 8 + len(png_data)) + png_data)

    body = b"".join(chunks)
    header = b"icns" + struct.pack(">I", 8 + len(body))
    out_path.write_bytes(header + body)


def main() -> None:
    root = Path(__file__).resolve().parent.parent
    logo_path = root / "logo.png"
    icons_dir = root / "icons"
    icons_dir.mkdir(parents=True, exist_ok=True)

    with Image.open(logo_path) as src:
        square_1024 = make_square_icon(src, canvas_size=1024, padding_ratio=0.06)

    # Linux / System Tray PNG (512x512)
    png_512 = square_1024.resize((512, 512), Image.Resampling.LANCZOS)
    png_512.save(icons_dir / "icon.png", format="PNG")

    # Windows multi-resolution ICO
    ico_sizes = [(16, 16), (24, 24), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)]
    square_1024.save(icons_dir / "icon.ico", format="ICO", sizes=ico_sizes)

    # macOS ICNS
    save_icns(square_1024, icons_dir / "icon.icns")

    print("Generated icons in:", icons_dir)
    for name in ("icon.png", "icon.ico", "icon.icns"):
        p = icons_dir / name
        print(f"  - {p.name}: {p.stat().st_size} bytes")


if __name__ == "__main__":
    main()
