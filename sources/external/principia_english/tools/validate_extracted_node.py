#!/usr/bin/env python3
"""Validate the sample extracted Wikisource node and write a QA report."""

from __future__ import annotations

import argparse
from datetime import datetime
from pathlib import Path


REQUIRED_MARKERS = [
    "PROPOSITION I. THEOREM I.",
    "Cor. 1.",
    "Cor. 2.",
    "Cor. 3.",
    "Cor. 4.",
    "Cor. 5.",
    "Cor. 6.",
]
FORBIDDEN_MARKERS = ["PROPOSITION II. THEOREM II.", "Proposition II. Theorem II."]


def timestamp() -> str:
    return datetime.now().astimezone().isoformat(timespec="seconds")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-dir", required=True, type=Path)
    parser.add_argument("--node-id", required=True)
    args = parser.parse_args()

    source_dir = args.source_dir.resolve()
    clean_path = source_dir / "extracted_nodes" / f"{args.node_id}_en_clean.md"
    report_path = source_dir / "logs" / "validation_report.md"
    report_path.parent.mkdir(parents=True, exist_ok=True)

    lines = [
        "# Wikisource Extracted Node Validation Report",
        "",
        f"Generated: {timestamp()}",
        "",
        f"Node: `{args.node_id}`",
        "",
    ]
    if not clean_path.exists():
        lines.extend(["## Result", "", "FAIL: clean node file does not exist.", ""])
        report_path.write_text("\n".join(lines), encoding="utf-8")
        print(f"Validation failed: missing {clean_path}")
        return 1

    text = clean_path.read_text(encoding="utf-8")
    missing = [marker for marker in REQUIRED_MARKERS if marker not in text]
    forbidden = [marker for marker in FORBIDDEN_MARKERS if marker in text]
    status = "PASS" if not missing and not forbidden else "FAIL"

    lines.extend(
        [
            "## Result",
            "",
            status,
            "",
            "## Required Markers",
            "",
            "| Marker | Present |",
            "|---|---|",
        ]
    )
    for marker in REQUIRED_MARKERS:
        lines.append(f"| `{marker}` | {'yes' if marker in text else 'no'} |")
    lines.extend(["", "## Forbidden Boundary Markers", "", "| Marker | Absent |", "|---|---|"])
    for marker in FORBIDDEN_MARKERS:
        lines.append(f"| `{marker}` | {'yes' if marker not in text else 'no'} |")

    lines.extend(["", "## Manual Review", ""])
    if missing:
        lines.append(f"- Missing markers require inspection: {', '.join(missing)}")
    else:
        lines.append("- All required proposition and corollary markers are present.")
    if forbidden:
        lines.append("- The extraction crossed into Proposition II. Adjust the end boundary.")
    else:
        lines.append("- Proposition II is excluded from the clean node.")
    lines.append("- Manual comparison with the matching Internet Archive 1729 scan is still required before public release.")
    lines.append("")
    report_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"Validation report: {report_path}")
    print(f"Result: {status}")
    return 0 if status == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
