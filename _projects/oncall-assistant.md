---
layout: project
title: "Automated Oncall Assistant for SRE Teams"
subtitle: "Agent Systems Intern – primary prototype developer, Volcano Engine Ark Group"
---

**Time.** Summer 2025  
**Affiliation.** ByteDance Volcengine Ark Group – SRE Intelligence  
**Role.** Primary prototype developer & system architect  

**Tagline.** LLM-powered oncall copilot that fuses triggers, observability context, RAG, and human feedback loops.

**Summary.** Built a production-facing prototype that ingests noisy incident streams, augments them with dashboards and SOPs, and replies to engineers with context-aware guidance.

**Highlights.**
- Designed ingestion and governance pipelines that clean alerts, deduplicate signals, and mine 1K+ historical incidents to auto-surface relevant Grafana dashboards and visuals.
- Implemented multi-layer triggers with severity-aware “politeness windows” so the agent only intervenes when helpful, avoiding alert fatigue.
- Built a Viking-based two-tier RAG stack (hot SOP snippets + cold KB) plus ToS-compliant screenshot handling to attach visual context safely.
- Added Lark-card feedback for Answer Adoption, Time-to-Helpful, and qualitative labels, enabling human-in-the-loop evaluation and future fine-tuning.
- Managed storage migration and capacity scaling during live pilots with SRE teams.

**Keywords.** LLM agents, SRE, oncall, RAG, observability, human-in-the-loop, production systems.

**Links.** Internal production prototype (no public repository).