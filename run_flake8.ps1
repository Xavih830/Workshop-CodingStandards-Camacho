param(
    [Parameter(Mandatory = $false, Position = 0)]
    [string]$Target = "test.py",

    [Parameter(Mandatory = $false, Position = 1)]
    [ValidateSet("initial", "final")]
    [string]$Stage = "final"
)

$RepoRoot = $PSScriptRoot
$ReportDir = Join-Path $RepoRoot "reports\$Stage"
$HtmlDir = Join-Path $ReportDir "flake8_html"

if (-not (Test-Path $ReportDir)) {
    New-Item -ItemType Directory -Path $ReportDir -Force | Out-Null
}

$Timestamp = Get-Date -Format "yyyyMMdd_HHmmss"
$ReportFile = Join-Path $ReportDir "flake8_${Timestamp}.txt"

$Flake8Exe = Join-Path $PSScriptRoot ".venv\Scripts\flake8.exe"

if (-not (Test-Path $Flake8Exe)) {
    Write-Error "Flake8 executable not found in virtual environment: $Flake8Exe"
    exit 1
}

Write-Host "=================================================="
Write-Host "Running Flake8 (Text and HTML)..."
Write-Host "Target: $Target"
Write-Host "Stage: $Stage"
Write-Host "Text Report: $ReportFile"
Write-Host "HTML Report: $HtmlDir\index.html"
Write-Host "=================================================="

# Generate text report to console and file with UTF-8 encoding
$output = & $Flake8Exe $Target 2>&1
$output | Out-Host
$output | Out-File -FilePath $ReportFile -Encoding utf8

# Generate HTML report
& $Flake8Exe --format=html --htmldir=$HtmlDir $Target 2>$null

Write-Host "=================================================="
Write-Host "Reports saved to: $ReportDir"
Write-Host "=================================================="
