param(
    [Parameter(Mandatory = $true)]
    [string]$InputDocx,

    [Parameter(Mandatory = $true)]
    [string]$OutputDir,

    [int]$StartIndex = 3,

    [int]$EndIndex = 16,

    [int]$MaxWidth = 2400
)

Add-Type -AssemblyName System.Drawing
Add-Type -AssemblyName System.IO.Compression.FileSystem

$resolvedDocx = (Resolve-Path -LiteralPath $InputDocx).Path
$resolvedOutput = [System.IO.Path]::GetFullPath($OutputDir)
[System.IO.Directory]::CreateDirectory($resolvedOutput) | Out-Null

$archive = [System.IO.Compression.ZipFile]::OpenRead($resolvedDocx)
try {
    foreach ($index in $StartIndex..$EndIndex) {
        $entryName = "word/media/image$index.wmf"
        $entry = $archive.GetEntry($entryName)
        if (-not $entry) {
            throw "Missing DOCX formula preview: $entryName"
        }

        $tempPath = Join-Path $resolvedOutput "image$index.wmf"
        $pngPath = Join-Path $resolvedOutput "image$index.png"
        $source = $entry.Open()
        $target = [System.IO.File]::Create($tempPath)
        try {
            $source.CopyTo($target)
        } finally {
            $source.Dispose()
            $target.Dispose()
        }

        $image = [System.Drawing.Image]::FromFile($tempPath)
        try {
            $scale = [Math]::Min(1.0, $MaxWidth / $image.Width)
            $width = [Math]::Max(1, [Math]::Round($image.Width * $scale))
            $height = [Math]::Max(1, [Math]::Round($image.Height * $scale))
            $bitmap = New-Object System.Drawing.Bitmap($width, $height)
            try {
                $graphics = [System.Drawing.Graphics]::FromImage($bitmap)
                try {
                    $graphics.Clear([System.Drawing.Color]::White)
                    $graphics.DrawImage($image, 0, 0, $width, $height)
                } finally {
                    $graphics.Dispose()
                }
                $bitmap.Save($pngPath, [System.Drawing.Imaging.ImageFormat]::Png)
            } finally {
                $bitmap.Dispose()
            }
        } finally {
            $image.Dispose()
        }

        Remove-Item -LiteralPath $tempPath
        Write-Output "EXTRACTED $entryName -> $pngPath"
    }
} finally {
    $archive.Dispose()
}
