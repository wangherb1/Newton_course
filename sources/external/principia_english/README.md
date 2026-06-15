# Principia English Source Workflow

This directory is the canonical workflow for English source text used by the Newton course project.

## Source Priority

1. Primary digital transcription: Wikisource 1846 page layout of the Motte translation.
2. Reference: Wikisource 1729 transcription.
3. Backup: Project Gutenberg 1846 electronic text.
4. Historical verification only: the local Internet Archive 1729 scans under `../motte_1729/`.

The local scans remain important for manual verification, printed page references, and image checks. They are no longer the routine extraction source.

## Sample Workflow

Fetch and cache Book I, Section II:

```powershell
python .\tools\fetch_wikisource.py `
  --url "https://en.wikisource.org/wiki/The_Mathematical_Principles_of_Natural_Philosophy_(1846)/BookI-II" `
  --page-title "The_Mathematical_Principles_of_Natural_Philosophy_(1846)/BookI-II" `
  --out-dir .\wikisource_1846_primary `
  --slug book_i_section_ii
```

Extract Proposition I, Theorem I:

```powershell
python .\tools\extract_wikisource_node.py `
  --source-dir .\wikisource_1846_primary `
  --source-slug book_i_section_ii `
  --node-id book1_section2_prop01_theorem01 `
  --start-title "PROPOSITION I. THEOREM I." `
  --end-title "PROPOSITION II. THEOREM II."
```

Validate the extracted node:

```powershell
python .\tools\validate_extracted_node.py `
  --source-dir .\wikisource_1846_primary `
  --node-id book1_section2_prop01_theorem01
```

## Extending The Workflow

For later propositions, lemmas, or corollaries:

1. Fetch the relevant Wikisource 1846 page into the local cache.
2. Run the generic extractor with the new node ID, start/end titles, source URL, metadata overrides, and scan-page overrides. Use `--help` for the full parameter list.
3. Check the generated metadata and validation report.
4. Download corresponding source-page illustrations when present, cache them under `assets/images/primary_sources/`, and preserve their placement in the English module.
5. Compare the final quotation with the corresponding `../motte_1729/` scan before public release.

See `source_strategy.md`, `urls.json`, and `manifest.json` for the fixed source policy and current cache state.
