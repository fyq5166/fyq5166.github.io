---
layout: project
title: "Agent Tool Calling Ability Evaluation Framework"
subtitle: "Independent prototype on top of Arkitect (Volcengine Ark Group)"
---

**Time.** Summer 2025  
**Affiliation.** ByteDance Volcengine Ark Group  
**Role.** Agent Systems Intern; sole designer & implementer of the prototype  

**Tagline.** Making Arkitect agents measurable and diagnosable via modular tool-calling tests and transparent logs.

**Summary.**  
This project turns Arkitect from a “tool-using SDK” into something that can also evaluate tool use. I designed and implemented a prototype framework that registers heterogeneous tools, runs them through configurable test suites, validates outcomes with both rules and LLM-as-judge checks, and emits human-readable logs so that failures are explainable rather than opaque. It serves as a research-style foundation for future tool-calling benchmarks inside the Arkitect ecosystem.

**Highlights.**
- Built a tool registration layer that handles local functions, HTTP APIs, and MCP tools behind a unified interface, reusing Arkitect’s context/hook abstractions.
- Designed a test-suite schema so engineers can write small YAML/JSON scenarios instead of hard-coding evaluation scripts.
- Implemented hybrid validation: rule-based checks for structured outputs plus LLM-as-judge scoring for open-ended answers.
- Added end-to-end logging that records prompts, tool invocations, intermediate observations, decisions, and verdicts in a compact, human-readable format.
- Used the framework to probe Arkitect agents under different prompting styles (few-shot, chain-of-thought, code-enforced flows) and to surface where failures come from—prompting, tool wiring, or model behavior.
- Integrated via internal PRs into the Arkitect codebase as an independent, research-oriented prototype for systematic tool-calling evaluation.

**Keywords.** LLM agents, tool calling, evaluation, Arkitect, MCP, logging, observability.

**Links.** Built on Arkitect within Volcengine (internal codebase; no public repository).