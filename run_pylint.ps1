param(
    [Parameter(Mandatory = $false, Position = 0)]
    [string]$Target = "test.py",

    [Parameter(Mandatory = $false, Position = 1)]
    [ValidateSet("initial", "final")]
    [string]$Stage = "initial"
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
$Json2HtmlExe = Join-Path $PSScriptRoot ".venv\Scripts\pylint-json2html.exe"

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

# Generate text report to console and file
& $PylintExe $Target 2>&1 | Tee-Object -FilePath $ReportFile

# Generate HTML report if json2html is available
if (Test-Path $Json2HtmlExe) {
    try {
        $jsonOutput = & $PylintExe -f json $Target 2>$null
        $jsonOutput | & $Json2HtmlExe -o $HtmlReport
    } catch {
        # Proceed if syntax prevents JSON output
    }
}

Write-Host "=================================================="
Write-Host "Reports saved to: $ReportDir"
Write-Host "=================================================="
