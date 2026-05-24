param([string]$Root = "G:\Vitor\J3 project")

$results = @()
Get-ChildItem -Path $Root -Recurse -Filter *.png -File | ForEach-Object {
    try {
        $fs = [System.IO.File]::OpenRead($_.FullName)
        $buf = New-Object byte[] 26
        [void]$fs.Read($buf, 0, 26)
        $fs.Close()
    } catch {
        return
    }
    if ($buf.Count -lt 26) { return }

    # PNG signature check: 89 50 4E 47 0D 0A 1A 0A
    if ($buf[0] -ne 0x89 -or $buf[1] -ne 0x50 -or $buf[2] -ne 0x4E -or $buf[3] -ne 0x47) {
        return
    }

    $bitDepth  = $buf[24]
    $colorType = $buf[25]
    $bpp = switch ($colorType) {
        0 { $bitDepth }           # grayscale
        2 { $bitDepth * 3 }       # RGB
        3 { $bitDepth }           # indexed (palette)
        4 { $bitDepth * 2 }       # gray + alpha
        6 { $bitDepth * 4 }       # RGBA
        default { 0 }
    }
    $colorName = switch ($colorType) {
        0 { "Gray" }
        2 { "RGB" }
        3 { "Indexed" }
        4 { "Gray+A" }
        6 { "RGBA" }
        default { "?" }
    }

    $results += [PSCustomObject]@{
        Path      = $_.FullName.Replace("$Root\", "")
        BitDepth  = $bitDepth
        ColorType = $colorName
        BPP       = $bpp
        SizeKB    = [math]::Round($_.Length / 1KB, 1)
    }
}

Write-Host "`n=== ALL PNGs (sorted by BPP) ===" -ForegroundColor Cyan
$results | Sort-Object BPP, Path | Format-Table -AutoSize

Write-Host "`n=== OUTLIERS (BPP < 32 = not 8-bit RGBA) ===" -ForegroundColor Yellow
$outliers = $results | Where-Object { $_.BPP -lt 32 }
if ($outliers.Count -eq 0) {
    Write-Host "None. All PNGs are 32-bit RGBA." -ForegroundColor Green
} else {
    $outliers | Sort-Object BPP, Path | Format-Table -AutoSize
    Write-Host "`nTotal outliers: $($outliers.Count) of $($results.Count)" -ForegroundColor Yellow
}
