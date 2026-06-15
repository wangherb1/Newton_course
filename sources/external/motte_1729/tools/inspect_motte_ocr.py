"""Inspect Motte 1729 OCR assets without modifying source text."""

from __future__ import annotations

from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "logs" / "ocr_inspection_report.md"
REQUIRED = [
    "ocr/vol_1/djvu.txt",
    "ocr/vol_1/djvu.xml",
    "ocr/vol_1/hocr.html",
    "page_maps/vol_1/page_numbers.json",
    "page_maps/vol_1/scandata.xml",
    "ocr/vol_2/djvu.txt",
    "ocr/vol_2/djvu.xml",
    "ocr/vol_2/hocr.html",
    "page_maps/vol_2/page_numbers.json",
    "page_maps/vol_2/scandata.xml",
]
OCR_TEXTS = [
    "ocr/vol_1/djvu.txt",
    "ocr/vol_2/djvu.txt",
]
KEYWORDS = [
    "PROPOSITION I",
    "THEOREM I",
    "centripetal",
    "equal areas",
]


def inspect_text(path: Path) -> dict[str, int]:
    text = path.read_text(encoding="utf-8", errors="replace")
    return {
        "characters": len(text),
        "lines": len(text.splitlines()),
        "size_bytes": path.stat().st_size,
    }


def main() -> int:
    lines = [
        "# Motte 1729 OCR Inspection Report",
        "",
        f"Generated: {datetime.now().astimezone().isoformat(timespec='seconds')}",
        "",
        "## Required Files",
        "",
        "| Path | Exists | Size bytes |",
        "|---|---|---:|",
    ]
    missing = []
    for relative in REQUIRED:
        path = ROOT / relative
        exists = path.is_file()
        if not exists:
            missing.append(relative)
        lines.append(f"| `{relative}` | {'yes' if exists else 'no'} | {path.stat().st_size if exists else ''} |")

    lines.extend(
        [
            "",
            "## OCR Text Statistics",
            "",
            "| Path | Characters | Lines | Size bytes |",
            "|---|---:|---:|---:|",
        ]
    )
    for relative in OCR_TEXTS:
        path = ROOT / relative
        if path.is_file():
            stats = inspect_text(path)
            lines.append(
                f"| `{relative}` | {stats['characters']} | {stats['lines']} | {stats['size_bytes']} |"
            )
        else:
            lines.append(f"| `{relative}` | missing | missing | missing |")

    vol1_text_path = ROOT / "ocr/vol_1/djvu.txt"
    lines.extend(["", "## Volume 1 Keyword Check", "", "| Keyword | Hits |", "|---|---:|"])
    if vol1_text_path.is_file():
        text = vol1_text_path.read_text(encoding="utf-8", errors="replace").lower()
        for keyword in KEYWORDS:
            lines.append(f"| `{keyword}` | {text.count(keyword.lower())} |")
    else:
        for keyword in KEYWORDS:
            lines.append(f"| `{keyword}` | unavailable |")

    lines.extend(
        [
            "",
            "## Notes",
            "",
            "- This report is a lightweight availability check only.",
            "- OCR text was not modified.",
            "- Final quotations must be checked against manually reviewed page maps and the matching Internet Archive scans under `vol_*/pdf/`.",
            "- PDFs under `vol_*/raw_pdf/` are supplementary reprint references only.",
            "",
            f"Missing required files: {len(missing)}",
        ]
    )
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"WROTE {REPORT}")
    print(f"Missing required files: {len(missing)}")
    return 0 if not missing else 1


if __name__ == "__main__":
    raise SystemExit(main())
