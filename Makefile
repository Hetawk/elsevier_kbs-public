# Makefile for Knowledge-Based Systems (KBS) Paper
# Enhanced version with extraction and integration workflows

# Configuration
MAIN = main
ANONYMOUS = main_anonymous
INTEGRATED = main_integrated
SOURCE_PAPER = to_be_reference/full_tmi.tex
BIB = ref/references
EXTRACTED_DIR = extracted_sections_complete

# Python scripts
EXTRACT_SCRIPT = extract_complete.py
INTEGRATE_SCRIPT = integrate_kbs.py

# Default target - build main paper directly
all: main

# Build main paper directly (with complete content) - force rebuild
main:
	@echo "Building KBS paper (forced rebuild)..."
	pdflatex $(MAIN)
	-bibtex $(MAIN) 2>/dev/null || true
	pdflatex $(MAIN)
	pdflatex $(MAIN)
	@echo "Paper built: $(MAIN).pdf"

# Build PDF (alias for main target)
pdf: main

# Build anonymized paper for double-blind review - force rebuild
anonymous:
	@echo "Building anonymized KBS paper for double-blind review (forced rebuild)..."
	pdflatex $(ANONYMOUS)
	-bibtex $(ANONYMOUS) 2>/dev/null || true
	pdflatex $(ANONYMOUS)
	pdflatex $(ANONYMOUS)
	@echo "Anonymized paper built: $(ANONYMOUS).pdf"

# Build anonymized paper with dependency checking (only rebuild if needed)
anonymous-check: $(ANONYMOUS).pdf

$(ANONYMOUS).pdf: $(ANONYMOUS).tex
	@echo "Building anonymized KBS paper (dependency-based)..."
	pdflatex $(ANONYMOUS)
	-bibtex $(ANONYMOUS) 2>/dev/null || true
	pdflatex $(ANONYMOUS)
	pdflatex $(ANONYMOUS)
	@echo "Anonymized paper built: $(ANONYMOUS).pdf"

# Build main paper directly (alternative target name) - force rebuild
build:
	@echo "Building KBS paper (forced rebuild)..."
	pdflatex $(MAIN)
	-bibtex $(MAIN) 2>/dev/null || true
	pdflatex $(MAIN)
	pdflatex $(MAIN)
	@echo "Paper built: $(MAIN).pdf"

# Build main paper with dependency checking (only rebuild if needed)
main-check: $(MAIN).pdf

# Build template paper (basic KBS template) - force rebuild
template:
	@echo "Building KBS template paper (forced rebuild)..."
	pdflatex $(MAIN)
	-bibtex $(MAIN) 2>/dev/null || true
	pdflatex $(MAIN)
	pdflatex $(MAIN)
	@echo "Template paper built: $(MAIN).pdf"

$(MAIN).pdf: $(MAIN).tex
	@echo "Building KBS paper (dependency-based)..."
	pdflatex $(MAIN)
	-bibtex $(MAIN) 2>/dev/null || true
	pdflatex $(MAIN)
	pdflatex $(MAIN)
	@echo "Paper built: $(MAIN).pdf"

# Extract content from source IEEE paper
extract: $(EXTRACTED_DIR)

$(EXTRACTED_DIR): $(EXTRACT_SCRIPT) $(SOURCE_PAPER)
	@echo "Extracting content from IEEE TMI paper..."
	python3 $(EXTRACT_SCRIPT) $(SOURCE_PAPER)
	@echo "Content extracted to $(EXTRACTED_DIR)/"

# Build integrated paper (main target)
integrated: $(INTEGRATED).pdf

$(INTEGRATED).pdf: $(INTEGRATE_SCRIPT) $(EXTRACTED_DIR)
	@echo "Integrating extracted content into KBS template..."
	python3 $(INTEGRATE_SCRIPT)
	@echo "Building integrated KBS paper..."
	pdflatex $(INTEGRATED)
	-bibtex $(INTEGRATED) 2>/dev/null || true
	pdflatex $(INTEGRATED)
	pdflatex $(INTEGRATED)
	@echo "Integrated paper built: $(INTEGRATED).pdf"

# Force re-extraction and integration
rebuild: clean-extract integrated

# Build highlights document - force rebuild
highlights:
	@echo "Building highlights document (forced rebuild)..."
	pdflatex highlights
	@echo "Highlights built: highlights.pdf"

# Build highlights with dependency checking (only rebuild if needed)
highlights-check: highlights.pdf

highlights.pdf: highlights.tex
	@echo "Building highlights document (dependency-based)..."
	pdflatex highlights
	@echo "Highlights built: highlights.pdf"

