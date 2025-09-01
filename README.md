# MedDef Paper

This repository contains the LaTeX source for "MedDef: An Efficient Self-Attention Model for Adversarial Resilience in Medical Imaging with Unstructured Pruning" - a research paper submitted to Knowledge-Based Systems journal.

## 🔗 **Public Repository Access**

> **📂 Complete Project Download:**  
> **🌐 [https://github.com/Hetawk/elsevier_kbs-public.git](https://github.com/Hetawk/elsevier_kbs-public.git)**
>
> **Quick Clone:**
>
> ```bash
> git clone https://github.com/Hetawk/elsevier_kbs-public.git
> cd elsevier_kbs-public
> make main  # Build the paper
> ```

## 📁 Project Structure

```
├── main.tex                    # Main manuscript (with author information)
├── main_anonymous.tex          # Anonymous version for double-blind review
├── author_agreement.tex        # Author agreement document
├── cover_letter.tex           # Cover letter for submission
├── declaration_interests.tex   # Declaration of interests
├── highlights.tex             # Research highlights
├── title_page.tex             # Title page template
├── ref/
│   └── references.bib         # Bibliography database
├── fig/                       # Figures and images
│   ├── fig1_a.png            # Dataset samples
│   ├── fig1_b.png
│   ├── fig2.jpg              # Model architecture
│   ├── fig3.jpg              # Adversarial training
│   ├── fig4.jpg              # Pruning process
│   ├── class_distribution_*.png
│   ├── per-class/            # Per-class performance metrics
│   ├── cm/                   # Confusion matrices
│   ├── asr-prunning/         # Attack success rate vs pruning
│   ├── saliency_map/         # Saliency visualizations
│   └── author/               # Author photos
└── to_be_reference/          # Reference materials (not for submission)
```

## 🔧 Build Commands

### Main Paper Compilation

```bash
# Build main manuscript with full author information
make main
# or
make pdf

# Build anonymous version for double-blind review
make anonymous

# Build both versions sequentially
make clean && make pdf && make anonymous
```

### Supporting Documents

```bash
# Build author agreement
make author_agreement

# Build cover letter
make cover_letter

# Build declaration of interests
make declaration_interests

# Build highlights document
make highlights

# Build all documents (main + supporting)
make all
```

### Utility Commands

```bash
# Clean auxiliary files
make clean

# Force clean rebuild of main paper
make clean && make pdf

# Complete workflow: clean → build main → build anonymous → clean
make clean && make pdf && make anonymous && make clean
```

## 📄 Document Descriptions

### Main Documents

- **`main.pdf`** (30 pages): Complete manuscript with author information, hyperref navigation, and PDF bookmarks
- **`main_anonymous.pdf`** (28 pages): Anonymized version for double-blind peer review
- **`author_agreement.pdf`**: Signed author agreement with ORCID IDs
- **`cover_letter.pdf`**: Professional cover letter for journal submission
- **`declaration_interests.pdf`**: Declaration of competing interests
- **`highlights.pdf`**: Research highlights summary

### Key Features

- ✅ **Enhanced Navigation**: PDF bookmarks and clickable hyperlinks
- ✅ **URL Optimization**: Proper line breaking for long URLs using `xurl` package
- ✅ **Professional Formatting**: Elsevier article class with proper citation style
- ✅ **Complete Visualizations**: All figures including per-class performance metrics
- ✅ **Author Credentials**: ORCID IDs integrated in author agreement and cover letter

## 🚀 Quick Start

1. **Complete Build Workflow**:

   ```bash
   make clean && make main && make anonymous && make clean

   make clean && make pdf && make anonymous && make clean
   ```

2. **Individual Document Build**:

   ```bash
   make main           # Main manuscript
   make anonymous      # Anonymous version
   make author_agreement  # Author agreement
   make cover_letter   # Cover letter
   make declaration_interests  # Declaration of interests
   make highlights     # Research highlights
   ```

3. **Development Workflow**:
   ```bash
   make clean          # Clean auxiliary files
   make main           # Build and check main document
   # Edit files as needed
   make anonymous      # Build anonymous version
   ```

## 📊 Document Statistics

- **Main manuscript**: 30 pages, ~1.2MB
- **Anonymous version**: 28 pages, ~760KB
- **Bibliography**: 50+ references in BibTeX format
- **Figures**: 8 main figures + class distribution + per-class metrics

## 📊 Data Availability

This study utilized two publicly available datasets for medical image classification tasks:

1. **Retinal OCT Images (optical coherence tomography)**  
   Available from Kermany et al. (2018) via Kaggle:  
   🔗 [https://www.kaggle.com/datasets/paultimothymooney/kermany2018](https://www.kaggle.com/datasets/paultimothymooney/kermany2018)

2. **Chest X-Ray Images (Pneumonia)**  
   Available via Kaggle:  
   🔗 [https://www.kaggle.com/datasets/paultimothymooney/chest-xray-pneumonia](https://www.kaggle.com/datasets/paultimothymooney/chest-xray-pneumonia)

### 💻 Source Code Availability

The complete implementation of the MedDef model and experimental code is available at:  
🔗 [https://github.com/Hetawk/meddef1.git](https://github.com/Hetawk/meddef1.git)

**Quick Setup:**

```bash
git clone https://github.com/Hetawk/meddef1.git
cd meddef1
# Follow setup instructions in the code repository
```

## 🔍 Technical Details

### LaTeX Packages Used

- `elsarticle`: Elsevier journal article class
- `hyperref`: PDF navigation and bookmarks with `breaklinks=true`
- `xurl`: Enhanced URL breaking for long links
- `natbib`: Citation management
- `subcaption`: Subfigure support
- `microtype`: Typography optimization

### Build System

- **Make-based**: Uses Makefile for automated builds
- **Multi-pass**: Automatic BibTeX and cross-reference resolution
- **Clean builds**: Removes auxiliary files for fresh compilation

## 📝 File Conventions

- **Main source**: `main.tex` (with authors)
- **Anonymous**: `main_anonymous.tex` (without author info)
- **Bibliography**: `ref/references.bib`
- **Figures**: `fig/` directory with organized subdirectories
- **Output**: PDF files generated in root directory

## 🛠️ Troubleshooting

### Common Issues

1. **Compilation errors**: Run `make clean` before rebuilding
2. **Missing figures**: Ensure all figure files exist in `fig/` directory
3. **Bibliography issues**: Check `ref/references.bib` for syntax errors
4. **URL overflow**: URLs now properly break with `xurl` package

### Make Targets

```bash
make clean          # Remove auxiliary files
make main           # Build main.pdf
make anonymous      # Build main_anonymous.pdf
make author_agreement  # Build author_agreement.pdf
make cover_letter   # Build cover_letter.pdf
make declaration_interests  # Build declaration_interests.pdf
make highlights     # Build highlights.pdf
make all           # Build all documents
```

## 📚 Submission Package

For journal submission, the complete package includes:

- `main.pdf` - Main manuscript with navigation
- `main_anonymous.pdf` - Anonymous version for review
- `author_agreement.pdf` - Signed author agreement
- `cover_letter.pdf` - Cover letter with author credentials
- `declaration_interests.pdf` - Declaration of competing interests
- `highlights.pdf` - Research highlights
- Source files and bibliography

## 🔄 Version Control

This project uses Git for version control. All major manuscript versions are tracked with proper commit messages for revision history.

---

**Contact**: For questions about the build system or document structure, refer to the corresponding author information in the manuscript.
