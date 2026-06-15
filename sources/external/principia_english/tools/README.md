# Principia English Source Tools

- `fetch_wikisource.py`: fetches and caches rendered HTML, MediaWiki wikitext, and cleaned section text.
- `extract_wikisource_node.py`: extracts a heading-bounded node from cached cleaned text and writes provenance metadata. Metadata fields can be overridden for later books, sections, and node types.
- `validate_extracted_node.py`: checks required markers and writes a validation report.

The scripts use Python's standard library only. Cached files are reused unless `--force` is passed to the fetcher.