# Build supporting documents for submission
supporting: author-agreement cover-letter declaration-interests
	@echo "All supporting documents built successfully!"

# Build author agreement document - force rebuild
author-agreement:
	@echo "Building author agreement document (forced rebuild)..."
	pdflatex author_agreement
	@echo "Author agreement built: author_agreement.pdf"

# Build author agreement with dependency checking
author-agreement-check: author_agreement.pdf

author_agreement.pdf: author_agreement.tex
	@echo "Building author agreement document (dependency-based)..."
	pdflatex author_agreement
	@echo "Author agreement built: author_agreement.pdf"

# Build cover letter document - force rebuild
cover-letter:
	@echo "Building cover letter document (forced rebuild)..."
	pdflatex cover_letter
	@echo "Cover letter built: cover_letter.pdf"

# Build cover letter with dependency checking
cover-letter-check: cover_letter.pdf

cover_letter.pdf: cover_letter.tex
	@echo "Building cover letter document (dependency-based)..."
	pdflatex cover_letter
	@echo "Cover letter built: cover_letter.pdf"

# Build declaration of interests document - force rebuild
declaration-interests:
	@echo "Building declaration of interests document (forced rebuild)..."
	pdflatex declaration_interests
	@echo "Declaration of interests built: declaration_interests.pdf"

# Build declaration of interests with dependency checking
declaration-interests-check: declaration_interests.pdf

declaration_interests.pdf: declaration_interests.tex
	@echo "Building declaration of interests document (dependency-based)..."
	pdflatex declaration_interests
	@echo "Declaration of interests built: declaration_interests.pdf"

# Build all submission documents (combined command)
submission-package: main anonymous highlights supporting
	@echo "Complete submission package built:"
	@echo "  ✓ main.pdf - Complete manuscript"
	@echo "  ✓ main_anonymous.pdf - Anonymized manuscript"
	@echo "  ✓ highlights.pdf - Research highlights"
	@echo "  ✓ author_agreement.pdf - Author agreement"
	@echo "  ✓ cover_letter.pdf - Cover letter"
	@echo "  ✓ declaration_interests.pdf - Declaration of interests"
	@echo "All documents ready for Knowledge-Based Systems submission!"

# View supporting documents
view-author-agreement: author_agreement.pdf
	open author_agreement.pdf

view-cover-letter: cover_letter.pdf
	open cover_letter.pdf

view-declaration-interests: declaration_interests.pdf
	open declaration_interests.pdf

# Quick compile without bibliography
quick:
	@echo "Quick compile of main paper..."
	pdflatex $(MAIN)

quick-main:
	@echo "Quick compile of main paper..."
	pdflatex $(MAIN)

quick-anonymous:
	@echo "Quick compile of anonymized paper..."
	pdflatex $(ANONYMOUS)

quick-integrated:
	@echo "Quick compile of integrated paper..."
	pdflatex $(INTEGRATED)

quick-template:
	@echo "Quick compile of template..."
	pdflatex $(MAIN)

# View PDFs (macOS)
view: $(INTEGRATED).pdf
	open $(INTEGRATED).pdf

view-main: $(MAIN).pdf
	open $(MAIN).pdf

view-anonymous: $(ANONYMOUS).pdf
	open $(ANONYMOUS).pdf

view-template: $(MAIN).pdf
	open $(MAIN).pdf

view-highlights: highlights.pdf
	open highlights.pdf

# Check paper status
status:
	@echo "=== KBS Paper Status ==="
	@echo "Main file: $(MAIN).tex"
	@echo "Anonymous file: $(ANONYMOUS).tex"
	@echo "Template file: $(MAIN).tex"
	@echo "Integrated file: $(INTEGRATED).tex"
	@echo "Source paper: $(SOURCE_PAPER)"
	@echo "Extracted sections directory: $(EXTRACTED_DIR)/"
	@echo
	@echo "Files:"
	@ls -la *.pdf 2>/dev/null || echo "No PDF files found"
	@echo
	@if [ -d "$(EXTRACTED_DIR)" ]; then \
		echo "Extracted sections ($(shell ls $(EXTRACTED_DIR) | wc -l) files):"; \
		ls -la $(EXTRACTED_DIR)/; \
	else \
		echo "No extracted sections found. Run 'make extract' first."; \
	fi

