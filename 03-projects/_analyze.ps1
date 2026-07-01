$path = Join-Path $PSScriptRoot '_github-raw.json'
$j = Get-Content $path -Raw | ConvertFrom-Json
Write-Output ("TOTAL: " + $j.Count)
Write-Output ("PUBLIC: " + ($j | Where-Object { -not $_.isPrivate }).Count)
Write-Output ("PRIVATE: " + ($j | Where-Object { $_.isPrivate }).Count)
Write-Output ("FORKS: " + ($j | Where-Object { $_.isFork }).Count)
Write-Output "--- BY LANGUAGE ---"
$j | Group-Object { $_.primaryLanguage.name } | Sort-Object Count -Descending | ForEach-Object { Write-Output ($_.Name + ": " + $_.Count) }
