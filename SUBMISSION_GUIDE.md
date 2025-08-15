# Knowledge-Based Systems Submission Guide

## Quick Summary

- **Page Limit**: 20 double-spaced pages for research papers, 10 for short communications
- **Template**: Use `main.tex` (based on elsarticle template)
- **Reference style**: Numbered references with square brackets [1]
- **Figure format**: High-resolution separate files (≥300 dpi for photos, ≥1000 dpi for line art)

## Journal Scope

Knowledge-Based Systems focuses on AI research including:

- Machine learning theory, methodology and algorithms
- Data science theory and techniques
- Knowledge presentation and engineering
- Recommender systems and personalization
- Intelligent decision support systems
- Computational Intelligence systems
- Data-driven optimization
- Brain-computer interfaces
- Knowledge-based computer vision

## Required Sections

### Frontmatter

1. **Title** - Concise and informative
2. **Authors & Affiliations** - Full names, complete addresses
3. **Abstract** - Max 250 words, no references
4. **Keywords** - 1-7 keywords in English

### Optional but Recommended

5. **Highlights** - 3-5 bullet points, max 85 characters each

### End Matter

6. **Acknowledgments**
7. **CRediT Author Contributions** (Required)
8. **Funding Statement** (Required)
9. **Declaration of Competing Interests** (Required)
10. **Data Availability Statement** (Required)

## File Structure Created

```
/Users/ekd/Documents/coding_env/latex/ekd_papers/elsevier_kbs/
├── main.tex          # Main manuscript file
├── highlights.tex     # Highlights file (optional)
├── Makefile          # Build automation
├── fig/              # All figures (copied from your work)
├── ref/              # Bibliography files
└── elsarticle-*      # Template files
```

## Build Commands

- `make pdf` - Full build with bibliography
- `make quick` - Quick compile without bibtex
- `make view` - Build and open PDF
- `make clean` - Remove auxiliary files

## Figure Requirements

- **Photos/Screenshots**: TIFF, JPG, PNG ≥300 dpi
- **Charts/Graphs**: TIFF, JPG, PNG ≥1000 dpi or vector (EPS/PDF)
- **Minimum width**: 1063 pixels (single column), 2244 pixels (full width)
- **Naming**: Figure_1.png, Figure_2.png, etc.
- **Captions**: Required for all figures

## Reference Format

Use numbered style with DOIs when available:

```
[1] J. Author, Title, Journal 123 (2020) 45-67. https://doi.org/10.1016/...
```

## Submission Process

1. **Initial**: Submit PDF version
2. **If accepted**: Provide LaTeX source files bundled in archive
3. **Include**: All .tex, .bib, .bst, figure files, any custom packages

## Next Steps

1. Adapt your existing content from `to_be_reference/` to the `main.tex` template
2. Ensure figures meet resolution requirements
3. Write highlights (optional but recommended)
4. Complete all required declarations
5. Build and review PDF
6. Submit via journal's online system

## Key Reminders

- Single anonymized review process
- Use inclusive language throughout
- Declare any AI assistance in writing
- Ensure data availability or explain why not possible
- Follow ethical guidelines for research involving humans/animals
