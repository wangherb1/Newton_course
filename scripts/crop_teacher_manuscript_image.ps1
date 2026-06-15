param(
    [Parameter(Mandatory = $true)]
    [string]$InputPath,

    [Parameter(Mandatory = $true)]
    [string]$OutputPath,

    [Parameter(Mandatory = $true)]
    [int]$X,

    [Parameter(Mandatory = $true)]
    [int]$Y,

    [Parameter(Mandatory = $true)]
    [int]$Width,

    [Parameter(Mandatory = $true)]
    [int]$Height
)

Add-Type -AssemblyName System.Drawing

$resolvedInput = (Resolve-Path -LiteralPath $InputPath).Path
$resolvedOutput = [System.IO.Path]::GetFullPath($OutputPath)
$outputDirectory = [System.IO.Path]::GetDirectoryName($resolvedOutput)
[System.IO.Directory]::CreateDirectory($outputDirectory) | Out-Null

$source = [System.Drawing.Image]::FromFile($resolvedInput)
try {
    if ($X -lt 0 -or $Y -lt 0 -or $Width -le 0 -or $Height -le 0) {
        throw "Crop values must be positive and start inside the source image."
    }
    if (($X + $Width) -gt $source.Width -or ($Y + $Height) -gt $source.Height) {
        throw "Crop rectangle exceeds source dimensions $($source.Width)x$($source.Height)."
    }

    $target = New-Object System.Drawing.Bitmap($Width, $Height)
    try {
        $graphics = [System.Drawing.Graphics]::FromImage($target)
        try {
            $graphics.DrawImage(
                $source,
                (New-Object System.Drawing.Rectangle(0, 0, $Width, $Height)),
                (New-Object System.Drawing.Rectangle($X, $Y, $Width, $Height)),
                [System.Drawing.GraphicsUnit]::Pixel
            )
        } finally {
            $graphics.Dispose()
        }
        $target.Save($resolvedOutput, [System.Drawing.Imaging.ImageFormat]::Png)
    } finally {
        $target.Dispose()
    }
} finally {
    $source.Dispose()
}

Write-Output "CROPPED $resolvedInput -> $resolvedOutput ($Width x $Height)"