# Count pages in PDFs
pages:
	@echo "=== Page Counts ==="
	@for pdf in *.pdf; do \
		if [ -f "$$pdf" ]; then \
			if command -v pdfinfo > /dev/null 2>&1; then \
				pages=$$(pdfinfo "$$pdf" 2>/dev/null | grep Pages | awk '{print $$2}'); \
			elif command -v mdls > /dev/null 2>&1; then \
				pages=$$(mdls -name kMDItemNumberOfPages "$$pdf" 2>/dev/null | awk '{print $$3}'); \
			else \
				pages="unknown"; \
			fi; \
			echo "$$pdf: $$pages pages"; \
		fi; \
	done

# Validate paper meets KBS requirements
validate:
	@echo "=== KBS Journal Requirements Validation ==="
	@if [ -f "$(MAIN).pdf" ]; then \
		if command -v pdfinfo > /dev/null 2>&1; then \
			pages=$$(pdfinfo "$(MAIN).pdf" 2>/dev/null | grep Pages | awk '{print $$2}'); \
		elif command -v mdls > /dev/null 2>&1; then \
			pages=$$(mdls -name kMDItemNumberOfPages "$(MAIN).pdf" 2>/dev/null | awk '{print $$3}'); \
		else \
			pages="unknown"; \
		fi; \
		echo "✓ Paper: $(MAIN).pdf ($$pages pages)"; \
		if [ "$$pages" != "unknown" ] && [ "$$pages" != "" ] && [ $$pages -le 20 ]; then \
			echo "✓ Page limit: $$pages/20 pages (WITHIN LIMIT)"; \
		elif [ "$$pages" != "unknown" ] && [ "$$pages" != "" ]; then \
			echo "✗ Page limit: $$pages/20 pages (EXCEEDS LIMIT)"; \
		else \
			echo "? Page limit: Unable to determine page count"; \
		fi; \
	elif [ -f "$(INTEGRATED).pdf" ]; then \
		if command -v pdfinfo > /dev/null 2>&1; then \
			pages=$$(pdfinfo "$(INTEGRATED).pdf" 2>/dev/null | grep Pages | awk '{print $$2}'); \
		elif command -v mdls > /dev/null 2>&1; then \
			pages=$$(mdls -name kMDItemNumberOfPages "$(INTEGRATED).pdf" 2>/dev/null | awk '{print $$3}'); \
		else \
			pages="unknown"; \
		fi; \
		echo "✓ Paper: $(INTEGRATED).pdf ($$pages pages)"; \
		if [ "$$pages" != "unknown" ] && [ "$$pages" != "" ] && [ $$pages -le 20 ]; then \
			echo "✓ Page limit: $$pages/20 pages (WITHIN LIMIT)"; \
		elif [ "$$pages" != "unknown" ] && [ "$$pages" != "" ]; then \
			echo "✗ Page limit: $$pages/20 pages (EXCEEDS LIMIT)"; \
		else \
			echo "? Page limit: Unable to determine page count"; \
		fi; \
	else \
		echo "✗ No paper found. Run 'make main' or 'make integrated' first."; \
	fi
	@echo
	@if [ -f "$(MAIN).tex" ]; then \
		grep -q "highlights" $(MAIN).tex 2>/dev/null && echo "✓ Highlights section found" || echo "✗ Highlights section missing"; \
		grep -q "CRediT" $(MAIN).tex 2>/dev/null && echo "✓ CRediT section found" || echo "✗ CRediT section missing"; \
		grep -q "Declaration of competing interests" $(MAIN).tex 2>/dev/null && echo "✓ Competing interests declaration found" || echo "✗ Competing interests declaration missing"; \
		grep -q "Data availability" $(MAIN).tex 2>/dev/null && echo "✓ Data availability statement found" || echo "✗ Data availability statement missing"; \
	elif [ -f "$(INTEGRATED).tex" ]; then \
		grep -q "highlights" $(INTEGRATED).tex 2>/dev/null && echo "✓ Highlights section found" || echo "✗ Highlights section missing"; \
		grep -q "CRediT" $(INTEGRATED).tex 2>/dev/null && echo "✓ CRediT section found" || echo "✗ CRediT section missing"; \
		grep -q "Declaration of competing interests" $(INTEGRATED).tex 2>/dev/null && echo "✓ Competing interests declaration found" || echo "✗ Competing interests declaration missing"; \
		grep -q "Data availability" $(INTEGRATED).tex 2>/dev/null && echo "✓ Data availability statement found" || echo "✗ Data availability statement missing"; \
	fi

