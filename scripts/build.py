#!/usr/bin/env python3
"""Compile the combined draft and split its main/supplementary PDFs using pypdf."""
from pathlib import Path
import shutil
import subprocess
from pypdf import PdfReader, PdfWriter

root = Path(__file__).resolve().parents[1]
def run(*args):
    return subprocess.run(args, cwd=root, check=True, text=True, stdout=subprocess.PIPE).stdout

print('Compiling CVPR draft...', flush=True)
run('latexmk', '-pdf', '-jobname=cvpr_final', '-outdir=build',
    '-interaction=nonstopmode', '-halt-on-error', 'main.tex')
combined = root / 'build/cvpr_final.pdf'
pages = run('pdftotext', '-layout', str(combined), '-').split('\f')
start = next(i + 1 for i, text in enumerate(pages) if 'Supplementary Material' in text)
count = len([p for p in pages if p.strip()])
reader = PdfReader(combined)
for name, bounds in [('paper.pdf', (0, start - 1)),
                     ('supplementary.pdf', (start - 1, count))]:
    writer = PdfWriter()
    writer.append(reader, pages=bounds)
    writer.add_metadata({'/Title': 'Cost-Aware Multi-Frame Deferral for Promptable Video Segmentation',
                         '/Author': 'Anonymous'})
    with (root / name).open('wb') as stream:
        writer.write(stream)
shutil.copy2(combined, root / 'main.pdf')
print(f'main.pdf: {count} pages (combined reading copy)')
print(f'paper.pdf: {start - 1} pages (main paper, statement, references)')
print(f'supplementary.pdf: {count - start + 1} pages (appendix)')
