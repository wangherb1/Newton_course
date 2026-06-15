# Decision: Use Wikisource 1729 As The Primary English Text Source

Date: 2026-05-31

## Decision

Use the Wikisource 1729 Andrew Motte edition as the primary source for routine English text extraction:

`https://en.wikisource.org/wiki/The_Mathematical_Principles_of_Natural_Philosophy_(1729)`

Use Wikisource 1846 and Project Gutenberg 1846 only as backup and comparison sources. Retain `sources/external/motte_1729/` as the historical scan verification archive.

## Reason

Wikisource 1729 already exposes section-level pages that are more efficient and maintainable for proposition-level extraction than a local OCR-first workflow. The organized Internet Archive scan archive remains necessary for manual verification, page references, difficult readings, and images.

## Consequence

All later English nodes should be fetched, cached, extracted, and validated through `sources/external/principia_english/`. Before public release, each quotation still needs a recorded comparison against the matching 1729 scan page.
