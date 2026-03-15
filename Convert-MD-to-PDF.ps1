# PowerShell Script to Convert Markdown Files to PDF
# Author: Auto-generated for 365EnglishPractice
# Date: March 15, 2026

<#
.SYNOPSIS
    Converts all Markdown (.md) files in the current directory to PDF format using Pandoc.

.DESCRIPTION
    This script checks if Pandoc is installed, then converts all .md files to PDF.
    It creates PDFs with proper formatting, margins, and professional appearance.

.EXAMPLE
    .\Convert-MD-to-PDF.ps1
    Converts all .md files in the current directory to PDF

.EXAMPLE
    .\Convert-MD-to-PDF.ps1 -Specific "ADVANCED_VOCABULARY_ESSAY.md"
    Converts only the specified file to PDF
#>

param(
    [string]$Specific = "",
    [string]$OutputFolder = "PDFs",
    [switch]$IncludeSubfolders = $false
)

# Color output functions
function Write-Success { param($Message) Write-Host $Message -ForegroundColor Green }
function Write-Info { param($Message) Write-Host $Message -ForegroundColor Cyan }
function Write-Warning { param($Message) Write-Host $Message -ForegroundColor Yellow }
function Write-Error { param($Message) Write-Host $Message -ForegroundColor Red }

# Banner
Write-Host "`n========================================" -ForegroundColor Magenta
Write-Host "   Markdown to PDF Converter" -ForegroundColor Magenta
Write-Host "========================================`n" -ForegroundColor Magenta

# Check if Pandoc is installed
Write-Info "Checking for Pandoc installation..."
try {
    $pandocVersion = pandoc --version 2>&1 | Select-Object -First 1
    Write-Success "✓ Pandoc found: $pandocVersion"
} catch {
    Write-Error "✗ Pandoc is not installed!"
    Write-Warning "`nTo install Pandoc, run one of these commands:"
    Write-Host "  Option 1 (winget): " -NoNewline
    Write-Host "winget install --id JohnMacFarlane.Pandoc" -ForegroundColor Yellow
    Write-Host "  Option 2 (choco):  " -NoNewline
    Write-Host "choco install pandoc" -ForegroundColor Yellow
    Write-Host "`nAfter installation, restart PowerShell and run this script again.`n"
    exit 1
}

# Create output folder if it doesn't exist
if (-not (Test-Path $OutputFolder)) {
    New-Item -ItemType Directory -Path $OutputFolder | Out-Null
    Write-Success "✓ Created output folder: $OutputFolder"
}

# Get the script directory
$scriptDir = Get-Location

# Get markdown files
if ($Specific) {
    $mdFiles = Get-Item $Specific -ErrorAction SilentlyContinue
    if (-not $mdFiles) {
        Write-Error "✗ File not found: $Specific"
        exit 1
    }
} elseif ($IncludeSubfolders) {
    $mdFiles = Get-ChildItem -Path $scriptDir -Filter "*.md" -Recurse
} else {
    $mdFiles = Get-ChildItem -Path $scriptDir -Filter "*.md"
}

if ($mdFiles.Count -eq 0) {
    Write-Warning "No Markdown files found in the current directory."
    exit 0
}

Write-Info "`nFound $($mdFiles.Count) Markdown file(s) to convert:`n"
$mdFiles | ForEach-Object { Write-Host "  • $($_.Name)" -ForegroundColor White }
Write-Host ""

# Conversion statistics
$successCount = 0
$failCount = 0
$skippedCount = 0

# Convert each file
foreach ($file in $mdFiles) {
    $fileName = $file.BaseName
    $outputPath = Join-Path $OutputFolder "$fileName.pdf"
    
    Write-Info "Converting: $($file.Name)..."
    
    try {
        # Pandoc conversion with professional formatting
        $pandocArgs = @(
            $file.FullName,
            "-o", $outputPath,
            "--pdf-engine=xelatex",
            "-V", "geometry:margin=1in",
            "-V", "fontsize=11pt",
            "-V", "linestretch=1.5",
            "--highlight-style=tango"
        )
        
        $process = Start-Process -FilePath "pandoc" -ArgumentList $pandocArgs -NoNewWindow -Wait -PassThru
        
        if ($process.ExitCode -eq 0 -and (Test-Path $outputPath)) {
            $fileSize = (Get-Item $outputPath).Length
            $fileSizeKB = [math]::Round($fileSize / 1KB, 2)
            Write-Success "  ✓ Success! Created: $fileName.pdf ($fileSizeKB KB)"
            $successCount++
        } else {
            Write-Error "  ✗ Failed to convert: $($file.Name)"
            $failCount++
        }
    } catch {
        Write-Error "  ✗ Error converting $($file.Name): $($_.Exception.Message)"
        $failCount++
    }
}

# Summary
Write-Host "`n========================================" -ForegroundColor Magenta
Write-Host "   Conversion Summary" -ForegroundColor Magenta
Write-Host "========================================" -ForegroundColor Magenta
Write-Success "✓ Successful: $successCount"
if ($failCount -gt 0) { Write-Error "✗ Failed: $failCount" }
if ($skippedCount -gt 0) { Write-Warning "⊘ Skipped: $skippedCount" }
Write-Host "========================================`n" -ForegroundColor Magenta

if ($successCount -gt 0) {
    Write-Info "PDFs saved to: $((Get-Item $OutputFolder).FullName)"
    Write-Host "`nTo open the PDF folder, run: " -NoNewline
    Write-Host "explorer $OutputFolder" -ForegroundColor Yellow
}

# Offer to open the folder
if ($successCount -gt 0) {
    Write-Host "`nWould you like to open the PDF folder now? (Y/N): " -NoNewline -ForegroundColor Cyan
    $response = Read-Host
    if ($response -eq 'Y' -or $response -eq 'y') {
        Start-Process explorer $OutputFolder
    }
}

Write-Host ""
