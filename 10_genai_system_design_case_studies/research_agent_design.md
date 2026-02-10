# 🧠 Research Agent Design

This notebook explains how to design **research agents**
that can explore information, synthesize insights, and assist humans
without becoming unsafe, unbounded, or hallucination-prone.

You will learn:
- What a research agent actually is (and is not)
- Why naive autonomous agents fail
- Core architectural components of a research agent
- How to bound exploration, reasoning, and output
- Evaluation and safety strategies for research agents

📌 Core principle:
> A research agent explores.
> Humans decide.

## 1. What Is a Research Agent?

A research agent is a system that:
- breaks a research goal into sub-questions
- retrieves information from multiple sources
- synthesizes findings
- presents structured outputs with citations

It is NOT:
- a decision-maker
- a truth oracle
- an autonomous authority

## 2. Inherent Risks

Research agents combine:
- retrieval uncertainty
- synthesis hallucinations
- long reasoning chains
- apparent authority

This creates:
> high confidence + incomplete evidence

Which is the most dangerous failure mode.

## 3. Key Distinctions

Search:
- retrieves documents
- no synthesis

RAG:
- answers a question from retrieved context
- bounded by input

Research Agent:
- decomposes questions
- performs multiple retrievals
- synthesizes across sources

Power increases risk.

## 4. Reference Architecture

```test
User Research Question
 ↓
Problem Decomposition
 ↓
Query Planning
 ↓
Iterative Retrieval (Search / RAG)
 ↓
Evidence Store
 ↓
Synthesis Engine
 ↓
Validation & Citation Checks
 ↓
Structured Research Output
 ↓
Human Review
```

## 5. Decomposition

The agent decomposes:
- broad questions → specific sub-questions

Rules:
- limit number of sub-questions
- make sub-questions explicit
- expose decomposition to the user

Hidden decomposition = hidden bias.

## 6. Query Planning

Planning defines:
- which sources to query
- how many iterations
- stop conditions

Exploration must be:
- time-bounded
- depth-bounded
- cost-bounded

## 7. Retrieval

Retrieval sources may include:
- web search
- internal documents
- academic databases
- APIs

Rules:
- log all queries
- track source credibility
- avoid recursive retrieval loops

## 8. Evidence Store

The agent must maintain:
- raw retrieved content
- source metadata
- timestamps
- confidence scores

Synthesis must only reference
stored evidence.

## 9. Synthesis Risk

Synthesis failures include:
- overgeneralization
- cherry-picking sources
- false consensus
- invented connections

Synthesis must be:
- conservative
- evidence-linked
- uncertainty-aware

## 10. Citation Enforcement

Every claim must:
- reference one or more sources
- include source identifiers
- allow trace-back to evidence

Uncited claims are invalid.

## 11. Conflicts

Good research agents:
- surface disagreements
- compare sources
- avoid forced conclusions

Conflict is information,
not failure.

## 12. Structured Outputs

Research outputs should include:
- executive summary
- key findings
- supporting evidence
- open questions
- limitations

Free-form essays hide uncertainty.

## 13. Human Review

Humans must:
- review evidence
- approve conclusions
- challenge assumptions

Agents assist thinking.
They do not replace it.

## 14. Guardrails

Validate:
- citation presence
- claim-evidence alignment
- source diversity
- prohibited content

Reject outputs
that violate research integrity.

## 15. Evaluation Metrics

Key metrics:
- citation coverage
- evidence diversity
- faithfulness
- uncertainty expression
- human satisfaction

Accuracy alone is meaningless.

## 16. Cost & Latency

Research agents are expensive due to:
- multiple retrievals
- long contexts
- synthesis steps

Mitigations:
- hard iteration caps
- early stopping
- tiered models

## 17. Anti-Patterns

❌ Fully autonomous research  
❌ No evidence store  
❌ No citations  
❌ Forced conclusions  
❌ No human review  

## Final Mental Lock

A research agent’s job
is not to be right.

It is to help humans
reason better with evidence.

## Self-Check

You understand this notebook if you can explain:

- Why research agents are high-risk
- Why synthesis is the most dangerous step
- Why evidence stores are mandatory
- Why humans must remain decision-makers

The more intelligent a research agent appears,
the more dangerous it becomes
without explicit bounds.

Design agents that respect
the limits of knowledge.




