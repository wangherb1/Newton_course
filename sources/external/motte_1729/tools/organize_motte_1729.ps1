param(
    [string]$SourceVol1 = "E:\Download\bim_eighteenth-century_principia-english-th_newton-sir-isaac_1729_1",
    [string]$SourceVol2 = "E:\Download\bim_eighteenth-century_principia-english-th_newton-sir-isaac_1729_2",
    [string]$TargetRoot = "E:\Codex\Newton_course\sources\external\motte_1729",
    [ValidateSet("Copy")]
    [string]$Mode = "Copy",
    [ValidateSet("HardLinkOrPointer")]
    [string]$LargeFilePolicy = "HardLinkOrPointer"
)

$ErrorActionPreference = "Stop"
$Utf8NoBom = New-Object System.Text.UTF8Encoding($false)
$LargeFileThreshold = 500MB
$Timestamp = Get-Date -Format "yyyyMMdd_HHmmss"
$Records = New-Object System.Collections.Generic.List[object]
$Missing = New-Object System.Collections.Generic.List[string]
$LogLines = New-Object System.Collections.Generic.List[string]

function Write-Utf8 {
    param([string]$Path, [string]$Content)
    $parent = Split-Path -Parent $Path
    if ($parent) {
        New-Item -ItemType Directory -Force -Path $parent | Out-Null
    }
    [System.IO.File]::WriteAllText($Path, $Content, $Utf8NoBom)
}

