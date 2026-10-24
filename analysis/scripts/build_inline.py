#!/usr/bin/env python3
"""Inline-figure reading copy: insert the PNG figures after the section of the
main manuscript where each is first discussed. Output is a convenience copy;
the submission uses figure files separately."""
import os
from docx import Document
from docx.shared import Inches

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
MAN = os.path.join(ROOT, "manuscript")
FIGD = os.path.join(ROOT, "analysis", "figures")

FIG_AFTER_HEADING = {
    "1. Introduction": "fig1_ontology.png",
    "3.1 Coverage and the activity matrix": "fig2_activity_matrix.png",
    "3.2 Dimensionality": "fig3_ordination.png",
    "3.3 Asynchronous persistence": "fig4_persistence.png",
    "3.4 Network architecture": "fig5_networks.png",
    "3.6 Comparison with simple descriptors": "fig6_energy.png",
}

doc = Document(os.path.join(MAN, "EPSL_main_manuscript.docx"))
paras = doc.paragraphs
insert_at = []
for i, p in enumerate(paras):
    t = p.text.strip()
    if t in FIG_AFTER_HEADING:
        # insert after the paragraph that follows the heading
        insert_at.append((i + 1, FIG_AFTER_HEADING[t]))

from docx.oxml.ns import qn
import copy
for idx, png in insert_at:
    anchor = paras[idx]
    new_p = anchor.insert_paragraph_before()  # placeholder: we want AFTER anchor
    # move new_p after anchor
    anchor._p.addnext(new_p._p)
    run = new_p.add_run()
    run.add_picture(os.path.join(FIGD, png), width=Inches(6.2))

doc.save(os.path.join(MAN, "EPSL_main_manuscript_inline.docx"))
print("inline docx written")
