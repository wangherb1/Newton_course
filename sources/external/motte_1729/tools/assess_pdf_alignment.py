"""Assess which Motte PDF set aligns directly with Internet Archive OCR metadata."""

from __future__ import annotations

import gzip
import json
from datetime import datetime
from pathlib import Path
from xml.etree import ElementTree as ET

import fitz


ROOT = Path(__file__).resolve().parents[1]
REPORT_MD = ROOT / "logs" / "pdf_source_alignment_report.md"
REPORT_JSON = ROOT / "logs" / "pdf_source_alignment_report.json"


def assess_volume(volume: int) -> dict[str, object]:
    key = f"vol_{volume}"
    ia_pdf = ROOT / key / "pdf" / f"motte_1729_vol{volume}.pdf"
    user_pdf = next((ROOT / key / "raw_pdf").glob("*.pdf"))
    page_numbers = json.loads(
        (ROOT / "page_maps" / key / "page_numbers.json").read_text(encoding="utf-8")
    )["pages"]
    scandata_pages = ET.parse(ROOT / "page_maps" / key / "scandata.xml").getroot().findall(
        ".//pageData/page"
    )
    djvu_objects = ET.parse(ROOT / "ocr" / key / "djvu.xml").getroot().findall(".//OBJECT")
    with gzip.open(ROOT / "ocr" / key / "hocr_pageindex.json.gz", "rt", encoding="utf-8") as handle:
        hocr_pageindex = json.load(handle)

    with fitz.open(ia_pdf) as ia_doc, fitz.open(user_pdf) as user_doc:
        matching_image_dimensions = 0
        mismatched_image_dimensions = []
        for index, (page, scan_page) in enumerate(zip(ia_doc, scandata_pages)):
            images = page.get_images(full=True)
            if not images:
                mismatched_image_dimensions.append({"page_index": index, "reason": "no_embedded_image"})
                continue
            actual = [images[0][2], images[0][3]]
            expected = [int(scan_page.findtext("origWidth")), int(scan_page.findtext("origHeight"))]
            if actual == expected:
                matching_image_dimensions += 1
            else:
                mismatched_image_dimensions.append(
                    {"page_index": index, "actual": actual, "expected": expected}
                )

        counts = {
            "ia_pdf_pages": len(ia_doc),
            "user_provided_pdf_pages": len(user_doc),
            "page_numbers_entries": len(page_numbers),
            "scandata_pages": len(scandata_pages),
            "djvu_objects": len(djvu_objects),
            "hocr_pageindex_entries": len(hocr_pageindex),
        }

    direct_alignment = len(set(
        [
            counts["ia_pdf_pages"],
            counts["page_numbers_entries"],
            counts["scandata_pages"],
            counts["djvu_objects"],
            counts["hocr_pageindex_entries"],
        ]
    )) == 1 and matching_image_dimensions == counts["scandata_pages"]

    return {
        "volume": volume,
        "internet_archive_pdf": ia_pdf.relative_to(ROOT).as_posix(),
        "user_provided_pdf": user_pdf.relative_to(ROOT).as_posix(),
        "counts": counts,
        "ia_pdf_scandata_image_dimension_matches": matching_image_dimensions,
        "ia_pdf_scandata_image_dimension_mismatches": mismatched_image_dimensions,
        "internet_archive_direct_alignment": direct_alignment,
    }


def write_reports(volumes: list[dict[str, object]]) -> None:
    payload = {
        "generated_at": datetime.now().astimezone().isoformat(timespec="seconds"),
        "conclusion": (
            "Use vol_*/pdf/motte_1729_vol*.pdf as the canonical scan source for page mapping, "
            "OCR alignment, quotation verification, and English node extraction. Treat vol_*/raw_pdf/ "
            "as supplementary modern reprint references only."
        ),
        "manual_visual_review": [
            "The user-provided Vol.1 cover identifies a Higher Education Press 2016 edition.",
            "The cover states that the translations were revised and supplied with a historical and explanatory appendix by Florian Cajori.",
            "The user-provided PDFs are re-typeset editions, not page-for-page scans of the Internet Archive 1729 source.",
        ],
        "volumes": volumes,
    }
    REPORT_JSON.parent.mkdir(parents=True, exist_ok=True)
    REPORT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    lines = [
        "# PDF Source Alignment Report",
        "",
        f"Generated: {payload['generated_at']}",
        "",
        "## Conclusion",
        "",
        "Use `vol_*/pdf/motte_1729_vol*.pdf` as the canonical scan source for page mapping, OCR alignment, quotation verification, and English node extraction.",
        "",
        "Treat `vol_*/raw_pdf/` as supplementary modern reprint references only. Do not use them as the default 1729 scan source.",
        "",
        "## Evidence",
        "",
        "| Volume | IA PDF pages | User PDF pages | page_numbers | scandata | DJVU objects | HOCR index | IA image dimensions matching scandata |",
        "|---|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for volume in volumes:
        counts = volume["counts"]
        lines.append(
            f"| {volume['volume']} | {counts['ia_pdf_pages']} | {counts['user_provided_pdf_pages']} | "
            f"{counts['page_numbers_entries']} | {counts['scandata_pages']} | {counts['djvu_objects']} | "
            f"{counts['hocr_pageindex_entries']} | {volume['ia_pdf_scandata_image_dimension_matches']}/{counts['scandata_pages']} |"
        )
    lines.extend(
        [
            "",
            "## Manual Visual Review",
            "",
            "- The user-provided Vol.1 cover identifies a Higher Education Press 2016 edition.",
            "- The cover states that the translations were revised and supplied with a historical and explanatory appendix by Florian Cajori.",
            "- The user-provided PDFs are re-typeset editions, not page-for-page scans of the Internet Archive 1729 source.",
            "",
            "## Operational Rule",
            "",
            "1. Search and initial extraction: use existing IA OCR under `ocr/vol_*/`.",
            "2. Page mapping and quotation verification: use the matching IA PDFs under `vol_*/pdf/`.",
            "3. Supplementary reading only: use the user-provided reprint PDFs under `vol_*/raw_pdf/`.",
            "4. Do not mix reprint pagination or Cajori revisions into the 1729 node source.",
            "",
        ]
    )
    REPORT_MD.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    volumes = [assess_volume(1), assess_volume(2)]
    write_reports(volumes)
    print(f"WROTE {REPORT_MD}")
    print(f"WROTE {REPORT_JSON}")
    for volume in volumes:
        counts = volume["counts"]
        print(
            f"VOL{volume['volume']} IA={counts['ia_pdf_pages']} USER={counts['user_provided_pdf_pages']} "
            f"SCANDATA={counts['scandata_pages']} DIM_MATCH={volume['ia_pdf_scandata_image_dimension_matches']}/"
            f"{counts['scandata_pages']}"
        )
    return 0 if all(volume["internet_archive_direct_alignment"] for volume in volumes) else 1


if __name__ == "__main__":
    raise SystemExit(main())
