# CVPR 2027 paper

Title: **Cost-Aware Multi-Frame Deferral for Promptable Video Segmentation**

Migrated from `../Multi_Frame_Selection_AAAI_2027/00_paper.tex` and its standalone
`appendix.tex`. The AAAI source directory is unchanged. The complete original
CVPR template, including its instructional sections and original PDF, is preserved
in `../cvpr_2027_original_template/`.

## Editing

- `main.tex`: CVPR review-mode entry point; imports all content and appendix.
- `sec/0_abstract.tex`: abstract.
- `sec/1_intro.tex` through `sec/7_conclusion.tex`: main paper.
- `sec/8_llm_usage.tex`: required LLM Usage Statement.
- `sec/X_suppl.tex`: complete appendix, with lettered sections.
- `main.bib`: copied AAAI bibliography, rendered with CVPR's numeric style.
- `Figures/`: copied source figure assets.
- `tables/`: individual table LaTeX files, imported from the sections with `\input`.
- `preamble.tex`: additional packages. `cvpr.sty` is unchanged.

Author comments and superseded commented-out alternatives were omitted from the
working copy; all remain in the untouched AAAI sources. Scientific prose, results,
figures, and appendix content were retained. Citation commands, heading case,
table-caption placement, and display-equation numbering were adapted for CVPR.
Math in appendix headings was replaced by equivalent plain wording to avoid an
infinite expansion with the local LaTeX/hyperref installation.

## Build

Requires a LaTeX installation with `latexmk`, `pdflatex`, and `bibtex`, Python 3,
Poppler (`pdftotext`), and the Python package `pypdf` (`python3 -m pip install pypdf`).

```sh
python3 scripts/build.py
```

Outputs:

- `main.pdf`: combined reading copy (18 pages).
- `paper.pdf`: submission manuscript (9 pages including references).
- `supplementary.pdf`: appendix only (9 pages).

The main scientific text ends on page 8. The LLM Usage Statement follows the
conclusion, before references; references continue through page 9. Supplementary
material starts on combined page 10. Upload the separate paper and supplementary
files, rather than the combined reading copy. Supplementary page numbers continue
from the main manuscript, preserving cross-reference numbers.

For IDE compilation, `main.tex` also builds normally with `latexmk -pdf main.tex`.
Re-run `scripts/build.py` after edits to refresh the separate PDFs.

## Before submission

Confirm that the LLM Usage Statement also covers any AI use predating this
migration; the current statement describes only the assistance known here.
Check the legibility of inherited plot and figure labels at actual print size.
This migration does not independently validate scientific claims, bibliography
accuracy, or research ethics documentation.

Official policies: https://cvpr.thecvf.com/Conferences/2027/AuthorGuidelines
