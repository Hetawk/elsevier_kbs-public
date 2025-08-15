# Paper Adaptation Guide: IEEE TMI to Elsevier KBS

## ✅ Template Status

Your `main.tex` is now based on the **official Elsevier `elsarticle` template** exactly as provided by the journal, with:

- Correct document class: `\documentclass[preprint,12pt]{elsarticle}`
- Proper frontmatter structure with title, authors, affiliations
- Required sections: highlights, abstract, keywords
- All mandatory end sections: acknowledgments, CRediT, funding, competing interests, data availability
- Correct reference style: `elsarticle-num`

## 📁 Content Extraction

The `extract_content.py` script has extracted key sections from your TMI paper:

```
extracted_sections/
├── abstract.tex         # Your abstract (already adapted)
├── keywords.tex         # Keywords converted to KBS format
├── introduction.tex     # Introduction section
├── related_work.tex     # Related work section
└── methodology.tex      # Methodology section
```

## 🔄 Key Format Differences: IEEE TMI → Elsevier KBS

### Document Structure

| IEEE TMI                             | Elsevier KBS                                |
| ------------------------------------ | ------------------------------------------- |
| `\documentclass[journal]{ieeecolor}` | `\documentclass[preprint,12pt]{elsarticle}` |
| `\begin{IEEEkeywords}`               | `\begin{keyword}` with `\sep` separators    |
| `\IEEEPARstart{D}{eep}`              | Just start with "Deep" normally             |
| `\cite{ref}`                         | `~\cite{ref}` (with space)                  |

### Required Sections for KBS

✅ Already included in your `main.tex`:

- **CRediT author contributions** (mandatory)
- **Declaration of competing interests** (mandatory)
- **Data availability statement** (mandatory)
- **Funding statement** (mandatory)
- **Highlights** (optional but recommended)

### Page Limit Compliance

- **Target**: 20 double-spaced pages maximum
- **Current TMI paper**: ~796 lines → likely exceeds limit
- **Action needed**: Condense content, focus on key contributions

## 🚀 Next Steps

### 1. Adapt Content (Priority Order)

```bash
# Review extracted sections
ls -la extracted_sections/

# Start with these files:
1. extracted_sections/abstract.tex     # ✅ Already adapted
2. extracted_sections/introduction.tex # Adapt and shorten
3. extracted_sections/methodology.tex  # Core contribution - keep detailed
4. extracted_sections/related_work.tex # Condense significantly
```

### 2. Content Adaptation Checklist

- [ ] **Abstract**: ✅ Already done (248 words, under 250 limit)
- [ ] **Keywords**: ✅ Already formatted with `\sep`
- [ ] **Introduction**: Shorten by ~30%, remove IEEE-specific content
- [ ] **Related Work**: Condense to 1-2 pages maximum
- [ ] **Methodology**: Keep detailed - this is your core contribution
- [ ] **Experiments**: Adapt from TMI format, ensure figures work
- [ ] **Results**: Focus on key findings, reduce table count if needed
- [ ] **Conclusion**: Shorten to 1 page

### 3. Technical Adaptations Needed

- [ ] Replace `\IEEEPARstart` with normal text
- [ ] Convert IEEE table/figure formatting to standard LaTeX
- [ ] Update references from IEEE style to Elsevier numbered style
- [ ] Remove IEEE-specific packages and commands
- [ ] Ensure all figures are in `fig/` directory with correct paths

### 4. KBS-Specific Adaptations

- [ ] Emphasize **knowledge-based systems** aspects
- [ ] Highlight **AI decision-making** applications
- [ ] Connect to **data science methodologies**
- [ ] Frame as **intelligent system** for healthcare

### 5. Validation Steps

```bash
# Test compilation frequently
make quick

# Full build with references
make pdf

# Check page count (target: ≤20 pages)
make view
```

## 📋 Content Priority for Page Reduction

### Keep Detailed (Core Contributions)

1. **DAAM Architecture** - Your main innovation
2. **Experimental Results** - Validation of approach
3. **Medical Domain Applications** - Clinical relevance

### Condense Significantly

1. **Related Work** - Reduce by 50-60%
2. **Background Theory** - Keep only essential concepts
3. **Implementation Details** - Move to supplementary if needed

### Consider Removing/Moving

1. **Extensive literature review** - Keep most relevant only
2. **Detailed mathematical proofs** - Summarize key equations
3. **Redundant experimental details** - Keep core experiments

## 🎯 KBS Journal Fit

Your paper fits KBS perfectly because it addresses:

- ✅ **Machine learning methodology** (DAAM)
- ✅ **Knowledge-based computer vision** (medical imaging)
- ✅ **Intelligent decision support systems** (diagnostic assistance)
- ✅ **Data science methodologies** (adversarial defense)

## 🔧 Quick Start Commands

```bash
# View extracted content
cat extracted_sections/introduction.tex

# Edit main paper
code main.tex  # or your preferred editor

# Test compilation
make quick

# Full build
make pdf && make view
```

Your template is now journal-compliant and ready for content adaptation!
