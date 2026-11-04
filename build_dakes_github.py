# -*- coding: utf-8 -*-
"""
DaKES Academic Repository One-Click Builder & Zenodo Linker
Target Repo: https://github.com/fredyingye-usa/dakes
Author: Prof. Dr. Fred Y. Ye (叶福翔)
"""

import os
from pathlib import Path

REPO_URL = "https://github.com/fredyingye-usa/dakes"
AUTHOR = "Ye, Fred Y."

# 完整解析自 KeyPublishData.txt 的 43 项学术成果结构化数据库
PUBLICATIONS = [
    # --- 1. Academic & Disciplinary Monographs ---
    {"cat": "Monographs", "sub": "Collected Works", "date": "2026-11-01", "title": "Dr. Ye's Collected Representative Works (Total 12 Vols.)", "doi": "10.5281/zenodo.23886305", "url": "https://zenodo.org/records/23886305", "isbn": ""},
    {"cat": "Monographs", "sub": "Mathematics", "date": "2026-07-08", "title": "Spectral-Geometric Program of the Riemann and Grand Riemann Hypotheses", "doi": "10.5281/zenodo.22060151", "url": "https://zenodo.org/records/22060151", "isbn": "979-8-182-51852-9"},
    {"cat": "Monographs", "sub": "Mathematics", "date": "2026-07-08", "title": "Spectral-Flow and Geometric-Closure Framework for Hodge Classes: A Conditional Program", "doi": "10.5281/zenodo.22770350", "url": "https://zenodo.org/records/22770350", "isbn": "979-8-182-51854-3"},
    {"cat": "Monographs", "sub": "Physics", "date": "2026-06-26", "title": "Vortex Field Theory: New Principles for Approaching Physical Unification", "doi": "10.5281/zenodo.23675225", "url": "https://zenodo.org/records/23675225", "isbn": "979-8-823-18069-6"},
    {"cat": "Monographs", "sub": "Physics", "date": "2026-06-26", "title": "Scalar-Vector-Spinor Effective Field Theory: A 5D Cl(2,3) Physical Unification", "doi": "10.5281/zenodo.23675315", "url": "https://zenodo.org/records/23675315", "isbn": "979-8-182-50531-4"},

    # --- 2. Mathematical Papers ---
    {"cat": "Mathematics", "sub": "Paper", "date": "2026-04-24", "title": "Reversal Dual Calculus: Harmonic Regularization in Gravitational Potential and Zeta Function Duality", "doi": "10.5281/zenodo.19764503", "url": "https://zenodo.org/records/19764503"},
    {"cat": "Mathematics", "sub": "Paper", "date": "2026-06-27", "title": "Spectral Flow and Categorified Index for Higher-Dimensional Prime-Torus Packets over the Scaling Site", "doi": "10.5281/zenodo.20944516", "url": "https://zenodo.org/records/20944516"},
    {"cat": "Mathematics", "sub": "Paper", "date": "2026-06-27", "title": "From Prime Circles to Fargues-Fontaine Curves: A Conditional Spectral-Flow Framework for Local Arithmetic Langlands", "doi": "10.5281/zenodo.20944785", "url": "https://zenodo.org/records/20944785"},
    {"cat": "Mathematics", "sub": "Paper", "date": "2026-06-27", "title": "Arithmetic Dirac Packets, Fargues-Fontaine Slopes, and Weil Positivity: A Conditional Spectral Route Toward the Riemann Hypothesis", "doi": "10.5281/zenodo.20945167", "url": "https://zenodo.org/records/20945167"},
    {"cat": "Mathematics", "sub": "Paper", "date": "2026-06-28", "title": "Operator Traces, Prime-Power Weights, and a Trace-Compatible Weil Positivity Theorem", "doi": "10.5281/zenodo.20997606", "url": "https://zenodo.org/records/20997606"},
    {"cat": "Mathematics", "sub": "Paper", "date": "2026-06-28", "title": "Uniform Convergence of Regularized Determinants for Zeta Spectral Triples: Toward Global Weil Positivity and the Riemann Hypothesis", "doi": "10.5281/zenodo.20998327", "url": "https://zenodo.org/records/20998327"},
    {"cat": "Mathematics", "sub": "Paper", "date": "2026-06-28", "title": "Screw Functions, de Branges Spaces, and Zeta Spectral Triples: A Spectral-Geometric Approach to RH and GRH", "doi": "10.5281/zenodo.20998512", "url": "https://zenodo.org/records/20998512"},
    {"cat": "Mathematics", "sub": "Paper", "date": "2026-06-29", "title": "Spectral-Geometric Approaches to RH and GRH: The Sobolev-Suzuki L² Framework for WEC and TR", "doi": "10.5281/zenodo.21032614", "url": "https://zenodo.org/records/21032614"},
    {"cat": "Mathematics", "sub": "Paper", "date": "2026-07-08", "title": "A Spectral-Geometric Program of Birch and Swinnerton-Dyer Conjecture", "doi": "10.5281/zenodo.21316732", "url": "https://zenodo.org/records/21316732"},
    {"cat": "Mathematics", "sub": "Paper", "date": "2026-07-12", "title": "Spectral Paradigm of Analytic Number Theory", "doi": "10.5281/zenodo.23126332", "url": "https://zenodo.org/records/23126332"},
    {"cat": "Mathematics", "sub": "Paper", "date": "2026-11-02", "title": "Quantitative Ground State Closure for the Weil Operator and Diagonal Hurwitz Reduction of the Riemann Hypothesis", "doi": "10.5281/zenodo.23886960", "url": "https://zenodo.org/records/23886960"},
    {"cat": "Mathematics", "sub": "Paper", "date": "2026-11-02", "title": "Two Decisive Closure Theorems for a Weil Hurwitz Approach to the Riemann Hypothesis", "doi": "10.5281/zenodo.23887241", "url": "https://zenodo.org/records/23887241"},
    {"cat": "Mathematics", "sub": "Paper", "date": "2026-11-02", "title": "Four Gate Certification for a Weil Hurwitz Route to the Riemann Hypothesis", "doi": "10.5281/zenodo.23887551", "url": "https://zenodo.org/records/23887551"},

    # --- 3. Physical Papers & Datasets ---
    {"cat": "Physics", "sub": "Paper", "date": "2026-04-25", "title": "TimeKK_Zenodo: A Modified Kaluza-Klein Framework for Quantum Gravity via Imaginary Time as a Fifth Dimension", "doi": "10.5281/zenodo.19764139", "url": "https://zenodo.org/records/19764139"},
    {"cat": "Physics", "sub": "Paper", "date": "2026-04-25", "title": "A Unified Operational Framework for Wave–Particle Duality via Metaplectic Transforms", "doi": "10.5281/zenodo.19772394", "url": "https://zenodo.org/records/19772394"},
    {"cat": "Physics", "sub": "Paper", "date": "2026-04-28", "title": "A Minimal Scalar-Vector-Spinor Effective Field Theory for Dark-Sector Phenomenology and Modified Cosmological Dynamics", "doi": "10.5281/zenodo.19855576", "url": "https://zenodo.org/records/19855576"},
    {"cat": "Physics", "sub": "Paper", "date": "2026-05-01", "title": "A 5D Scalar-Vector-Spinor Effective Field Theory in Cl(2,3): Real-Imaginary Time Co-ordering Energy-Information", "doi": "10.5281/zenodo.19949736", "url": "https://zenodo.org/records/19949736"},
    {"cat": "Physics", "sub": "Paper", "date": "2026-05-02", "title": "Metaplectic Holography and Gauge Embedding in 5D SVS-EFT: Bridging the Standard Model and Gravitation", "doi": "10.5281/zenodo.19981083", "url": "https://zenodo.org/records/19981083"},
    {"cat": "Physics", "sub": "Paper", "date": "2026-08-19", "title": "Theory of Heterocrystals: Unit-Cell Rupture, Emergent Gauge Fields, and Quantum Geometry", "doi": "10.5281/zenodo.22017051", "url": "https://zenodo.org/records/22017051"},
    {"cat": "Physics", "sub": "Paper", "date": "2026-08-19", "title": "Heterocrystalline chimeric technology: topology-gated multiphysics and risk-aware inverse design", "doi": "10.5281/zenodo.22017089", "url": "https://zenodo.org/records/22017089"},
    {"cat": "Physics", "sub": "Dataset", "date": "2026-07-30", "title": "Dataset: Theory of heterocrystals", "doi": "10.5281/zenodo.21702944", "url": "https://zenodo.org/records/21702944"},
    {"cat": "Physics", "sub": "Dataset", "date": "2026-08-03", "title": "Dataset: Heterocrystalline chimeric technology", "doi": "10.5281/zenodo.21778647", "url": "https://zenodo.org/records/21778647"},
    {"cat": "Physics", "sub": "Dataset", "date": "2026-10-22", "title": "Heterocrystalline chimeric technology -- completed dataset", "doi": "10.5281/zenodo.23575685", "url": "https://zenodo.org/records/23575685"},

    # --- 4. Biomedical Papers & Datasets ---
    {"cat": "Biomedicine", "sub": "Paper", "date": "2026-05-08", "title": "OCT4-MHC Tight Linkage in Mammals: A Comparative Evo-Devo, Immunogenomic, and Topological Framework", "doi": "10.5281/zenodo.20089673", "url": "https://zenodo.org/records/20089673"},
    {"cat": "Biomedicine", "sub": "Paper", "date": "2026-08-19", "title": "Multilayer h-Backbones Identify KLRB1 as a Stable Immune-Ageing h-Focus across Populations, Tissues and Cell Lineages", "doi": "10.5281/zenodo.22018570", "url": "https://zenodo.org/records/22018570"},
    {"cat": "Biomedicine", "sub": "Paper", "date": "2026-08-22", "title": "Multiscale h-Foci and CNS-Gated Reversal Identify Riluzole as a Repurposing Candidate in Alzheimer's Disease", "doi": "10.5281/zenodo.22057218", "url": "https://zenodo.org/records/22057218"},
    {"cat": "Biomedicine", "sub": "Paper", "date": "2026-08-28", "title": "Spiro-Terpenoid Privileged Scaffolds: An Auditable Multiscale Workflow for Undruggable Targets", "doi": "10.5281/zenodo.22147096", "url": "https://zenodo.org/records/22147096"},
    {"cat": "Biomedicine", "sub": "Paper", "date": "2026-09-15", "title": "Comparator-Dependent Druggability and Safety of Spiro-Terpenoid Scaffolds: A Proteome-Scale Pocket-Transfer Screen", "doi": "10.5281/zenodo.22770001", "url": "https://zenodo.org/records/22770001"},
    {"cat": "Biomedicine", "sub": "Dataset", "date": "2026-07-21", "title": "Dataset: Multilayer h-Backbones Identify KLRB1 as a Stable Immune-Ageing h-Focus across Populations, Tissues and Cell Lineages", "doi": "10.5281/zenodo.21464228", "url": "https://zenodo.org/records/21464228"},
    {"cat": "Biomedicine", "sub": "Dataset", "date": "2026-07-22", "title": "Dataset: Multiscale h-Foci and CNS-Gated Reversal Identify Riluzole as a Repurposing Candidate in Alzheimer's Disease", "doi": "10.5281/zenodo.21493971", "url": "https://zenodo.org/records/21493971"},
    {"cat": "Biomedicine", "sub": "Dataset", "date": "2026-08-11", "title": "Dataset: Spiro-Terpenoid Privileged Scaffolds", "doi": "10.5281/zenodo.21888841", "url": "https://zenodo.org/records/21888841"},
    {"cat": "Biomedicine", "sub": "Dataset", "date": "2026-08-17", "title": "Dataset: Comparator-Dependent Druggability and Safety of Spiro-Terpenoid Scaffolds", "doi": "10.5281/zenodo.21970731", "url": "https://zenodo.org/records/21970731"},

    # --- 5. Economics & Philosophy (SSRN) ---
    {"cat": "Economics_Philosophy", "sub": "Economics", "date": "2026-05-02", "title": "Market-Driven Growth with Knowledge and Capital as Twin Propellants: Integrating Melitz-Finance Micro-foundations and Ramsey Optimal Policy", "doi": "10.2139/ssrn.6697998", "url": "https://ssrn.com/abstract=6697998"},
    {"cat": "Economics_Philosophy", "sub": "Economics", "date": "2026-05-03", "title": "Probing the Efficiency-Equity-Innovation Trilemma: Economic Analysis via Grand Synthetic Model", "doi": "10.2139/ssrn.6703820", "url": "https://ssrn.com/abstract=6703820"},
    {"cat": "Economics_Philosophy", "sub": "Economics", "date": "2026-05-04", "title": "Knowledge-Driven Endogenous Growth in Open Economy: A Grand Synthetic Approach", "doi": "10.2139/ssrn.6709739", "url": "https://ssrn.com/abstract=6709739"},
    {"cat": "Economics_Philosophy", "sub": "Economics", "date": "2026-09-08", "title": "Knowledge and Capital as Co-evolving Productive Stocks: A Minimal Core of Grand Synthetic Economics", "doi": "10.2139/ssrn.7473120", "url": "https://ssrn.com/abstract=7473120"},
    {"cat": "Economics_Philosophy", "sub": "Economics", "date": "2026-09-08", "title": "Creative Destruction and Open-Market Reversals: Dynamic Equilibrium in Grand Synthetic Economics", "doi": "10.2139/ssrn.7473121", "url": "https://ssrn.com/abstract=7473121"},
    {"cat": "Economics_Philosophy", "sub": "Philosophy", "date": "2026-05-12", "title": "AI Philosophy from Triad Philosophy: Triadic Governance of Artificial Intelligence beyond Binary Minds", "doi": "10.2139/ssrn.6755681", "url": "https://ssrn.com/abstract=6755681"},
]

