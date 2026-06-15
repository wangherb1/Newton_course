# Wikisource 1729 Reference Cache

This directory contains the earlier Wikisource 1729 extraction cache. It remains available for provenance and comparison, but routine extraction now uses `../wikisource_1846_primary/`.

## Current Cache

- `Book I / Section II`: `cleaned_text/book_1_section_2_clean.txt`
- Cached rendered HTML: `raw_html/book_1_section_2.html`
- Cached MediaWiki wikitext: `raw_wikitext/book_1_section_2.wikitext`

## Current Extracted Nodes

- `book1_section2_prop01_theorem01`: auto extracted and automatically validated; manual scan comparison is still pending.

## Review State

Every generated node starts as `auto_extracted_pending_manual_review`. Before public release, compare the selected text with the corresponding scan under `../../motte_1729/` and record the scan page used.

## Segmentation Rule

Fetch a complete section page, then extract one proposition, theorem, lemma, or other node from its heading up to the next major heading. Keep the cached HTML, wikitext, cleaned text, node text, metadata, and logs together.