function Get-RelativeToTarget {
    param([string]$Path)
    $targetUri = New-Object System.Uri(($TargetRoot.TrimEnd("\") + "\"))
    $pathUri = New-Object System.Uri($Path)
    return [System.Uri]::UnescapeDataString($targetUri.MakeRelativeUri($pathUri).ToString()).Replace("/", "\")
}

function Get-Sha256 {
    param([string]$Path)
    return (Get-FileHash -LiteralPath $Path -Algorithm SHA256).Hash.ToLowerInvariant()
}

function Add-Record {
    param(
        [int]$Volume,
        [string]$Category,
        [string]$CanonicalName,
        [string]$CanonicalPath,
        [System.IO.FileInfo]$SourceFile,
        [string]$Sha256,
        [string]$Action,
        [string]$Notes = ""
    )
    $Records.Add([PSCustomObject]@{
        volume = $Volume
        category = $Category
        canonical_name = $CanonicalName
        canonical_path = (Get-RelativeToTarget $CanonicalPath)
        original_name = $SourceFile.Name
        original_path = $SourceFile.FullName
        size_bytes = $SourceFile.Length
        sha256 = $Sha256
        action = $Action
        notes = $Notes
    })
}

function Copy-ManagedFile {
    param(
        [int]$Volume,
        [string]$Category,
        [System.IO.FileInfo]$SourceFile,
        [string]$Destination,
        [bool]$ComputeHash = $true
    )
    New-Item -ItemType Directory -Force -Path (Split-Path -Parent $Destination) | Out-Null
    $sha = if ($ComputeHash) { Get-Sha256 $SourceFile.FullName } else { "" }
    $action = "copied"
    $actualDestination = $Destination
    if (Test-Path -LiteralPath $Destination) {
        $existing = Get-Item -LiteralPath $Destination
        $same = $existing.Length -eq $SourceFile.Length
        if ($same -and $ComputeHash) {
            $same = (Get-Sha256 $Destination) -eq $sha
        }
        if ($same) {
            $action = "skipped_existing"
        }
        else {
            $directory = Split-Path -Parent $Destination
            $name = [System.IO.Path]::GetFileNameWithoutExtension($Destination)
            $extension = [System.IO.Path]::GetExtension($Destination)
            $actualDestination = Join-Path $directory ("{0}_candidate_{1}{2}" -f $name, $Timestamp, $extension)
            Copy-Item -LiteralPath $SourceFile.FullName -Destination $actualDestination
            $action = "copied_candidate"
            $LogLines.Add("- Existing destination differed; wrote candidate: $actualDestination.")
        }
    }
    else {
        Copy-Item -LiteralPath $SourceFile.FullName -Destination $Destination
    }
    Add-Record $Volume $Category ([System.IO.Path]::GetFileName($actualDestination)) $actualDestination $SourceFile $sha $action
}

function Add-LargeAsset {
    param(
        [int]$Volume,
        [System.IO.FileInfo]$SourceFile,
        [string]$VolumeRoot
    )
    $destination = Join-Path $VolumeRoot ("large_assets\jp2\" + $SourceFile.Name)
    New-Item -ItemType Directory -Force -Path (Split-Path -Parent $destination) | Out-Null
    if (Test-Path -LiteralPath $destination) {
        $existing = Get-Item -LiteralPath $destination
        if ($existing.Length -eq $SourceFile.Length) {
            Add-Record $Volume "large_asset" $SourceFile.Name $destination $SourceFile "" "skipped_existing" "Existing large asset has matching size. Hash omitted for archive over 500MB."
            return
        }
    }
    try {
        New-Item -ItemType HardLink -Path $destination -Target $SourceFile.FullName | Out-Null
        Add-Record $Volume "large_asset" $SourceFile.Name $destination $SourceFile "" "hardlinked" "Hash omitted for large asset over 500MB."
        $LogLines.Add("- Created hard link for large asset: $destination.")
    }
    catch {
        $pointerDir = Join-Path $VolumeRoot "large_assets\pointers"
        $pointerName = if ($SourceFile.Name -match "_jp2\.zip$") { "jp2_zip_external_path.txt" } else { $SourceFile.Name + ".external_path.txt" }
        $pointer = Join-Path $pointerDir $pointerName
        $content = @(
            "original_path: $($SourceFile.FullName)"
            "file_name: $($SourceFile.Name)"
            "file_size_bytes: $($SourceFile.Length)"
            "reason: Hard link failed; large file was not copied."
            "suggested_usage: Use the external archive only when page-level high-resolution images are required."
            ""
        ) -join "`n"
        Write-Utf8 $pointer $content
        Add-Record $Volume "large_asset_pointer" $pointerName $pointer $SourceFile "" "pointer" $_.Exception.Message
        $LogLines.Add("- Hard link failed; wrote pointer: $pointer.")
    }
}

function Write-OriginalFileList {
    param([string]$SourceDir, [string]$Output)
    $lines = @("relative_path`tfile_name`textension`tsize_bytes`tlast_write_time")
    $files = Get-ChildItem -LiteralPath $SourceDir -Recurse -File | Sort-Object FullName
    foreach ($file in $files) {
        $relative = $file.FullName.Substring($SourceDir.Length).TrimStart("\")
        $lines += "$relative`t$($file.Name)`t$($file.Extension)`t$($file.Length)`t$($file.LastWriteTime.ToString("s"))"
    }
    Write-Utf8 $Output (($lines -join "`n") + "`n")
}

function Write-JsonFile {
    param([string]$Path, [object]$Value)
    Write-Utf8 $Path (($Value | ConvertTo-Json -Depth 12) + "`n")
}

function Organize-Volume {
    param([int]$Volume, [string]$SourceDir)
    $volumeKey = "vol_$Volume"
    $volumeRoot = Join-Path $TargetRoot $volumeKey
    $ocrRoot = Join-Path $TargetRoot "ocr\$volumeKey"
    $mapRoot = Join-Path $TargetRoot "page_maps\$volumeKey"
    $archiveRoot = Join-Path $volumeRoot "archive_raw"
    $originalNames = [ordered]@{}

    Write-OriginalFileList $SourceDir (Join-Path $archiveRoot "original_file_list.txt")
    Write-Utf8 (Join-Path $archiveRoot "archive_metadata_source.txt") ("Internet Archive download directory:`n$SourceDir`n")
    Write-Utf8 (Join-Path $archiveRoot "README.md") ("# Archive Raw`n`nInternet Archive metadata and original file inventory for volume $Volume.`n")

    $files = Get-ChildItem -LiteralPath $SourceDir -Recurse -File | Sort-Object FullName
    foreach ($file in $files) {
        $name = $file.Name
        $lower = $name.ToLowerInvariant()
        $destination = $null
        $category = $null
        $canonicalName = $null

        if ($lower -match "_1729_$Volume\.pdf$") {
            $destination = Join-Path $volumeRoot "pdf\motte_1729_vol$Volume.pdf"
            Copy-ManagedFile $Volume "pdf" $file $destination
            continue
        }
        $ocrRules = [ordered]@{
            "_djvu.txt" = "djvu.txt"
            "_djvu.xml" = "djvu.xml"
            "_hocr.html" = "hocr.html"
            "_hocr_pageindex.json.gz" = "hocr_pageindex.json.gz"
            "_hocr_searchtext.txt.gz" = "hocr_searchtext.txt.gz"
            "_abbyy.gz" = "abbyy.gz"
        }
        $matchedOcr = $false
        foreach ($suffix in $ocrRules.Keys) {
            if ($lower.EndsWith($suffix)) {
                $canonicalName = $ocrRules[$suffix]
                $destination = Join-Path $ocrRoot $canonicalName
                Copy-ManagedFile $Volume "ocr" $file $destination
                $originalNames[$canonicalName] = $name
                $matchedOcr = $true
                break
            }
        }
        if ($matchedOcr) { continue }
        if ($lower.EndsWith("_page_numbers.json")) {
            $destination = Join-Path $mapRoot "page_numbers.json"
            Copy-ManagedFile $Volume "page_map" $file $destination
            continue
        }
        if ($lower.EndsWith("_scandata.xml")) {
            $destination = Join-Path $mapRoot "scandata.xml"
            Copy-ManagedFile $Volume "page_map" $file $destination
            continue
        }
        if ($lower.EndsWith("_meta.xml") -or $lower.EndsWith("_files.xml") -or $lower.EndsWith("_meta.sqlite")) {
            $destination = Join-Path $archiveRoot $name
            Copy-ManagedFile $Volume "archive_metadata" $file $destination
            continue
        }
        if ($lower.EndsWith("_archive.torrent")) {
            $destination = Join-Path $volumeRoot ("derivatives\torrent\" + $name)
            Copy-ManagedFile $Volume "torrent" $file $destination
            continue
        }
        if ($lower.EndsWith(".epub")) {
            $destination = Join-Path $volumeRoot ("derivatives\epub\" + $name)
            Copy-ManagedFile $Volume "epub" $file $destination
            continue
        }
        if ($lower.EndsWith(".mobi") -or $lower.EndsWith(".azw3")) {
            $destination = Join-Path $volumeRoot ("derivatives\kindle\" + $name)
            Copy-ManagedFile $Volume "kindle" $file $destination
            continue
        }
        if ($lower.EndsWith(".zip") -and $file.Length -gt $LargeFileThreshold) {
            Add-LargeAsset $Volume $file $volumeRoot
            continue
        }
        if ($lower.EndsWith(".zip") -and $lower.Contains("_jp2")) {
            $destination = Join-Path $volumeRoot ("large_assets\jp2\" + $name)
            Copy-ManagedFile $Volume "large_asset" $file $destination
            continue
        }

        $relative = $file.FullName.Substring($SourceDir.Length).TrimStart("\")
        $destination = Join-Path $volumeRoot ("derivatives\other\" + $relative)
        Copy-ManagedFile $Volume "other" $file $destination
    }

    Write-JsonFile (Join-Path $ocrRoot "original_names.json") $originalNames
    Write-Utf8 (Join-Path $ocrRoot "README.md") ("# OCR Volume $Volume`n`nUse ``djvu.txt``, ``djvu.xml``, and ``hocr.html`` before considering fresh OCR of a PDF. Verify final quotations against the matching Internet Archive scan under ``vol_$Volume/pdf/``. Treat ``vol_$Volume/raw_pdf/`` as a supplementary reprint reference only.`n")
    $review = [ordered]@{
        volume = $Volume
        status = "not_reviewed"
        source_files = [ordered]@{
            page_numbers = "page_numbers.json"
            scandata = "scandata.xml"
        }
        notes = @(
            "This file is reserved for manual mapping between scan page index, printed page number, and Principia nodes."
            "Do not rely only on OCR page numbering before manual review."
        )
        review_items = @()
    }
    Write-JsonFile (Join-Path $mapRoot "page_map_manual_review.json") $review
    Write-Utf8 (Join-Path $mapRoot "README.md") ("# Page Maps Volume $Volume`n`nPage-number data is imported from Internet Archive and must be manually reviewed before node extraction.`n")
    Write-Utf8 (Join-Path $TargetRoot "extracted_nodes\$volumeKey\README.md") ("# Extracted Nodes Volume $Volume`n`nReserved for manually verified English node slices. This organize step intentionally creates no node content.`n")
}

function Escape-Markdown {
    param([string]$Value)
    if ($null -eq $Value) { return "" }
    return $Value.Replace("|", "\|").Replace("`r", " ").Replace("`n", " ")
}

foreach ($required in @($SourceVol1, $SourceVol2, $TargetRoot)) {
    if (-not (Test-Path -LiteralPath $required)) {
        throw "Required path does not exist: $required"
    }
}

$directories = @(
    "vol_1\pdf", "vol_1\archive_raw", "vol_1\derivatives\epub", "vol_1\derivatives\kindle",
    "vol_1\derivatives\torrent", "vol_1\derivatives\other", "vol_1\large_assets\jp2", "vol_1\large_assets\pointers",
    "vol_2\pdf", "vol_2\archive_raw", "vol_2\derivatives\epub", "vol_2\derivatives\kindle",
    "vol_2\derivatives\torrent", "vol_2\derivatives\other", "vol_2\large_assets\jp2", "vol_2\large_assets\pointers",
    "ocr\vol_1", "ocr\vol_2", "page_maps\vol_1", "page_maps\vol_2",
    "extracted_nodes\vol_1", "extracted_nodes\vol_2", "tools", "logs"
)
foreach ($relative in $directories) {
    New-Item -ItemType Directory -Force -Path (Join-Path $TargetRoot $relative) | Out-Null
}

Write-Output "Plan: organize Motte 1729 Internet Archive resources"
Write-Output "  SourceVol1: $SourceVol1"
Write-Output "  SourceVol2: $SourceVol2"
Write-Output "  TargetRoot: $TargetRoot"
Write-Output "  Mode: $Mode"
Write-Output "  LargeFilePolicy: $LargeFilePolicy"

$LogLines.Add("# Motte 1729 Organization Log")
$LogLines.Add("")
$LogLines.Add("- Time: $(Get-Date -Format "yyyy-MM-dd HH:mm:ss")")
$LogLines.Add("- Mode: $Mode")
$LogLines.Add("- Large file policy: $LargeFilePolicy")
$LogLines.Add("- Source volume 1: $SourceVol1")
$LogLines.Add("- Source volume 2: $SourceVol2")
$LogLines.Add("- Target root: $TargetRoot")
$LogLines.Add("")
$LogLines.Add("## Actions")

Organize-Volume 1 $SourceVol1
Organize-Volume 2 $SourceVol2

$expected = @(
    "vol_1\pdf\motte_1729_vol1.pdf", "vol_2\pdf\motte_1729_vol2.pdf",
    "ocr\vol_1\djvu.txt", "ocr\vol_1\djvu.xml", "ocr\vol_1\hocr.html", "ocr\vol_1\hocr_pageindex.json.gz",
    "ocr\vol_1\hocr_searchtext.txt.gz", "ocr\vol_1\abbyy.gz", "page_maps\vol_1\page_numbers.json", "page_maps\vol_1\scandata.xml",
    "ocr\vol_2\djvu.txt", "ocr\vol_2\djvu.xml", "ocr\vol_2\hocr.html", "ocr\vol_2\hocr_pageindex.json.gz",
    "ocr\vol_2\hocr_searchtext.txt.gz", "ocr\vol_2\abbyy.gz", "page_maps\vol_2\page_numbers.json", "page_maps\vol_2\scandata.xml"
)
foreach ($relative in $expected) {
    if (-not (Test-Path -LiteralPath (Join-Path $TargetRoot $relative))) {
        $Missing.Add($relative)
    }
}

$manifest = [ordered]@{
    project = "Newton_course"
    source = "Andrew Motte 1729 English translation of Newton's Principia"
    generated_at = (Get-Date).ToString("s")
    pdf_source_priority = "pdf_source_priority.json"
    pdf_source_rule = "Use existing OCR first. For page mapping, OCR alignment, scan verification, English node extraction, and fallback OCR, use vol_*/pdf/motte_1729_vol*.pdf. Treat vol_*/raw_pdf/ as supplementary modern reprint references only."
    volumes = [ordered]@{
        vol_1 = [ordered]@{
            source_dir = $SourceVol1
            files = @($Records | Where-Object { $_.volume -eq 1 })
        }
        vol_2 = [ordered]@{
            source_dir = $SourceVol2
            files = @($Records | Where-Object { $_.volume -eq 2 })
        }
    }
    missing_expected_files = @($Missing)
}
Write-JsonFile (Join-Path $TargetRoot "MANIFEST_motte_1729.json") $manifest

$manifestMd = @(
    "# MANIFEST: Andrew Motte 1729 Resources"
    ""
    "Generated: $(Get-Date -Format "yyyy-MM-dd HH:mm:ss")"
    ""
    "| Volume | Category | Canonical path | Original path | Size bytes | Action | SHA256 | Notes |"
    "|---|---|---|---|---:|---|---|---|"
)
foreach ($record in $Records) {
    $manifestMd += "| $($record.volume) | $(Escape-Markdown $record.category) | ``$(Escape-Markdown $record.canonical_path)`` | ``$(Escape-Markdown $record.original_path)`` | $($record.size_bytes) | $($record.action) | $($record.sha256) | $(Escape-Markdown $record.notes) |"
}
Write-Utf8 (Join-Path $TargetRoot "MANIFEST_motte_1729.md") (($manifestMd -join "`n") + "`n")

$checksumPath = Join-Path $TargetRoot "logs\checksum_report.csv"
$Records | Select-Object volume, category, canonical_path, original_path, size_bytes, sha256, action |
    Export-Csv -LiteralPath $checksumPath -NoTypeInformation -Encoding UTF8

$missingLines = @(
    "# Missing Files Report"
    ""
    "Generated: $(Get-Date -Format "yyyy-MM-dd HH:mm:ss")"
    ""
    "The following optional expected derivatives were not found after organization:"
    ""
)
if ($Missing.Count -eq 0) {
    $missingLines += "- None."
}
else {
    foreach ($item in $Missing) {
        $missingLines += "- ``$item``"
    }
}
$missingLines += ""
$missingLines += "The missing ``abbyy.gz`` files are ABBYY OCR XML derivatives. They are distinct from ``hocr_pageindex.json.gz`` and ``hocr_searchtext.txt.gz``. Their absence is not blocking because DJVU text, DJVU XML, HOCR, page-number JSON, and scandata XML are available."
$missingLines += ""
$missingLines += "Unrecognized Internet Archive derivatives were preserved under each volume's `derivatives\other\` directory."
Write-Utf8 (Join-Path $TargetRoot "logs\missing_files_report.md") (($missingLines -join "`n") + "`n")

$LogLines.Add("")
$LogLines.Add("## Summary")
$LogLines.Add("- Manifest records: $($Records.Count)")
$LogLines.Add("- Missing expected files: $($Missing.Count)")
$LogLines.Add("- Source files were copied or hardlinked only; no source files were deleted, moved, or renamed.")
$organizationLog = Join-Path $TargetRoot "logs\organize_motte_1729_log.md"
$newLogSection = ($LogLines -join "`n") + "`n"
if (Test-Path -LiteralPath $organizationLog) {
    $previousLog = [System.IO.File]::ReadAllText($organizationLog)
    Write-Utf8 $organizationLog ($previousLog.TrimEnd() + "`n`n---`n`n" + $newLogSection)
}
else {
    Write-Utf8 $organizationLog $newLogSection
}

Write-Output "Completed organization. Manifest records: $($Records.Count). Missing expected files: $($Missing.Count)."
