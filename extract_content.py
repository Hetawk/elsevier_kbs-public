#!/usr/bin/env python3
"""
Script to help adapt content from IEEE TMI format to Elsevier KBS format
This script helps extract and convert sections from your existing paper.
"""

import re
import sys


def extract_sections_from_tmi(file_path):
    """Extract sections from the TMI paper for adaptation"""

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Error: Could not find file {file_path}")
        return

    # Define section patterns to extract
    sections = {
        'abstract': r'\\begin{abstract}(.*?)\\end{abstract}',
        'keywords': r'\\begin{IEEEkeywords}(.*?)\\end{IEEEkeywords}',
        'introduction': r'\\section{Introduction}\\label{sec:introduction}(.*?)(?=\\section)',
        'related_work': r'\\section{Related Work}\\label{sec:related_work}(.*?)(?=\\section)',
        'methodology': r'\\section{Methodology}\\label{sec:methodology}(.*?)(?=\\section)',
    }

    extracted = {}

    for section_name, pattern in sections.items():
        match = re.search(pattern, content, re.DOTALL)
        if match:
            extracted[section_name] = match.group(1).strip()
        else:
            extracted[section_name] = f"Section {section_name} not found"

    # Clean up IEEE-specific formatting
    def clean_ieee_formatting(text):
        # Convert IEEE references to Elsevier format
        text = re.sub(r'\\cite{([^}]+)}', r'~\\cite{\1}', text)

        # Remove IEEE-specific commands
        text = re.sub(r'\\IEEEPARstart{([^}]+)}{([^}]+)}', r'\1\2', text)

        # Convert IEEE keywords format
        if 'IEEEkeywords' in text:
            text = text.replace('\\begin{IEEEkeywords}', '').replace(
                '\\end{IEEEkeywords}', '')
            text = re.sub(r',\s*', r' \\sep ', text.strip())

        return text

    # Process and save sections
    output_dir = "extracted_sections"
    import os
    os.makedirs(output_dir, exist_ok=True)

    for section_name, content in extracted.items():
        cleaned_content = clean_ieee_formatting(content)

        output_file = f"{output_dir}/{section_name}.tex"
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(f"% Extracted {section_name} section\n")
            f.write(f"% Converted from IEEE TMI to Elsevier KBS format\n\n")
            f.write(cleaned_content)

        print(f"Extracted {section_name} -> {output_file}")

    print(f"\nExtraction complete! Check the '{output_dir}' directory.")
    print("\nNext steps:")
    print("1. Review each extracted section file")
    print("2. Copy relevant content to your main.tex file")
    print("3. Adapt citations and formatting as needed")
    print("4. Ensure compliance with KBS guidelines (max 20 pages)")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 extract_content.py <path_to_tmi_file>")
        print("Example: python3 extract_content.py to_be_reference/full_tmi.tex")
        sys.exit(1)

    extract_sections_from_tmi(sys.argv[1])
