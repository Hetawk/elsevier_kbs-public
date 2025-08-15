#!/usr/bin/env python3
"""
Fixed comprehensive extraction script for TMI to KBS conversion
"""

import re
import sys
import os


def extract_sections_from_tmi(file_path):
    """Extract comprehensive sections from the TMI paper"""

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Error: Could not find file {file_path}")
        return

    # Define section patterns - simplified for robustness
    sections = {
        'abstract': (r'\\begin{abstract}(.*?)\\end{abstract}', 1),
        'keywords': (r'\\begin{IEEEkeywords}(.*?)\\end{IEEEkeywords}', 1),
        'title': (r'\\title{([^}]+)}', 1),
        'introduction': (r'\\section{Introduction}\\label{sec:introduction}(.*?)(?=\\section{Related Work})', 1),
        'related_work': (r'\\section{Related Work}.*?(Recent research.*?)(?=\\section)', 1),
        'methodology': (r'\\section{Methodology}.*?(This section.*?)(?=\\section)', 1),
        'results': (r'\\section{Results and Discussion}.*?(This section presents.*?)(?=\\section)', 1),
        'daam_complete': (r'\\subsection{Defense-Aware Attention Mechanism.*?}(.*?)(?=\\subsection{Unstructured Pruning})', 1),
        'contributions': (r'(Our contributions include:.*?)(?=\\section)', 1),
        'three_challenges': (r'(Three critical challenges emerge.*?)(?=To tackle adversarial vulnerabilities)', 1),
        'conclusion': (r'\\subsection{Conclusion}(.*?)(?=\\pdfbookmark)', 1),
        'acknowledgments': (r'\\section\*{Acknowledgment}(.*?)(?=\\bibliographystyle)', 1),
        'funding_thanks': (r'(\\thanks{The date for submission.*?})', 1),
    }

    extracted = {}

    for section_name, (pattern, group_num) in sections.items():
        match = re.search(pattern, content, re.DOTALL)
        if match and len(match.groups()) >= group_num:
            extracted[section_name] = match.group(group_num).strip()
        else:
            extracted[section_name] = f"Section {section_name} not found"

    # Extract figures, tables, equations
    figures = re.findall(
        r'(\\begin{figure\*?}.*?\\end{figure\*?})', content, re.DOTALL)
    tables = re.findall(
        r'(\\begin{table\*?}.*?\\end{table\*?})', content, re.DOTALL)
    equations = re.findall(
        r'(\\begin{equation}.*?\\end{equation}|\\begin{align}.*?\\end{align})', content, re.DOTALL)

    def clean_ieee_formatting(text):
        """Clean IEEE-specific formatting for Elsevier"""
        if isinstance(text, list):
            return [clean_ieee_formatting(item) for item in text]

        # Convert IEEE references to Elsevier format
        text = re.sub(r'\\cite{([^}]+)}', r'~\\cite{\1}', text)

        # Remove IEEE-specific commands
        text = re.sub(r'\\IEEEPARstart{([^}]+)}{([^}]+)}', r'\1\2', text)
        text = re.sub(r'\\IEEEmembership{[^}]*}', '', text)

        # Convert keywords
        if 'IEEEkeywords' in text:
            text = text.replace('\\begin{IEEEkeywords}', '').replace(
                '\\end{IEEEkeywords}', '')
            text = re.sub(r',\s*', r' \\sep ', text.strip())

        # Fix figure references
        text = re.sub(r'Fig~\\ref{([^}]+)}', r'Figure~\\ref{\1}', text)
        text = re.sub(r'Fig\.~\\ref{([^}]+)}', r'Figure~\\ref{\1}', text)

        return text

    # Create output directory
    output_dir = "extracted_sections_complete"
    os.makedirs(output_dir, exist_ok=True)

    # Save all extracted sections
    for section_name, content_text in extracted.items():
        if content_text != f"Section {section_name} not found":
            cleaned_content = clean_ieee_formatting(content_text)

            output_file = f"{output_dir}/{section_name}.tex"
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(f"% Extracted {section_name}\n")
                f.write(f"% Converted from IEEE TMI to Elsevier KBS format\n\n")
                f.write(cleaned_content)

            print(f"✅ Extracted {section_name} -> {output_file}")
        else:
            print(f"❌ {section_name} not found")

    # Save visual elements
    for name, items in [('figures', figures), ('tables', tables), ('equations', equations)]:
        if items:
            output_file = f"{output_dir}/{name}_all.tex"
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(f"% All {name} from TMI paper\n")
                f.write(f"% Found {len(items)} items\n\n")
                for i, item in enumerate(items):
                    cleaned_item = clean_ieee_formatting(item)
                    f.write(f"%% {name.capitalize()} {i+1}\n")
                    f.write(cleaned_item)
                    f.write("\n\n")
            print(f"✅ Extracted {len(items)} {name} -> {output_file}")

    # Create comprehensive summary
    summary_file = f"{output_dir}/SUMMARY.md"
    with open(summary_file, 'w', encoding='utf-8') as f:
        f.write("# TMI to KBS Conversion Summary\n\n")
        f.write(f"**Title:** {extracted.get('title', 'Not found')}\n\n")

        # Abstract analysis
        abstract = extracted.get('abstract', '')
        if abstract != 'Section abstract not found':
            word_count = len(abstract.split())
            f.write(f"## Abstract\n")
            f.write(f"- Length: {word_count} words (KBS limit: 250)\n")
            f.write(
                f"- Status: {'✅ OK' if word_count <= 250 else '⚠️ Too long'}\n\n")

        # Keywords analysis
        keywords = extracted.get('keywords', '')
        if keywords != 'Section keywords not found':
            kw_list = [k.strip()
                       for k in keywords.replace('\\sep', ',').split(',')]
            f.write(f"## Keywords\n")
            f.write(f"- Count: {len(kw_list)} (KBS limit: 1-7)\n")
            f.write(f"- Keywords: {', '.join(kw_list)}\n\n")

        # Content overview
        f.write("## Content Status\n")
        found_sections = [name for name, content in extracted.items()
                          if content != f"Section {name} not found"]
        f.write(f"- Sections found: {len(found_sections)}\n")
        f.write(f"- Figures: {len(figures)}\n")
        f.write(f"- Tables: {len(tables)}\n")
        f.write(f"- Equations: {len(equations)}\n\n")

        # Adaptation guide
        f.write("## Adaptation Priority for KBS (20-page limit)\n\n")
        f.write("### 🎯 High Priority (Keep Detailed)\n")
        f.write("- DAAM Architecture (your innovation)\n")
        f.write("- Experimental results\n")
        f.write("- Medical domain applications\n\n")

        f.write("### 📝 Medium Priority (Condense 30-50%)\n")
        f.write("- Introduction\n")
        f.write("- Methodology core\n")
        f.write("- Key results\n\n")

        f.write("### ✂️ Low Priority (Heavily condense/remove)\n")
        f.write("- Related work (keep only most relevant)\n")
        f.write("- Detailed ablations (summarize)\n")
        f.write("- Extended discussions\n\n")

        f.write("### 🎯 KBS Focus Areas\n")
        f.write("Emphasize these aspects for KBS journal:\n")
        f.write("- Knowledge-based computer vision\n")
        f.write("- Intelligent decision support systems\n")
        f.write("- Machine learning methodology\n")
        f.write("- Data science techniques\n")

    print(f"\n🎉 Extraction complete!")
    print(f"📁 Output: {output_dir}/")
    print(f"📋 Summary: {summary_file}")
    print(
        f"✅ Found {len([s for s in extracted.values() if 'not found' not in s])} sections")
    print(
        f"🖼️ Found {len(figures)} figures, {len(tables)} tables, {len(equations)} equations")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 extract_complete.py <tmi_file>")
        print("Example: python3 extract_complete.py to_be_reference/full_tmi.tex")
        sys.exit(1)

    extract_sections_from_tmi(sys.argv[1])
