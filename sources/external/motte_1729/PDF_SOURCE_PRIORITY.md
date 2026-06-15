# PDF Source Priority

## Required Rule

For page mapping, OCR alignment, quotation verification, English node extraction, page-image inspection, and fallback OCR work, use the Internet Archive PDFs under `pdf/` as the canonical scan source:

- Vol.1: `vol_1/pdf/motte_1729_vol1.pdf`
- Vol.2: `vol_2/pdf/motte_1729_vol2.pdf`

These PDFs align page-for-page with the Internet Archive OCR, HOCR, page-number JSON, and scandata XML.

The user-provided PDFs under `raw_pdf/` are re-typeset reference editions, not page-for-page 1729 scans. The Vol.1 cover identifies a Higher Education Press 2016 edition and states that the translations were revised and supplied with a historical and explanatory appendix by Florian Cajori. Keep these files as supplementary reading references only.

## Priority Order

1. Prefer existing OCR text for text search and initial extraction: `ocr/vol_*/djvu.txt`, `djvu.xml`, and `hocr.html`.
2. Verify quotations, printed page numbers, ambiguous OCR, and page images against `vol_*/pdf/motte_1729_vol*.pdf`.
3. Use `vol_*/raw_pdf/` only as supplementary modern reprint references.
4. Do not mix reprint pagination or Cajori revisions into the 1729 node source.
5. Do not run fresh OCR against either PDF unless existing OCR is insufficient and the need is explicitly recorded.

## Notes

- Both PDF sets remain excluded from ordinary Git commits.
- Do not move, rename, overwrite, or delete either PDF set.
- Alignment evidence is recorded in `logs/pdf_source_alignment_report.md`.
