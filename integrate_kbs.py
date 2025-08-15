#!/usr/bin/env python3
"""
Integration script to merge extracted TMI content into KBS template
This will create a complete KBS paper from the extracted sections
"""

import os
import re


def load_section(section_file):
    """Load content from a section file"""
    try:
        with open(f"extracted_sections_complete/{section_file}", 'r', encoding='utf-8') as f:
            content = f.read()
        # Remove the header comments
        lines = content.split('\n')
        content_lines = []
        skip_header = True
        for line in lines:
            if skip_header and line.startswith('% '):
                continue
            elif skip_header and line.strip() == '':
                continue
            else:
                skip_header = False
                content_lines.append(line)
        return '\n'.join(content_lines)
    except FileNotFoundError:
        print(f"Warning: {section_file} not found")
        return ""


def clean_ieee_refs(text):
    """Clean IEEE-specific reference formatting for KBS"""
    # Convert \cite{ref} to ~\cite{ref}
    text = re.sub(r'([^~])\\cite{', r'\1~\\cite{', text)
    # Fix multiple citations
    text = re.sub(r'~\\cite{([^}]+)}~\\cite{', r'~\\cite{\1,', text)
    return text


def create_integrated_paper():
    """Create the integrated KBS paper"""

    # Load all sections
    abstract = load_section("abstract.tex")
    keywords = load_section("keywords.tex")
    three_challenges = load_section("three_challenges.tex")
    contributions = load_section("contributions.tex")
    related_work = load_section("related_work.tex")
    methodology = load_section("methodology.tex")
    daam = load_section("daam_complete.tex")
    results = load_section("results.tex")
    conclusion = load_section("conclusion.tex")
    acknowledgments = load_section("acknowledgments.tex")
    funding_thanks = load_section("funding_thanks.tex")

    # Create the integrated paper content
    integrated_content = f'''%% 
%% Copyright 2007-2025 Elsevier Ltd
%% 
%% Template article for Elsevier's document class `elsarticle'
%% with numbered style bibliographic references
%% Adapted for Knowledge-Based Systems journal submission
%% 
\\documentclass[preprint,12pt]{{elsarticle}}

%% Use the option review to obtain double line spacing
%% \\documentclass[preprint,review,12pt]{{elsarticle}}

%% Use the options 1p,twocolumn; 3p; 3p,twocolumn; 5p; or 5p,twocolumn
%% for a journal layout:
%% \\documentclass[final,3p,times]{{elsarticle}}

%% The amssymb package provides various useful mathematical symbols
\\usepackage{{amssymb}}
%% The amsmath package provides various useful equation environments.
\\usepackage{{amsmath}}

%% Additional packages for medical imaging paper
\\usepackage{{algorithmic}}
\\usepackage{{textcomp}}
\\usepackage{{multirow}}
\\usepackage{{url}}
\\usepackage{{subcaption}}
\\usepackage{{microtype}}

\\journal{{Knowledge-Based Systems}}

\\begin{{document}}

\\begin{{frontmatter}}

\\title{{MedDef: An Efficient Self-Attention Model for Adversarial Resilience in Medical Imaging with Unstructured Pruning}}

\\author[a]{{E.K. Dongbo}}
\\author[a]{{S. Niu\\corref{{cor1}}}}
\\author[b]{{P. Fero}}
\\author[b]{{P. Bargin}}
\\author[c]{{J.N. Kofa}}

\\ead{{sjniu@hotmail.com}}

%% Author affiliations
\\affiliation[a]{{organization={{School of Information Science and Engineering, University of Jinan}},
            addressline={{}}, 
            city={{Jinan}},
            postcode={{250022}}, 
            state={{Shandong}},
            country={{P.R. China}}}}

\\affiliation[b]{{organization={{School of Computer Science \\& Technology, Zhejiang Sci-Tech University}},
            addressline={{}}, 
            city={{Hangzhou}},
            postcode={{310018}}, 
            state={{}},
            country={{P.R. China}}}}

\\affiliation[c]{{organization={{College of Informatics, Huazhong Agricultural University}},
            addressline={{}}, 
            city={{Wuhan}},
            postcode={{430070}}, 
            state={{}},
            country={{P.R. China}}}}

\\cortext[cor1]{{Corresponding author}}

%% Abstract (max 250 words)
\\begin{{abstract}}
{clean_ieee_refs(abstract)}
\\end{{abstract}}

%%Research highlights
\\begin{{highlights}}
\\item Novel Defense-Aware Attention Mechanism (DAAM) integrates adversarial robustness into feature extraction
\\item Medical domain-aware defensive strategy preserves diagnostic features while suppressing attacks
\\item Unstructured pruning enhances security rather than compromising it in medical imaging
\\item Achieves 97.52\\% adversarial accuracy with maintained diagnostic performance
\\item Comprehensive evaluation on Retinal OCT and Chest X-Ray datasets against multiple attacks
\\end{{highlights}}

%% Keywords (1-7 keywords)
\\begin{{keyword}}
{keywords.replace(',', ' \\sep ')}
\\end{{keyword}}

\\end{{frontmatter}}

\\section{{Introduction}}
\\label{{sec:introduction}}

Deep neural networks have revolutionized medical imaging analysis, achieving unprecedented diagnostic accuracy across various conditions~\\cite{{Mamo24}}. While these systems approach or exceed human-level performance in specialized tasks, they remain vulnerable to adversarial attacks; imperceptible perturbations that cause incorrect predictions with potentially serious clinical consequences~\\cite{{Bortsova21, Kaviani22}}.

Current defense strategies fall into several areas, which can be categorically grouped into three: (1) input preprocessing techniques (denoising~\\cite{{Chiang20}}, JPEG compression~\\cite{{Cheng21}}) that neutralize perturbations; (2) model regularization approaches like adversarial training~\\cite{{Muoka23}} that improve robustness; and (3) architectural modifications (defensive distillation~\\cite{{Qi24}}, feature squeezing~\\cite{{vasan2024}}, ensemble methods~\\cite{{Alzubaidi24}}) that detect or mitigate adversarial inputs. The success of these methods is, however, constrained by the particular difficulties associated with medical imaging.

{clean_ieee_refs(three_challenges)}

To tackle adversarial vulnerabilities in medical imaging, we propose MedDef, a framework built around a Defense-Aware Attention Mechanism (DAAM) that integrates defense directly into feature processing. DAAM comprises three components: Adversarial Feature Detection (AFD), which suppresses high-frequency adversarial noise while preserving fine-grained diagnostic features; Medical Feature Extraction (MFE), which enhances edge and texture cues using domain knowledge; and Multi-Scale Feature Analysis (MSF), which defends across spatial resolutions to maintain robust hierarchical representations.

{clean_ieee_refs(contributions)}

\\section{{Related Work}}
\\label{{sec:related_work}}

{clean_ieee_refs(related_work[:2000])}  % Truncate to fit page limits

\\section{{Methodology}}
\\label{{sec:methodology}}

{clean_ieee_refs(methodology[:3000])}  % Keep core methodology

\\subsection{{Defense-Aware Attention Mechanism (DAAM)}}

{clean_ieee_refs(daam)}

\\section{{Experimental Results}}
\\label{{sec:results}}

{clean_ieee_refs(results[:4000])}  % Keep key results

\\section{{Conclusion}}
\\label{{sec:conclusion}}

{clean_ieee_refs(conclusion)}

%% Acknowledgments section
\\section*{{Acknowledgments}}
{clean_ieee_refs(acknowledgments)}

%% CRediT authorship contribution statement (required for KBS)
\\section*{{CRediT authorship contribution statement}}
\\textbf{{E.K. Dongbo:}} Conceptualization, Methodology, Software, Validation, Formal analysis, Investigation, Writing – original draft, Writing – review \\& editing, Visualization.
\\textbf{{S. Niu:}} Conceptualization, Methodology, Supervision, Project administration, Funding acquisition, Writing – review \\& editing.
\\textbf{{P. Fero:}} Methodology, Validation, Investigation, Writing – review \\& editing.
\\textbf{{P. Bargin:}} Data curation, Resources, Investigation.
\\textbf{{J.N. Kofa:}} Formal analysis, Investigation, Writing – review \\& editing.

%% Declaration of competing interests (required for KBS)
\\section*{{Declaration of competing interests}}
The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

%% Data availability statement (required for KBS)
\\section*{{Data availability}}
The datasets used in this study are publicly available: Retinal OCT dataset and Chest X-Ray dataset. Code and additional materials will be made available upon reasonable request.

%% Funding statement (required for KBS)
\\section*{{Funding}}
This work was supported by the National Natural Science Foundation of China [grant numbers 62471202, 62302191]; the Natural Science Foundation of Shandong Province [grant number ZR2023QF001]; Development Program Project of Youth Innovation Team of Institutions of Higher Learning in Shandong Province [grant number 2023KJ315]; Young Talent of Lifting Engineering for Science and Technology in Shandong [grant number SDAST2024QTA014]; and the Key Laboratory of Intelligent Computing Technology for Network Environment, Shandong Province.

\\bibliographystyle{{elsarticle-num}} 
\\bibliography{{ref/references}}

\\end{{document}}'''

    # Write the integrated paper
    with open('main_integrated.tex', 'w', encoding='utf-8') as f:
        f.write(integrated_content)

    print("✅ Created main_integrated.tex with full content")
    print("📝 Next steps:")
    print("   1. Review content and adjust for 20-page limit")
    print("   2. Add figures using the extracted figures_all.tex")
    print("   3. Add tables using the extracted tables_all.tex")
    print("   4. Test compilation: make clean && pdflatex main_integrated")

    # Create a figure integration helper
    create_figure_helper()


def create_figure_helper():
    """Create helper script to integrate figures"""
    figures_content = load_section("figures_all.tex")

    helper_content = f'''% Figure Integration Helper
% Copy relevant figures from below into your main_integrated.tex

{figures_content}

% Usage Instructions:
% 1. Select the figures you want to include in your final paper
% 2. Copy them into the appropriate sections of main_integrated.tex
% 3. Ensure all figure files exist in the fig/ directory
% 4. Update figure references in the text
'''

    with open('figures_helper.tex', 'w', encoding='utf-8') as f:
        f.write(helper_content)
    print("✅ Created figures_helper.tex")


if __name__ == "__main__":
    if not os.path.exists("extracted_sections_complete"):
        print("❌ Error: extracted_sections_complete directory not found")
        print("Run the extraction script first")
        exit(1)

    create_integrated_paper()
