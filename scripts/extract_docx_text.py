"""Extract traceable plain-text copies from DOCX files without editing sources."""

from __future__ import annotations

import argparse
import sys
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET


WORD_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
MATH_NS = "http://schemas.openxmlformats.org/officeDocument/2006/math"
NS = {"w": WORD_NS, "m": MATH_NS}
FORMULA_MARKER = "[公式待人工校核：DOCX 中检测到公式对象]"


def extract_docx_lines(docx_path: Path) -> list[str]:
    """Return conservative paragraph-level text with formula markers."""
    with zipfile.ZipFile(docx_path) as archive:
        xml = archive.read("word/document.xml")

    root = ET.fromstring(xml)
    lines: list[str] = []
    for paragraph in root.findall(".//w:p", NS):
        text = "".join(node.text or "" for node in paragraph.findall(".//w:t", NS))
        contains_formula = (
            paragraph.find(".//m:oMath", NS) is not None
            or paragraph.find(".//m:oMathPara", NS) is not None
        )
        if contains_formula:
            text = f"{text} {FORMULA_MARKER}".strip()
        if text:
            lines.append(text)
    return lines


def destination_for(source: Path, source_root: Path, output_root: Path) -> Path:
    relative = source.relative_to(source_root)
    return (output_root / relative).with_suffix(".txt")


def parse_args() -> argparse.Namespace:
    project_root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "inputs",
        nargs="*",
        type=Path,
        help="DOCX files to extract. Defaults to every DOCX under sources/raw/liao_teacher.",
    )
    parser.add_argument(
        "--source-root",
        type=Path,
        default=project_root / "sources" / "raw" / "liao_teacher",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=project_root / "sources" / "processed" / "text_extracts",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    source_root = args.source_root.resolve()
    output_root = args.output_dir.resolve()
    sources = [item.resolve() for item in args.inputs]
    if not sources:
        sources = sorted(source_root.rglob("*.docx"))

    if not sources:
        print(f"No DOCX files found under {source_root}", file=sys.stderr)
        return 1

    completed = 0
    for source in sources:
        if not source.is_file():
            print(f"SKIP missing file: {source}", file=sys.stderr)
            continue
        try:
            lines = extract_docx_lines(source)
            try:
                target = destination_for(source, source_root, output_root)
            except ValueError:
                target = output_root / f"{source.stem}.txt"
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text("\n\n".join(lines) + "\n", encoding="utf-8")
            print(f"EXTRACTED {source} -> {target} ({len(lines)} paragraphs)")
            completed += 1
        except (KeyError, ET.ParseError, zipfile.BadZipFile) as exc:
            print(f"FAILED {source}: {exc}", file=sys.stderr)

    print(f"Completed {completed}/{len(sources)} DOCX extractions.")
    return 0 if completed == len(sources) else 1


if __name__ == "__main__":
    raise SystemExit(main())
