# Wikisource 1846 Primary Digital Source

This is the primary digital transcription for routine English extraction and source-page illustration lookup.

## Attribution Boundary

The quoted English translation remains Andrew Motte's translation first published in 1729. `1846` identifies the Wikisource digital page layout selected for extraction because it preserves readable initials and integrated figure placement.

## Current Cache

- `Book I / Section II`: `cleaned_text/book_i_section_ii_clean.txt`
- Cached rendered HTML: `raw_html/book_i_section_ii.html`
- Cached MediaWiki wikitext: `raw_wikitext/book_i_section_ii.wikitext`

## Current Extracted Nodes

- `book1_section2_prop01_theorem01`: auto extracted and automatically validated; manual scan comparison is still pending.

## Segmentation Rule

Fetch the relevant 1846 Wikisource page, then extract each proposition, theorem, lemma, or corollary from its heading up to the next major heading. When the source page contains an original illustration, cache the Wikimedia image under `assets/images/primary_sources/` and preserve its approximate source-page position in the English module.
