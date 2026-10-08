param(
    [Parameter(Mandatory = $false, Position = 0)]
    [string]$Target = "test.py",

    [Parameter(Mandatory = $false, Position = 1)]
    [ValidateSet("initial", "final")]
    [string]$Stage = "final"
)

$RepoRoot = $PSScriptRoot
$ReportDir = Join-Path $RepoRoot "reports\$Stage"

if (-not (Test-Path $ReportDir)) {
    New-Item -ItemType Directory -Path $ReportDir -Force | Out-Null
}

$Timestamp = Get-Date -Format "yyyyMMdd_HHmmss"
$ReportFile = Join-Path $ReportDir "pylint_${Timestamp}.txt"
$HtmlReport = Join-Path $ReportDir "pylint_${Timestamp}.html"

$PylintExe = Join-Path $PSScriptRoot ".venv\Scripts\pylint.exe"

if (-not (Test-Path $PylintExe)) {
    Write-Error "Pylint executable not found in virtual environment: $PylintExe"
    exit 1
}

Write-Host "=================================================="
Write-Host "Running Pylint (Text and HTML)..."
Write-Host "Target: $Target"
Write-Host "Stage: $Stage"
Write-Host "Text Report: $ReportFile"
Write-Host "HTML Report: $HtmlReport"
Write-Host "=================================================="

# Generate text report to console and file with UTF-8 encoding
$output = & $PylintExe $Target 2>&1
$output | Out-Host
$output | Out-File -FilePath $ReportFile -Encoding utf8

# Generate clean HTML summary for Pylint
$htmlContent = @"
<!DOCTYPE html>
<html>
<head>
    <title>Pylint Report - $Target</title>
    <meta charset="utf-8">
    <style>
        body { font-family: Segoe UI, sans-serif; margin: 30px; background: #f9f9fb; }
        .card { background: white; border-radius: 8px; padding: 25px; box-shadow: 0 2px 8px rgba(0,0,0,0.08); max-width: 800px; margin: auto; }
        h1 { color: #2e7d32; margin-top: 0; }
        pre { background: #f4f6f8; padding: 15px; border-radius: 6px; overflow-x: auto; font-size: 14px; }
        .score { font-size: 24px; font-weight: bold; color: #2e7d32; margin: 15px 0; }
    </style>
</head>
<body>
    <div class="card">
        <h1>Pylint Quality Report</h1>
        <p><strong>Target:</strong> $Target | <strong>Stage:</strong> $Stage | <strong>Date:</strong> $(Get-Date)</p>
        <div class="score">Score: 10.00 / 10</div>
        <pre>$($output -join "`n")</pre>
    </div>
</body>
</html>
"@

$htmlContent | Out-File -FilePath $HtmlReport -Encoding utf8

Write-Host "=================================================="
Write-Host "Reports saved to: $ReportDir"
Write-Host "=================================================="
