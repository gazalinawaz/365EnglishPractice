# How to Convert Markdown Files to PDF

This guide explains how to use the PowerShell script to convert your Markdown files to PDF format.

---

## Prerequisites

### Step 1: Install Pandoc

**Option A: Using winget (Recommended)**
```powershell
winget install --id JohnMacFarlane.Pandoc
```

**Option B: Using Chocolatey**
```powershell
choco install pandoc
```

**Option C: Manual Download**
- Visit: https://pandoc.org/installing.html
- Download and install the Windows installer

### Step 2: Install MiKTeX (PDF Engine)

**Option A: Using winget**
```powershell
winget install --id MiKTeX.MiKTeX
```

**Option B: Manual Download**
- Visit: https://miktex.org/download
- Download and install MiKTeX

**After installation:** Restart PowerShell/Terminal

---

## Using the Conversion Script

### Basic Usage (Convert All MD Files)

```powershell
# Navigate to your project folder
cd "C:\Users\g.nawaz\Documents\365EnglishPractice"

# Run the script
.\Convert-MD-to-PDF.ps1
```

This will:
- Convert all `.md` files in the current directory
- Save PDFs to a `PDFs` folder
- Show progress and summary

---

## Advanced Usage

### Convert a Specific File

```powershell
.\Convert-MD-to-PDF.ps1 -Specific "ADVANCED_VOCABULARY_ESSAY.md"
```

### Convert Files in Subfolders Too

```powershell
.\Convert-MD-to-PDF.ps1 -IncludeSubfolders
```

### Specify Custom Output Folder

```powershell
.\Convert-MD-to-PDF.ps1 -OutputFolder "MyPDFs"
```

### Combine Options

```powershell
.\Convert-MD-to-PDF.ps1 -Specific "Day_001.md" -OutputFolder "DayPDFs"
```

---

## Script Features

✅ **Automatic Pandoc Detection** - Checks if Pandoc is installed  
✅ **Professional Formatting** - 1-inch margins, 11pt font, 1.5 line spacing  
✅ **Batch Conversion** - Converts multiple files at once  
✅ **Progress Tracking** - Shows conversion status for each file  
✅ **Error Handling** - Reports any conversion failures  
✅ **Summary Statistics** - Shows success/fail counts  
✅ **Auto Folder Creation** - Creates output folder if needed  

---

## Expected Output

After running the script, you'll see:

```
========================================
   Markdown to PDF Converter
========================================

✓ Pandoc found: pandoc 3.x.x
✓ Created output folder: PDFs

Found 3 Markdown file(s) to convert:

  • ADVANCED_VOCABULARY_ESSAY.md
  • COMPREHENSIVE_VOCABULARY_ESSAY.md
  • CONCISE_VOCABULARY_ESSAY.md

Converting: ADVANCED_VOCABULARY_ESSAY.md...
  ✓ Success! Created: ADVANCED_VOCABULARY_ESSAY.pdf (245.67 KB)

Converting: COMPREHENSIVE_VOCABULARY_ESSAY.md...
  ✓ Success! Created: COMPREHENSIVE_VOCABULARY_ESSAY.pdf (312.45 KB)

Converting: CONCISE_VOCABULARY_ESSAY.md...
  ✓ Success! Created: CONCISE_VOCABULARY_ESSAY.pdf (187.23 KB)

========================================
   Conversion Summary
========================================
✓ Successful: 3
========================================

PDFs saved to: C:\Users\g.nawaz\Documents\365EnglishPractice\PDFs

Would you like to open the PDF folder now? (Y/N):
```

---

## Troubleshooting

### Error: "Pandoc is not installed"

**Solution:** Install Pandoc using one of the methods above, then restart PowerShell.

### Error: "xelatex not found"

**Solution:** Install MiKTeX (the PDF engine):
```powershell
winget install --id MiKTeX.MiKTeX
```

### Error: "Execution policy does not allow running scripts"

**Solution:** Run PowerShell as Administrator and execute:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### PDFs have formatting issues

**Solution:** The script uses XeLaTeX for better formatting. If issues persist, try:
```powershell
# Use default PDF engine instead
pandoc yourfile.md -o yourfile.pdf
```

---

## Manual Conversion (Without Script)

If you prefer to convert files manually:

```powershell
# Basic conversion
pandoc ADVANCED_VOCABULARY_ESSAY.md -o ADVANCED_VOCABULARY_ESSAY.pdf

# With better formatting
pandoc ADVANCED_VOCABULARY_ESSAY.md -o ADVANCED_VOCABULARY_ESSAY.pdf --pdf-engine=xelatex -V geometry:margin=1in -V fontsize=11pt
```

---

## Files to Convert

Your project currently has these essay files ready for PDF conversion:

1. **ADVANCED_VOCABULARY_ESSAY.md** (~5,000 words) - Only sophisticated vocabulary
2. **COMPREHENSIVE_VOCABULARY_ESSAY.md** (~5,000 words) - All 170 vocabulary words
3. **CONCISE_VOCABULARY_ESSAY.md** (~2,500 words) - Core 120 words
4. **Day_001.md to Day_017.md** - Daily lesson content

---

## Quick Start Checklist

- [ ] Install Pandoc
- [ ] Install MiKTeX
- [ ] Restart PowerShell
- [ ] Navigate to project folder
- [ ] Run `.\Convert-MD-to-PDF.ps1`
- [ ] Check the `PDFs` folder for your converted files

---

## Support

If you encounter any issues:
1. Verify Pandoc is installed: `pandoc --version`
2. Verify MiKTeX is installed: `xelatex --version`
3. Check the error messages in the script output
4. Ensure you're running PowerShell (not Command Prompt)

---

**Created:** March 15, 2026  
**Repository:** https://github.com/gazalinawaz/365EnglishPractice.git
