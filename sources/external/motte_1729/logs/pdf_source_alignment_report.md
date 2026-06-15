# PDF Source Alignment Report

Generated: 2026-05-31T14:30:30+08:00

## Conclusion

Use `vol_*/pdf/motte_1729_vol*.pdf` as the canonical scan source for page mapping, OCR alignment, quotation verification, and English node extraction.

Treat `vol_*/raw_pdf/` as supplementary modern reprint references only. Do not use them as the default 1729 scan source.

## Evidence

| Volume | IA PDF pages | User PDF pages | page_numbers | scandata | DJVU objects | HOCR index | IA image dimensions matching scandata |
|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | 414 | 408 | 414 | 414 | 414 | 414 | 414/414 |
| 2 | 543 | 267 | 543 | 543 | 543 | 543 | 543/543 |

## Manual Visual Review

- The user-provided Vol.1 cover identifies a Higher Education Press 2016 edition.
- The cover states that the translations were revised and supplied with a historical and explanatory appendix by Florian Cajori.
- The user-provided PDFs are re-typeset editions, not page-for-page scans of the Internet Archive 1729 source.

## Operational Rule

1. Search and initial extraction: use existing IA OCR under `ocr/vol_*/`.
2. Page mapping and quotation verification: use the matching IA PDFs under `vol_*/pdf/`.
3. Supplementary reading only: use the user-provided reprint PDFs under `vol_*/raw_pdf/`.
4. Do not mix reprint pagination or Cajori revisions into the 1729 node source.
