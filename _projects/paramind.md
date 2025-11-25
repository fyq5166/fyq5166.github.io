---
layout: project
title: "ParaMind: Collaborative Large Language Model Inference Platform"
subtitle: "FYP student – system architect & implementer"
---

**Time.** 2025–present  
**Affiliation.** The University of Hong Kong (Final Year Project)  
**Role.** FYP owner (architecture + implementation)  

**Tagline.** P2P collaborative inference platform that aims to stitch consumer GPUs into one logical accelerator.

**Summary.** ParaMind is an ongoing FYP exploring how households of heterogeneous devices can jointly serve large LLMs by combining pipeline/tensor parallelism, NAT traversal, and transparent scheduling. The current focus is on designing the end-to-end architecture and building a working multi-peer prototype.

**Highlights.**
- Designing a peer-to-peer overlay where layers or segments are distributed across peers and activations are streamed via hole punching with relay fallbacks when NAT traversal fails.
- Integrating Hugging Face Accelerate `big_modeling` offload to maximize single-node capacity, while coordinating multi-peer execution with static cut points and KV-cache reuse.
- Building a chat-style interface and orchestration service so users can submit prompts once and have the system schedule segments across peers transparently.
- Investigating reliability and fairness mechanisms (peer availability scoring, checksum verification) to keep collaborative inference robust under churn.

**Keywords.** Distributed inference, P2P, pipeline parallelism, systems for ML.

**Links.** Work in progress – FYP repo, report, and slides to be released after project completion.