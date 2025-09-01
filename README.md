# Knowledge-Based Systems (KBS) Journal Paper

This repository contains the LaTeX source for a research paper submission to Knowledge-Based Systems journal, featuring a complete workflow for double-blind review preparation.

## Paper Versions

### Main Files

- **`main.tex`** - Complete manuscript with full author information for final publication
- **`main_anonymous.tex`** - Anonymized manuscript for double-blind review (NO author info)
- **`title_page.tex`** - Separate title page with author information for submission
- **`ref/references.bib`** - Bibliography database

### Requirements Files

- **`SUBMISSION_GUIDE.md`** - Comprehensive submission checklist and requirements

## Quick Start

### Build Main Paper (Complete Version)

```bash
make main
# or
make pdf
```

### Build Anonymous Paper (Double-Blind Review)

```bash
make anonymous
```

### Build Both Versions

```bash
make main && make anonymous
```

## Makefile Commands

### Main Build Commands

- `make main` or `make pdf` - Build complete paper with author information
- `make anonymous` - Build anonymized paper for double-blind review
- `make build` - Alternative command to build main paper
- `make template` - Build basic KBS template

### Quick Compilation (No Bibliography)

- `make quick` - Quick compile main paper
- `make quick-main` - Quick compile main paper
- `make quick-anonymous` - Quick compile anonymous paper

### Dependency-Based Building (Only Rebuild if Needed)

- `make main-check` - Build main paper only if source changed
- `make anonymous-check` - Build anonymous paper only if source changed

### Viewing PDFs

- `make view-main` - Open main paper PDF
- `make view-anonymous` - Open anonymous paper PDF
- `make view` - Open integrated paper PDF

### Utilities

- `make status` - Show paper status and available files
- `make pages` - Count pages in all PDF files
- `make validate` - Check if paper meets KBS journal requirements
- `make archive` - Create submission archive with all files

### Cleaning

- `make clean` - Remove LaTeX auxiliary files
- `make clean-all` - Remove all generated files including PDFs

### Help

- `make help` - Show all available commands

## File Structure

```
├── main.tex                    # Complete manuscript (with authors)
├── main_anonymous.tex          # Anonymous manuscript (double-blind)
├── title_page.tex             # Title page with author info
├── SUBMISSION_GUIDE.md        # Submission requirements checklist
├── Makefile                   # Build automation
├── README.md                  # This file
├── ref/
│   └── references.bib         # Bibliography database
└── fig/                       # Figures directory
    ├── fig1_a.png
    ├── fig1_b.png
    ├── fig2.jpg
    ├── fig3.jpg
    └── fig4.jpg
```

## Double-Blind Review Submission

Knowledge-Based Systems requires double-blind review. Use these commands:

1. **Build anonymous version**: `make anonymous`
2. **Verify anonymization**: Check that no author information appears in `main_anonymous.pdf`
3. **Build complete archive**: `make archive`

The anonymous version automatically:

- Removes all author information from front matter
- Comments out acknowledgments section
- Removes Declaration of Interests details
- Maintains all technical content

## Development Workflow

### Standard Workflow

```bash
# Edit main.tex (complete version)
# Copy changes to main_anonymous.tex (remove author info)
make main && make anonymous
```

### Quick Testing

```bash
# Quick compile for testing
make quick-anonymous
```

### Validation

```bash
# Check paper requirements
make validate
```

### Submission Preparation

```bash
# Create complete submission package
make archive
```

## Journal Requirements (KBS)

The paper automatically includes required sections:

- ✅ Abstract (max 250 words)
- ✅ Research Highlights (5-7 bullet points)
- ✅ Keywords (1-7 keywords)
- ✅ Data Availability Statement
- ✅ Declaration of Interests
- ✅ Proper citation format (elsarticle-num style)

Use `make validate` to check compliance.

## Troubleshooting

### Common Issues

**Bibliography not showing:**

```bash
make clean && make main
```

**Anonymous version has author info:**

- Edit `main_anonymous.tex` to remove author identification
- Check front matter, acknowledgments, and funding sections

**PDF not opening:**

```bash
# Check if PDF was created successfully
ls -la *.pdf
```

### Build Process

The Makefile runs this sequence:

1. `pdflatex filename`
2. `bibtex filename` (if .bib file exists)
3. `pdflatex filename` (twice for cross-references)

## Paper Status

Check current status:

```bash
make status
```

This shows:

- Available source files
- Generated PDF files
- Build timestamps
- File sizes

## Archive Creation

For journal submission:

```bash
make archive
```

Creates timestamped archive containing:

- `main.tex` and `main.pdf` (complete version)
- `main_anonymous.tex` and `main_anonymous.pdf` (anonymous version)
- `title_page.tex` (author information)
- `ref/` directory (bibliography)
- `fig/` directory (figures)
- `SUBMISSION_GUIDE.md` (requirements checklist)

## Dependencies

### Required LaTeX Packages

- `elsarticle` (journal class)
- `amssymb, amsmath` (mathematics)
- `algorithmic` (algorithms)
- `multirow` (tables)
- `url` (URLs)
- `subcaption` (subfigures)
- `microtype` (typography)

### System Requirements

- LaTeX distribution (TeXLive, MikTeX, etc.)
- `pdflatex` command
- `bibtex` command
- `make` utility (for Makefile)

## Contact

For issues with this build system, check:

1. `make help` - Available commands
2. `make status` - Current file status
3. `make validate` - Journal compliance check

For LaTeX issues with elsarticle class:

- Documentation: `doc/elsdoc.pdf`
- Support: elsarticle@stmdocs.in
