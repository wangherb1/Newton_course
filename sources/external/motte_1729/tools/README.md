# Motte 1729 Tools

## Organize Internet Archive resources

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File .\sources\external\motte_1729\tools\organize_motte_1729.ps1
```

The organizer copies ordinary files, creates hard links for archives over 500MB when possible, records pointers when hard links fail, and regenerates manifests safely on repeated runs.

## Inspect OCR availability

```powershell
python .\sources\external\motte_1729\tools\inspect_motte_ocr.py
```

The inspector reports file availability, OCR text statistics, and keyword hits without editing OCR text.

## Assess PDF alignment

```powershell
python .\sources\external\motte_1729\tools\assess_pdf_alignment.py
```

The assessor compares PDF page counts with Internet Archive OCR metadata and checks each IA PDF page image against scandata dimensions.
