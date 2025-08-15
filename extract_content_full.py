#!/usr/bin/env python3
"""
Comprehensive script to extract all sections from IEEE TMI format to Elsevier KBS format
This script extracts the complete content from your TMI paper for adaptation.
"""

import re
import sys
import os


def extract_sections_from_tmi(file_path):
    """Extract comprehensive sections from the TMI paper for adaptation"""

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Error: Could not find file {file_path}")
        return

    # Define comprehensive section patterns to extract
    sections = {
        'abstract': r'\\begin{abstract}(.*?)\\end{abstract}',
        'keywords': r'\\begin{IEEEkeywords}(.*?)\\end{IEEEkeywords}',
        'introduction': r'\\section{Introduction}\\label{sec:introduction}(.*?)(?=\\section)',
        'related_work': r'\\section{Related Work}\\label{sec:related_work}(.*?)(?=\\section)',
        'methodology': r'\\section{Methodology}\\label{sec:methodology}(.*?)(?=\\section)',
        'results': r'\\section{Results and Discussion}\\label{sec:results}(.*?)(?=\\section)',
        'challenges_conclusion': r'\\section{Challenges, Future Perspectives, and Conclusion}\\label{sec:challenges}(.*?)(?=\\pdfbookmark|\\bibliographystyle)',
        'acknowledgments': r'\\section\*{Acknowledgment}(.*?)(?=\\bibliographystyle)',
        'funding_info': r'\\thanks{The date for submission.*?}',
        'author_affiliations': r'(\\thanks{E\. K\. Dongbo.*?}.*?\\thanks{J\. N\. Kofa.*?})',
        'title': r'\\title{([^}]+)}',
        'complete_daam_section': r'\\subsection{Defense-Aware Attention Mechanism \(DAAM\)}(.*?)(?=\\subsection{Unstructured Pruning})',
        'contributions': r'Our contributions include:(.*?)(?=\\section)',
        'challenges_three': r'Three critical challenges emerge in medical imaging defense(.*?)(?=To tackle adversarial vulnerabilities)',
        'attack_methods': r'\\subsection{Attack Methods}(.*?)(?=\\section)',
        'unstructured_pruning': r'\\subsection{Unstructured Pruning}(.*?)(?=\\subsection)',
        'parameter_settings': r'\\subsection{Parameter Settings}(.*?)(?=\\section)',
        'ablation_study': r'\\subsection{Comprehensive Ablation Study Analysis}(.*?)(?=\\subsection)',
        'sota_comparison': r'\\subsection{State-of-the-Art Comparison}(.*?)(?=\\subsection)',
    }

    extracted = {}

    for section_name, pattern in sections.items():
        match = re.search(pattern, content, re.DOTALL)
        if match:
            if section_name == 'title':
                extracted[section_name] = match.group(1).strip()
            else:
                extracted[section_name] = match.group(1).strip(
                ) if match.group(1) else match.group(0).strip()
        else:
            extracted[section_name] = f"Section {section_name} not found"

    # Extract all figures separately
    figures = re.findall(
        r'(\\begin{figure}.*?\\end{figure})', content, re.DOTALL)
    tables = re.findall(r'(\\begin{table}.*?\\end{table})', content, re.DOTALL)
    equations = re.findall(
        r'(\\begin{equation}.*?\\end{equation}|\\begin{align}.*?\\end{align})', content, re.DOTALL)

    # Clean up IEEE-specific formatting
    def clean_ieee_formatting(text):
        if isinstance(text, list):
            return [clean_ieee_formatting(item) for item in text]

        # Convert IEEE references to Elsevier format
        text = re.sub(r'\\cite{([^}]+)}', r'~\\cite{\1}', text)

        # Remove IEEE-specific commands
        text = re.sub(r'\\IEEEPARstart{([^}]+)}{([^}]+)}', r'\1\2', text)
        text = re.sub(r'\\IEEEmembership{[^}]*}', '', text)

        # Convert IEEE keywords format
        if 'IEEEkeywords' in text:
            text = text.replace('\\begin{IEEEkeywords}', '').replace(
                '\\end{IEEEkeywords}', '')
            text = re.sub(r',\s*', r' \\sep ', text.strip())

        # Fix figure references for Elsevier format
        text = re.sub(r'Fig~\\ref{([^}]+)}', r'Figure~\\ref{\1}', text)
        text = re.sub(r'Fig\.~\\ref{([^}]+)}', r'Figure~\\ref{\1}', text)

        return text

    # Process and save sections
    output_dir = "extracted_sections_full"
    os.makedirs(output_dir, exist_ok=True)

    # Save main sections
    for section_name, section_content in extracted.items():
        cleaned_content = clean_ieee_formatting(section_content)

        output_file = f"{output_dir}/{section_name}.tex"
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(f"% Extracted {section_name} section\n")
            f.write(f"% Converted from IEEE TMI to Elsevier KBS format\n\n")
            f.write(str(cleaned_content))

        print(f"Extracted {section_name} -> {output_file}")

    # Save figures, tables, equations separately
    for name, items in [('figures', figures), ('tables', tables), ('equations', equations)]:
        if items:
            output_file = f"{output_dir}/{name}.tex"
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(f"% Extracted {name}\n")
                f.write(f"% Found {len(items)} items\n\n")
                for i, item in enumerate(items):
                    cleaned_item = clean_ieee_formatting(item)
                    f.write(f"% {name.capitalize()} {i+1}\n")
                    f.write(str(cleaned_item))
                    f.write("\n\n")
            print(f"Extracted {len(items)} {name} -> {output_file}")

    # Create a comprehensive summary
    summary_file = f"{output_dir}/EXTRACTION_SUMMARY.md"
    with open(summary_file, 'w', encoding='utf-8') as f:
        f.write("# Comprehensive Content Extraction Summary\n\n")
        f.write(f"## Title\n{extracted.get('title', 'Not found')}\n\n")

        f.write("## Abstract Analysis\n")
        abstract_text = extracted.get('abstract', '')
        word_count = len(abstract_text.split(
        )) if abstract_text != 'Section abstract not found' else 0
        f.write(f"- Word count: {word_count} words (KBS limit: 250 words)\n")
        f.write(
            f"- Status: {'✅ Within limit' if word_count <= 250 else '❌ Exceeds limit - needs condensing'}\n\n")

        f.write("## Keywords Analysis\n")
        keywords = extracted.get('keywords', 'Not found')
        if keywords != 'Section keywords not found':
            keyword_list = [k.strip()
                            for k in keywords.replace('\\sep', ',').split(',')]
            f.write(
                f"- Count: {len(keyword_list)} keywords (KBS limit: 1-7)\n")
            f.write(
                f"- Status: {'✅ Within limit' if 1 <= len(keyword_list) <= 7 else '❌ Outside limit'}\n")
            f.write("- Keywords:\n")
            for i, kw in enumerate(keyword_list, 1):
                f.write(f"  {i}. {kw}\n")
        f.write("\n")

        f.write("## Content Breakdown\n")
        for section, content in extracted.items():
            if section in ['title', 'abstract', 'keywords']:
                continue
            status = "✅ Found" if content != f"Section {section} not found" else "❌ Not found"
            if content != f"Section {section} not found":
                word_count = len(str(content).split())
                status += f" ({word_count} words)"
            f.write(f"- {section.replace('_', ' ').title()}: {status}\n")

        f.write(f"\n## Visual Elements\n")
        f.write(f"- Figures: {len(figures)} found\n")
        f.write(f"- Tables: {len(tables)} found\n")
        f.write(f"- Equations: {len(equations)} found\n\n")

        f.write("## Adaptation Priority (for 20-page limit)\n")
        f.write("### High Priority (Keep Detailed)\n")
        f.write("- DAAM Architecture (core innovation)\n")
        f.write("- Experimental Results (validation)\n")
        f.write("- Medical Domain Applications\n\n")

        f.write("### Medium Priority (Condense)\n")
        f.write("- Methodology (keep essential)\n")
        f.write("- Introduction (reduce by 30%)\n")
        f.write("- Parameter Settings\n\n")

        f.write("### Low Priority (Significantly Reduce)\n")
        f.write("- Related Work (reduce by 50-60%)\n")
        f.write("- Challenges section (summarize)\n")
        f.write("- Some ablation details\n\n")

        f.write("## KBS Journal Fit\n")
        f.write("✅ Perfect fit - addresses:\n")
        f.write("- Machine learning methodology (DAAM)\n")
        f.write("- Knowledge-based computer vision (medical imaging)\n")
        f.write("- Intelligent decision support systems (diagnostic assistance)\n")
        f.write("- Data science methodologies (adversarial defense)\n")

    print(f"\n🎉 Comprehensive extraction complete!")
    print(f"📁 Output directory: {output_dir}/")
    print(f"📋 Summary: {summary_file}")
    print("\n🚀 Next steps:")
    print("1. Review EXTRACTION_SUMMARY.md for complete overview")
    print("2. Start with high-priority sections for main.tex")
    print("3. Condense content to meet 20-page KBS limit")
    print("4. Emphasize knowledge-based systems aspects")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 extract_content_full.py <path_to_tmi_file>")
        print("Example: python3 extract_content_full.py to_be_reference/full_tmi.tex")
        sys.exit(1)

    extract_sections_from_tmi(sys.argv[1])
