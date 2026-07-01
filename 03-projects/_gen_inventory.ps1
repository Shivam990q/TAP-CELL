# Legacy PowerShell inventory generator (kept for reference).
# NOTE: The maintained tool is now `python tools/sync_github.py` (also reports repo changes).
$path = Join-Path $PSScriptRoot '_github-raw.json'
$out  = Join-Path $PSScriptRoot 'github-inventory.md'
$j = Get-Content $path -Raw | ConvertFrom-Json

$sb = New-Object System.Text.StringBuilder
[void]$sb.AppendLine("# GitHub Inventory - Shivam990q")
[void]$sb.AppendLine("")
[void]$sb.AppendLine("Auto-generated from GitHub. Total: " + $j.Count + " repos (" + ($j | Where-Object { -not $_.isPrivate }).Count + " public, " + ($j | Where-Object { $_.isPrivate }).Count + " private, " + ($j | Where-Object { $_.isFork }).Count + " forks).")
[void]$sb.AppendLine("")
[void]$sb.AppendLine("| Repo | Lang | Vis | Fork | Stars | Updated | Description |")
[void]$sb.AppendLine("| --- | --- | --- | --- | --- | --- | --- |")

$rows = $j | Sort-Object { $_.pushedAt } -Descending
foreach ($r in $rows) {
  $lang = if ($r.primaryLanguage) { $r.primaryLanguage.name } else { "-" }
  $vis  = if ($r.isPrivate) { "priv" } else { "pub" }
  $fork = if ($r.isFork) { "fork" } else { "" }
  $upd  = ($r.pushedAt -split "T")[0]
  $desc = ($r.description -replace "\r?\n"," " -replace "\|","/")
  if ([string]::IsNullOrWhiteSpace($desc)) { $desc = "" }
  $line = "| [" + $r.name + "](" + $r.url + ") | " + $lang + " | " + $vis + " | " + $fork + " | " + $r.stargazerCount + " | " + $upd + " | " + $desc + " |"
  [void]$sb.AppendLine($line)
}
Set-Content -Path $out -Value $sb.ToString() -Encoding UTF8
Write-Output ("Wrote " + $out)
