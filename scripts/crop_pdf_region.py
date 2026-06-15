"""Render one PDF rectangle as a PNG for source-figure extraction."""

from __future__ import annotations

import argparse
from pathlib import Path

import fitz


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pdf", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--page", required=True, type=int, help="1-based PDF page number")
    parser.add_argument("--x0", required=True, type=float)
    parser.add_argument("--y0", required=True, type=float)
    parser.add_argument("--x1", required=True, type=float)
    parser.add_argument("--y1", required=True, type=float)
    parser.add_argument("--scale", type=float, default=4.0)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    output = args.output.resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    clip = fitz.Rect(args.x0, args.y0, args.x1, args.y1)
    with fitz.open(args.pdf.resolve()) as document:
        if args.page < 1 or args.page > document.page_count:
            raise SystemExit(f"Page {args.page} is outside PDF range 1-{document.page_count}.")
        page = document[args.page - 1]
        if not page.rect.contains(clip):
            raise SystemExit(f"Crop rectangle {clip} exceeds page bounds {page.rect}.")
        pixmap = page.get_pixmap(matrix=fitz.Matrix(args.scale, args.scale), clip=clip, alpha=False)
        pixmap.save(output)
    print(f"CROPPED {args.pdf} page {args.page} {clip} -> {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
