---
layout: project
title: "Interactive Website Modeling and Trajectory Generation"
subtitle: "Lead developer & system designer"
---

**Time.** 2024  
**Affiliation.** XLANG Lab, The University of Hong Kong  
**Role.** Lead developer & system designer  

**Tagline.** Turn live, dynamic websites into executable “web worlds” with replayable trajectories for agents.

**Summary.** This project builds a pipeline that converts messy, dynamic websites into structured environments via human-like exploration, deterministic replay, and automated trajectory quality scoring, so that web agents can be trained and evaluated in a stable, resettable setting.

**Highlights.**
- Designed the **expand → record → replay → curate** loop: actively exposes dynamic UI (flyouts, modals, pagination, forms) with click/scroll/form actions while logging DOM deltas at each step.
- Maintained an **accessibility-tree–centric state** that keeps only meaningful UI elements (buttons, links, inputs) and stable mappings between actions, locators, and UI semantics.
- Built **navigation DAGs** that capture how actions transition across URLs, enabling deterministic replays and brittle-path diagnosis when DOMs drift or selectors break.
- Implemented an **LLM-as-judge evaluator** that rates trajectories on Completeness, Complexity, Conciseness, Concreteness, and Diversity, achieving around 70% agreement with human raters.
- Provides **resettable environments** for downstream planning, grounding, and trajectory generation tasks, avoiding brittle one-off static scrapes.

**Keywords.** Web agents, interactive web, world modeling, trajectory generation, accessibility tree, LLM-as-judge.

**Links.** Internal research prototype; no public repository currently available.