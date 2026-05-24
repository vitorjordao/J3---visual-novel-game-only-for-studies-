param([string]$Root = "G:\Vitor\J3 project\Projeto\J3 Project\game\characters")

$results = @()
Get-ChildItem -Path $Root -Recurse -Filter *.png -File | Where-Object { $_.FullName -notmatch "\\_backups\\" } | ForEach-Object {
    try {
        $fs = [System.IO.File]::OpenRead($_.FullName)
        $buf = New-Object byte[] 24
        [void]$fs.Read($buf, 0, 24)
        $fs.Close()
    } catch { return }
    if ($buf.Count -lt 24) { return }
    if ($buf[0] -ne 0x89 -or $buf[1] -ne 0x50) { return }
    # IHDR width = bytes 16-19, height = bytes 20-23, big-endian
    $w = ([int]$buf[16] -shl 24) -bor ([int]$buf[17] -shl 16) -bor ([int]$buf[18] -shl 8) -bor [int]$buf[19]
    $h = ([int]$buf[20] -shl 24) -bor ([int]$buf[21] -shl 16) -bor ([int]$buf[22] -shl 8) -bor [int]$buf[23]
    $results += [PSCustomObject]@{
        Name   = $_.BaseName
        W      = $w
        H      = $h
        AR     = [math]::Round($w / $h, 3)
        SizeKB = [math]::Round($_.Length / 1KB, 1)
        Path   = $_.FullName.Replace("$Root\", "")
    }
}
$results | Sort-Object Name | Format-Table -AutoSize
