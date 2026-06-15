# Principia English Source Strategy

## Fixed Priority Order

1. Use the Wikisource 1846 page layout as the primary digital source for routine English text extraction and source-page illustrations.
2. Treat the quoted work as the Andrew Motte English translation first published in 1729. The digital transcription source and the translation attribution are separate metadata.
3. Retain the Wikisource 1729 transcription as a comparison source. Its decorative initial letters and detached illustration layout make it less suitable for routine extraction.
4. Use Project Gutenberg 1846 only as a backup and comparison source.
5. Retain the Internet Archive 1729 scans as historical verification material. They are not the routine extraction workflow.

## Caching And Provenance

1. Cache every fetched page locally before extracting nodes.
2. Record source URL, fetch time, extraction rule, and manual review state for every extracted node.
3. Store all routine English nodes under `wikisource_1846_primary/extracted_nodes/`.
4. Do not paste English source text manually without recording its provenance.
5. When the two Wikisource transcriptions differ, use the 1846 page transcription as the routine working text and record any relevant difference in node metadata.
6. For public pages that quote the historical English text, retain attribution and a public-domain statement.
7. When the source page contains an original illustration, cache the corresponding Wikimedia image under `assets/images/primary_sources/`, preserve its approximate source-page position, and record the page URL.

## Scan Verification

The existing `../motte_1729/` archive remains available for difficult readings, printed page references, images, and scan-page verification. Verification work should record the exact scan page and file name used. Do not copy additional large JP2, PDF, or OCR assets into this directory unless specifically required.