# Archive for submission
archive: $(MAIN).pdf $(ANONYMOUS).pdf
	@echo "Creating submission archive..."
	@mkdir -p kbs_submission
	@cp $(MAIN).tex kbs_submission/
	@cp $(MAIN).pdf kbs_submission/
	@cp $(ANONYMOUS).tex kbs_submission/
	@cp $(ANONYMOUS).pdf kbs_submission/
	@cp title_page.tex kbs_submission/ 2>/dev/null || true
	@cp -r fig/ kbs_submission/ 2>/dev/null || true
	@cp -r ref/ kbs_submission/ 2>/dev/null || true
	@cp highlights.pdf kbs_submission/ 2>/dev/null || true
	@cp SUBMISSION_GUIDE.md kbs_submission/ 2>/dev/null || true
	@tar -czf kbs_submission_$(shell date +%Y%m%d_%H%M%S).tar.gz kbs_submission/
	@echo "Submission archive created: kbs_submission_*.tar.gz"
	@rm -rf kbs_submission/

# Development workflow
dev: extract integrated validate
	@echo "=== Development Workflow Complete ==="
	@make status

# Clean auxiliary files
clean:
	@echo "Cleaning LaTeX auxiliary files..."
	rm -f *.aux *.bbl *.blg *.log *.out *.toc *.lof *.lot 
	rm -f *.fls *.fdb_latexmk *.synctex.gz *.nav *.snm *.vrb
	rm -f *.spl *.figlist *.makefile *.fls *.fdb_latexmk
	rm -f .DS_Store

# Clean extracted content
clean-extract:
	@echo "Cleaning extracted content..."
	rm -rf $(EXTRACTED_DIR)/
	rm -f figures_helper.tex

# Clean all generated files except source
clean-all: clean clean-extract
	@echo "Cleaning all generated files..."
	rm -f *.pdf
	rm -f $(INTEGRATED).tex
	rm -rf kbs_submission*/

# Help
help:
	@echo "KBS Paper Build System"
	@echo "====================="
	@echo
	@echo "Main Targets:"
	@echo "  all, main       - Build main KBS paper (forced rebuild)"
	@echo "  anonymous       - Build anonymized paper for double-blind review"
	@echo "  build           - Build main KBS paper (forced rebuild)"
	@echo "  pdf             - Build main KBS paper (alias for main)"
	@echo "  main-check      - Build main KBS paper (only if needed)"
	@echo "  anonymous-check - Build anonymized paper (only if needed)"
	@echo "  template        - Build basic KBS template (forced rebuild)"
	@echo "  integrated      - Build integrated KBS paper (via extraction)"
	@echo "  extract         - Extract content from IEEE source"
	@echo "  highlights      - Build highlights document (forced rebuild)"
	@echo "  highlights-check - Build highlights document (only if needed)"
	@echo
	@echo "Supporting Documents:"
	@echo "  supporting      - Build all supporting documents"
	@echo "  author-agreement - Build author agreement document"
	@echo "  cover-letter    - Build cover letter document"
	@echo "  declaration-interests - Build declaration of interests document"
	@echo "  submission-package - Build complete submission package"
	@echo
	@echo "Development:"
	@echo "  dev             - Full development workflow (integrated)"
	@echo "  rebuild         - Force re-extraction and rebuild"
	@echo "  quick           - Quick compile main paper (no bibtex)"
	@echo "  quick-main      - Quick compile main paper (no bibtex)"
	@echo "  quick-anonymous - Quick compile anonymized paper (no bibtex)"
	@echo
	@echo "Utilities:"
	@echo "  status          - Show paper status and files"
	@echo "  pages           - Count pages in PDFs"
	@echo "  validate        - Check KBS requirements"
	@echo "  view            - Open integrated paper"
	@echo "  view-main       - Open main paper"
	@echo "  view-anonymous  - Open anonymized paper"
	@echo "  archive         - Create submission archive"
	@echo
	@echo "Cleaning:"
	@echo "  clean           - Remove auxiliary files"
	@echo "  clean-extract   - Remove extracted content"
	@echo "  clean-all       - Remove all generated files"
	@echo
	@echo "Files:"
	@echo "  Main: $(MAIN).tex"
	@echo "  Anonymous: $(ANONYMOUS).tex"
	@echo "  Source: $(SOURCE_PAPER)"
	@echo "  Template: $(MAIN).tex"
	@echo "  Integrated: $(INTEGRATED).tex"
	@echo "  Extracted: $(EXTRACTED_DIR)/"

# Prevent deletion of intermediate files
.PRECIOUS: $(EXTRACTED_DIR) $(INTEGRATED).tex

# Declare phony targets
.PHONY: all main anonymous build main-check anonymous-check template integrated extract rebuild highlights quick quick-main quick-anonymous quick-template pdf
.PHONY: view view-main view-anonymous view-template view-highlights status pages validate archive dev
.PHONY: clean clean-extract clean-all help
