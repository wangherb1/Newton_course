"""Copy canonical website media assets into Astro's public directory."""

from __future__ import annotations

import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ASSET_GROUPS = [
    (ROOT / "assets" / "images" / "heroes", ROOT / "web" / "public" / "assets" / "heroes"),
    (
        ROOT / "assets" / "images" / "primary_sources",
        ROOT / "web" / "public" / "assets" / "primary-sources",
    ),
    (
        ROOT / "assets" / "images" / "teacher_manuscripts",
        ROOT / "web" / "public" / "assets" / "teacher-manuscripts",
    ),
    (ROOT / "assets" / "videos", ROOT / "web" / "public" / "assets" / "videos"),
]


def main() -> None:
    copied = 0
    for source, destination in ASSET_GROUPS:
        if not source.exists():
            continue
        for source_file in source.rglob("*"):
            if not source_file.is_file():
                continue

            relative_path = source_file.relative_to(source)
            destination_file = destination / relative_path
            destination_file.parent.mkdir(parents=True, exist_ok=True)

            if destination_file.exists() and source_file.read_bytes() == destination_file.read_bytes():
                continue

            shutil.copy2(source_file, destination_file)
            copied += 1
            print(f"COPIED {relative_path.as_posix()}")

    print(f"Website media assets synchronized: {copied} file(s) copied.")


if __name__ == "__main__":
    main()
