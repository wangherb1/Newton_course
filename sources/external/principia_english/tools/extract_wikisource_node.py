#!/usr/bin/env python3
"""Extract one heading-bounded Wikisource node and record provenance metadata."""

from __future__ import annotations

import argparse
import json
import re
from datetime import datetime
from pathlib import Path


DEFAULT_URL = "https://en.wikisource.org/wiki/The_Mathematical_Principles_of_Natural_Philosophy_(1846)/BookI-II"


def timestamp() -> str:
    return datetime.now().astimezone().isoformat(timespec="seconds")


def heading_pattern(title: str) -> re.Pattern[str]:
    words = [re.escape(word) for word in title.strip().split()]
    return re.compile(r"(?im)^[ \t]*" + r"[ \t]+".join(words) + r"[ \t]*$")


def extract_between(text: str, start_title: str, end_title: str) -> tuple[str, str]:
    start = heading_pattern(start_title).search(text)
    if not start:
        raise ValueError(f"Start heading not found: {start_title}")
    end = heading_pattern(end_title).search(text, start.end())
    if not end:
        raise ValueError(f"End heading not found after start heading: {end_title}")
    raw = text[start.start():end.start()].strip()
    body = text[start.end():end.start()].strip()
    clean = f"# {start_title.upper()}\n\n{body}\n"
    return raw + "\n", clean


def append_log(path: Path, lines: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as handle:
        if path.stat().st_size == 0:
            handle.write("# Wikisource Extraction Log\n\n")
        handle.write("\n".join(lines) + "\n\n")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-dir", required=True, type=Path)
    parser.add_argument("--source-slug", required=True)
    parser.add_argument("--node-id", required=True)
    parser.add_argument("--start-title", required=True)
    parser.add_argument("--end-title", required=True)
    parser.add_argument("--source-url", default=DEFAULT_URL)
    parser.add_argument("--book", default="Book I")
    parser.add_argument("--section", default="Section II")
    parser.add_argument("--section-title", default="Of the invention of centripetal forces")
    parser.add_argument("--node-type", default="proposition_theorem")
    parser.add_argument("--node-number")
    parser.add_argument("--title-en", default="The areas, which revolving bodies describe by radii drawn to an immovable centre of force do lie in the same immovable planes, and are proportional to the times in which they are described.")
    parser.add_argument("--title-zh", default="仅受向心力作用的物体与固定力心的连线扫面积速度恒定")
    parser.add_argument("--scan-volume", default="vol_1")
    parser.add_argument("--ia-scan-leaf", default="102-103")
    parser.add_argument("--ia-pdf-page", default="103-104")
    parser.add_argument("--printed-page", default="57-58")
    args = parser.parse_args()

    source_dir = args.source_dir.resolve()
    clean_source_path = source_dir / "cleaned_text" / f"{args.source_slug}_clean.txt"
    nodes_dir = source_dir / "extracted_nodes"
    log_path = source_dir / "logs" / "extraction_log.md"
    nodes_dir.mkdir(parents=True, exist_ok=True)
    now = timestamp()

    if not clean_source_path.exists():
        append_log(log_path, [f"## {now}", f"- Node: `{args.node_id}`", "- Status: failed", f"- Missing source: `{clean_source_path}`"])
        raise SystemExit(f"Missing cached clean source: {clean_source_path}")

    text = clean_source_path.read_text(encoding="utf-8")
    try:
        raw_text, clean_text = extract_between(text, args.start_title, args.end_title)
    except ValueError as error:
        append_log(log_path, [f"## {now}", f"- Node: `{args.node_id}`", "- Status: failed", f"- Error: `{error}`"])
        raise SystemExit(str(error))

    raw_path = nodes_dir / f"{args.node_id}_en_raw.md"
    clean_path = nodes_dir / f"{args.node_id}_en_clean.md"
    metadata_path = nodes_dir / f"{args.node_id}_metadata.json"
    raw_path.write_text(raw_text, encoding="utf-8")
    clean_path.write_text(clean_text, encoding="utf-8")

    contains = ["proposition", "proof"]
    contains.extend(f"corollary_{index}" for index in range(1, 100) if f"Cor. {index}." in clean_text)
    metadata = {
        "node_id": args.node_id,
        "work": "The Mathematical Principles of Natural Philosophy",
        "translation": "Andrew Motte English translation, first published 1729",
        "digital_source_edition": "Wikisource 1846 digital transcription",
        "source": "Wikisource",
        "source_priority": "primary",
        "source_url": args.source_url,
        "source_page_slug": args.source_slug,
        "book": args.book,
        "section": args.section,
        "section_title": args.section_title,
        "node_type": args.node_type,
        "node_number": args.node_number or args.start_title.title(),
        "title_en": args.title_en,
        "title_zh": args.title_zh,
        "contains": contains,
        "extraction_rule": f"Extract from heading `{args.start_title}` up to but excluding `{args.end_title}`.",
        "extraction_status": "auto_extracted_pending_manual_review",
        "manual_review_status": "not_reviewed",
        "scan_verification": {
            "project_archive": "E:\\Codex\\Newton_course\\sources\\external\\motte_1729",
            "volume": args.scan_volume,
            "ia_scan_leaf": args.ia_scan_leaf,
            "ia_archive_pdf_page_1_based": args.ia_pdf_page,
            "printed_page": args.printed_page,
            "verification_status": "pending_manual_comparison"
        },
        "created_at": now,
        "updated_at": now,
        "notes": "Extracted from the Wikisource 1846 digital transcription of the Motte translation. Must be manually compared with the matching scan before final public release."
    }
    metadata_path.write_text(json.dumps(metadata, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    append_log(
        log_path,
        [
            f"## {now}",
            f"- Node: `{args.node_id}`",
            f"- Source: {args.source_url}",
            f"- Rule: {metadata['extraction_rule']}",
            "- Status: auto extracted; manual scan comparison pending",
            f"- Raw output: `{raw_path.name}`",
            f"- Clean output: `{clean_path.name}`",
            f"- Metadata: `{metadata_path.name}`",
        ],
    )
    print(f"Raw node: {raw_path}")
    print(f"Clean node: {clean_path}")
    print(f"Metadata: {metadata_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