def make_badge(doi, url, isbn=""):
    if "zenodo" in doi:
        badge = f"[![DOI](https://zenodo.org/badge/DOI/{doi}.svg)]({url})"
    else:
        badge = f"[![SSRN DOI](https://img.shields.io/badge/SSRN-{doi.replace('-', '--')}-blue.svg)]({url})"
    if isbn:
        badge += f" [![B&N ISBN](https://img.shields.io/badge/B%26N_ISBN-{isbn.replace('-', '--')}-00573F.svg)]({url})"
    return badge

def build_repository():
    # 1. 创建分类目录
    folders = ["01_Monographs", "02_Mathematics", "03_Physics", "04_Biomedicine", "05_Economics_Philosophy"]
    for folder in folders:
        Path(folder).mkdir(exist_ok=True)

    # 2. 生成主 README.md
    lines = [
        "# DaKES Institute: Collected Monographs, Papers & Datasets of Prof. Dr. Fred Y. Ye",
        "",
        "[![Collected Works DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.23886305.svg)](https://zenodo.org/records/23886305)",
        "[![Website](https://img.shields.io/badge/Platform-dakes.top-0A66C2.svg)](https://www.dakes.top)",
        "[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)",
        "",
        "> **Official Academic Portal & Open-Science Repository**  ",
        "> **Author:** Prof. Dr. Fred Y. Ye (叶福翔) | DaKES Institute & Nanjing University  ",
        "> **Repository URL:** [https://github.com/fredyingye-usa/dakes](https://github.com/fredyingye-usa/dakes)",
        "",
        "---",
        "",
        "## 1. Key Academic Monographs & Collected Works (学术专著与代表作全集)",
        "| Date | Monograph Title | Identifiers & Access (Zenodo DOI / B&N Press ISBN) |",
        "| :--- | :--- | :--- |"
    ]

    for p in PUBLICATIONS:
        if p["cat"] == "Monographs":
            lines.append(f"| {p['date']} | **{p['title']}** | {make_badge(p['doi'], p['url'], p.get('isbn', ''))} |")

    sections = [
        ("Mathematics", "## 2. Mathematical Papers (Riemann Hypothesis, Spectral Flow & Langlands)"),
        ("Physics", "## 3. Physical Papers & Datasets (5D Cl(2,3) SVS-EFT, Vortex Field & Heterocrystals)"),
        ("Biomedicine", "## 4. Biomedical Papers & Datasets (Multilayer h-Backbones & Spiro-Terpenoid Scaffolds)"),
        ("Economics_Philosophy", "## 5. Grand Synthetic Economics (GSE) & Triad Philosophy (SSRN Series)")
    ]

    for cat_key, header in sections:
        lines.extend(["", header, "| Date | Type | Title | Permanent Identifier (DOI) |", "| :--- | :--- | :--- | :--- |"])
        for p in PUBLICATIONS:
            if p["cat"] == cat_key:
                lines.append(f"| {p['date']} | `{p['sub']}` | {p['title']} | {make_badge(p['doi'], p['url'])} |")

    lines.extend([
        "",
        "---",
        "## Citation & BibTeX",
        "All BibTeX entries are consolidated in [`references.bib`](references.bib). You can also click the **\"Cite this repository\"** button on the top-right sidebar of this GitHub page."
    ])

    Path("README.md").write_text("\n".join(lines), encoding="utf-8")

    # 3. 生成 CITATION.cff
    cff_content = f"""cff-version: 1.2.0
message: "If you reference these monographs, papers, or datasets, please cite as below."
type: dataset
title: "Dr. Ye's Collected Representative Works, Monographs, and Datasets (DaKES)"
version: 2026.11
doi: 10.5281/zenodo.23886305
date-released: 2026-11-01
url: "{REPO_URL}"
license: CC-BY-4.0
authors:
  - family-names: "Ye"
    given-names: "Fred Y."
    affiliation: "DaKES Institute"
"""
    Path("CITATION.cff").write_text(cff_content, encoding="utf-8")

    # 4. 生成全量 BibTeX 文献库 references.bib
    bib_lines = []
    for idx, p in enumerate(PUBLICATIONS, 1):
        entry_type = "book" if p["cat"] == "Monographs" else ("dataset" if p["sub"] == "Dataset" else "article")
        key = f"Ye2026_{p['cat'][:4]}_{idx:02d}"
        bib_lines.append(f"@{entry_type}{{{key},\n  author = {{{AUTHOR}}},\n  title = {{{p['title']}}},\n  year = {{2026}},\n  date = {{{p['date']}}},\n  doi = {{{p['doi']}}},\n  url = {{{p['url']}}}\n}}\n")
    Path("references.bib").write_text("\n".join(bib_lines), encoding="utf-8")
    print("[SUCCESS] Generated README.md, CITATION.cff, references.bib, and disciplinary folders!")

if __name__ == "__main__":
    build_repository()