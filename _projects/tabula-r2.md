---
layout: project
title: "TABULA-R²: A Reproducible Tabular Reasoning Benchmark for Local LLMs"
subtitle: "Independent research with Prof. Philipp Koehn (Johns Hopkins University)"
---

**Time.** 2025  
**Affiliation.** Johns Hopkins University (remote) + The University of Hong Kong  
**Role.** Independent researcher; end-to-end designer & sole implementer  

**Tagline.** Fully reproducible PLAN/END benchmark for evaluating multi-table reasoning of locally deployed LLMs.

**Summary.** TABULA-R² decouples genuine reasoning ability from formatting tricks by forcing models to emit executable programs before answering, across realistic data from Our World in Data.

**Highlights.**
- Curated and cleaned 129+ tables spanning health, economics, environment, demographics, and education, grouped into coherent multi-table collections.
- Authored and validated 263 human-written questions (single-table, multi-table, distractor variants) covering arithmetic, conditional logic, language inference, and entity alignment.
- Designed a PLAN/END prompting protocol plus a lightweight DSL (filter, aggregate, join, align) so models must output reasoning plans that my Python executor can run deterministically.
- Implemented a robust executor + unified validator that tolerates minor formatting drift and can fall back to a local LLM judge for True/False adjudication.
- Produced 80+ pages of behavioral analysis: multi-table contexts halve success rates, distractors only help when they clarify schema, and strict protocols can let zero-shot prompts beat few-shot/CoT.
- Shipping as a complete artifact with data, code, and documentation for reproducible benchmarking.

**Keywords.** LLMs, tabular reasoning, benchmark, DSL, evaluation, reproducibility.

**Links.** [GitHub repository](https://github.com/fyq5166/TABULA-R2) • [Technical report (PDF)](https://drive.google.com/file/d/1_K5ld4YPc3cvkS7EZVTyWf65wjK4QG-E/view?usp=sharing)