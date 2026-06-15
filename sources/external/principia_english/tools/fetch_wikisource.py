#!/usr/bin/env python3
"""Fetch and cache a Wikisource page for repeatable source extraction."""

from __future__ import annotations

import argparse
import html
import json
import re
import sys
import time
from datetime import datetime
from html.parser import HTMLParser
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import unquote, urlencode, urlparse
from urllib.request import Request, urlopen


USER_AGENT = "NewtonCourseSourceWorkflow/0.1 (educational source preparation)"
API_URL = "https://en.wikisource.org/w/api.php"
BLOCK_TAGS = {
    "address", "blockquote", "br", "dd", "div", "dl", "dt", "figcaption",
    "figure", "h1", "h2", "h3", "h4", "h5", "h6", "hr", "li", "ol", "p",
    "pre", "table", "td", "th", "tr", "ul",
}
VOID_TAGS = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "param", "source", "track", "wbr"}


def timestamp() -> str:
    return datetime.now().astimezone().isoformat(timespec="seconds")


class WikisourceTextParser(HTMLParser):
    """Collect visible text from the rendered Wikisource content container."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.capture_depth = 0
        self.skip_depth = 0
        self.parts: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attributes = dict(attrs)
        classes = (attributes.get("class") or "").split()
        if self.capture_depth == 0 and tag == "div" and "mw-parser-output" in classes:
            self.capture_depth = 1
            return
        if self.capture_depth == 0:
            return
        if tag not in VOID_TAGS:
            self.capture_depth += 1
        if tag in {"script", "style", "noscript"}:
            self.skip_depth += 1
        if self.skip_depth == 0 and tag in BLOCK_TAGS:
            self.parts.append("\n")

    def handle_startendtag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if self.capture_depth and self.skip_depth == 0 and tag in BLOCK_TAGS:
            self.parts.append("\n")

    def handle_endtag(self, tag: str) -> None:
        if self.capture_depth == 0:
            return
        if tag in {"script", "style", "noscript"} and self.skip_depth:
            self.skip_depth -= 1
        if self.skip_depth == 0 and tag in BLOCK_TAGS:
            self.parts.append("\n")
        if tag not in VOID_TAGS:
            self.capture_depth -= 1

    def handle_data(self, data: str) -> None:
        if self.capture_depth and self.skip_depth == 0:
            self.parts.append(data)

    def text(self) -> str:
        value = html.unescape("".join(self.parts))
        value = value.replace("\u200b", "").replace("\ufeff", "")
        value = re.sub(r"[ \t]+\n", "\n", value)
        value = re.sub(r"\n[ \t]+", "\n", value)
        value = re.sub(r"[ \t]{2,}", " ", value)
        value = re.sub(r"\n{3,}", "\n\n", value)
        blocks = []
        for block in value.split("\n\n"):
            compact = re.sub(r"\s*\n\s*", " ", block).strip()
            if compact:
                blocks.append(compact)
        return "\n\n".join(blocks) + "\n"


def derive_page_title(url: str) -> str:
    parsed = urlparse(url)
    marker = "/wiki/"
    if marker not in parsed.path:
        raise ValueError("Cannot derive page title: URL does not contain /wiki/.")
    return unquote(parsed.path.split(marker, 1)[1])


def fetch_text(url: str, timeout: int = 30) -> str:
    request = Request(url, headers={"User-Agent": USER_AGENT})
    with urlopen(request, timeout=timeout) as response:
        charset = response.headers.get_content_charset() or "utf-8"
        return response.read().decode(charset, errors="replace")


def fetch_wikitext(page_title: str, timeout: int = 30) -> str:
    query = urlencode(
        {
            "action": "parse",
            "page": page_title,
            "prop": "wikitext",
            "format": "json",
            "formatversion": "2",
        }
    )
    payload = json.loads(fetch_text(f"{API_URL}?{query}", timeout=timeout))
    return payload["parse"]["wikitext"]


def append_log(path: Path, lines: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as handle:
        if path.stat().st_size == 0:
            handle.write("# Wikisource Fetch Log\n\n")
        handle.write("\n".join(lines) + "\n\n")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", required=True)
    parser.add_argument("--page-title")
    parser.add_argument("--out-dir", required=True, type=Path)
    parser.add_argument("--slug", required=True)
    parser.add_argument("--sleep", type=float, default=1.0)
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()

    out_dir = args.out_dir.resolve()
    html_path = out_dir / "raw_html" / f"{args.slug}.html"
    wikitext_path = out_dir / "raw_wikitext" / f"{args.slug}.wikitext"
    clean_path = out_dir / "cleaned_text" / f"{args.slug}_clean.txt"
    log_path = out_dir / "logs" / "fetch_log.md"
    for path in (html_path, wikitext_path, clean_path, log_path):
        path.parent.mkdir(parents=True, exist_ok=True)

    fetched_at = timestamp()
    try:
        if html_path.exists() and not args.force:
            rendered_html = html_path.read_text(encoding="utf-8")
            html_action = "reused cached HTML"
        else:
            if args.sleep > 0:
                time.sleep(args.sleep)
            rendered_html = fetch_text(args.url)
            html_path.write_text(rendered_html, encoding="utf-8")
            html_action = "downloaded HTML"

        page_title = args.page_title or derive_page_title(args.url)
        if wikitext_path.exists() and not args.force:
            wikitext_action = "reused cached wikitext"
        else:
            if args.sleep > 0:
                time.sleep(args.sleep)
            wikitext_path.write_text(fetch_wikitext(page_title), encoding="utf-8")
            wikitext_action = "downloaded wikitext"

        text_parser = WikisourceTextParser()
        text_parser.feed(rendered_html)
        cleaned_text = text_parser.text()
        if not cleaned_text.strip():
            raise ValueError("Rendered page did not contain a mw-parser-output text block.")
        clean_path.write_text(cleaned_text, encoding="utf-8")
        append_log(
            log_path,
            [
                f"## {fetched_at}",
                f"- URL: {args.url}",
                f"- Page title: `{page_title}`",
                f"- Slug: `{args.slug}`",
                f"- HTML: {html_action}",
                f"- Wikitext: {wikitext_action}",
                f"- Clean text: regenerated from cached rendered HTML ({len(cleaned_text)} characters)",
            ],
        )
    except (HTTPError, URLError, TimeoutError, ValueError, KeyError, json.JSONDecodeError) as error:
        append_log(
            log_path,
            [
                f"## {fetched_at}",
                f"- URL: {args.url}",
                f"- Slug: `{args.slug}`",
                f"- Status: failed",
                f"- Error: `{type(error).__name__}: {error}`",
            ],
        )
        print(f"Fetch failed: {error}", file=sys.stderr)
        return 1

    print(f"Cached HTML: {html_path}")
    print(f"Cached wikitext: {wikitext_path}")
    print(f"Cleaned text: {clean_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
