"""Scan content node MDX files and emit a small completion-status report."""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from datetime import datetime
from pathlib import Path


FRONTMATTER = re.compile(r"\A---\s*\n(?P<body>.*?)\n---\s*\n", re.DOTALL)
SCALAR = re.compile(r"^(?P<key>[a-zA-Z0-9_]+):\s*(?P<value>.*)$")


def parse_frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    match = FRONTMATTER.match(text)
    if not match:
        return {}
    values: dict[str, str] = {}
    for line in match.group("body").splitlines():
        if line.startswith((" ", "\t")):
            continue
        scalar = SCALAR.match(line)
        if scalar:
            values[scalar.group("key")] = scalar.group("value").strip().strip("\"'")
    return values


def parse_args() -> argparse.Namespace:
    project_root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--nodes-dir", type=Path, default=project_root / "content" / "nodes")
    parser.add_argument("--output-dir", type=Path, default=project_root / "exports" / "status")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    nodes_dir = args.nodes_dir.resolve()
    output_dir = args.output_dir.resolve()
    files = sorted(path for path in nodes_dir.rglob("*.mdx") if path.name != "_template.mdx")
    nodes = []
    for path in files:
        metadata = parse_frontmatter(path)
        nodes.append(
            {
                "file": path.relative_to(nodes_dir.parents[1]).as_posix(),
                "id": metadata.get("id"),
                "display_id": metadata.get("display_id"),
                "title_cn": metadata.get("title_cn"),
                "status": metadata.get("status", "missing_frontmatter"),
                "last_updated": metadata.get("last_updated"),
            }
        )

    status_counts = Counter(node["status"] for node in nodes)
    report = {
        "generated_at": datetime.now().astimezone().isoformat(timespec="seconds"),
        "node_count": len(nodes),
        "status_counts": dict(sorted(status_counts.items())),
        "nodes": nodes,
    }
    output_dir.mkdir(parents=True, exist_ok=True)
    json_target = output_dir / "content_status.json"
    md_target = output_dir / "content_status.md"
    json_target.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    table = [
        "# Content Status",
        "",
        f"Generated: {report['generated_at']}",
        "",
        f"Total nodes: {len(nodes)}",
        "",
        "| ID | Display ID | Status | File |",
        "|---|---|---|---|",
    ]
    table.extend(
        f"| {node['id'] or ''} | {node['display_id'] or ''} | {node['status']} | `{node['file']}` |"
        for node in nodes
    )
    md_target.write_text("\n".join(table) + "\n", encoding="utf-8")
    print(f"WROTE {json_target} and {md_target} for {len(nodes)} nodes")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
