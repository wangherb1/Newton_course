"""Build a conservative, review-required outline seed from 原理概要.docx."""

from __future__ import annotations

import argparse
import json
import re
from datetime import datetime
from pathlib import Path

from extract_docx_text import extract_docx_lines


HEADING_PATTERN = re.compile(
    r"^(第[一二三四五六七八九十百零0-9]+[卷编章节部]|"
    r"第[一二三]定律|"
    r"定义|公理|定律|运动定律|引理|命题|问题|定理|推论|附注|附录|"
    r"BOOK\b|SECTION\b|DEFINITION\b|LAW\b|LEMMA\b|PROPOSITION\b|COROLLARY\b)",
    re.IGNORECASE,
)


def parse_args() -> argparse.Namespace:
    project_root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--source",
        type=Path,
        default=project_root / "sources" / "raw" / "liao_teacher" / "outline" / "原理概要.docx",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=project_root / "content" / "metadata" / "principia_outline.seed.json",
    )
    return parser.parse_args()


def classify(text: str) -> str:
    match = HEADING_PATTERN.match(text)
    return match.group(1) if match else "unclassified"


def main() -> int:
    args = parse_args()
    source = args.source.resolve()
    output = args.output.resolve()
    if not source.is_file():
        raise SystemExit(f"Outline source not found: {source}")

    lines = extract_docx_lines(source)
    candidates = [
        {
            "source_line": number,
            "candidate_type": classify(text),
            "text": text,
            "review_status": "pending_manual_review",
        }
        for number, text in enumerate(lines, start=1)
        if HEADING_PATTERN.match(text)
    ]
    payload = {
        "generated_at": datetime.now().astimezone().isoformat(timespec="seconds"),
        "source_file": "sources/raw/liao_teacher/outline/原理概要.docx",
        "extraction_mode": "conservative_heading_candidates",
        "needs_manual_review": True,
        "source_paragraph_count": len(lines),
        "candidate_count": len(candidates),
        "confirmed_nodes": [
            {
                "id": "principia-book1-chapter02-prop001-theorem001",
                "source_line": next(
                    (
                        candidate["source_line"]
                        for candidate in candidates
                        if candidate["text"].startswith("命题1 定理1")
                    ),
                    None,
                ),
                "node_type": "proposition_theorem",
                "text": "命题1 定理1：仅受向心力作用的物体与固定力心的连线扫面积速度恒定。",
                "review_status": "sample_page_created_pending_manual_review",
            }
        ],
        "items": candidates,
    }
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"WROTE {output} with {len(candidates)} review-required candidates from {len(lines)} paragraphs")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
