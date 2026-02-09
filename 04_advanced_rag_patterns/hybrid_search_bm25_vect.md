# 🧠 Hybrid Search: BM25 + Vector Search

This notebook explains **why neither keyword search nor vector search
is sufficient alone**, and how combining them produces
more reliable, controllable retrieval systems.

You will learn:
- Why vector search fails on precision
- Why BM25 fails on meaning
- How hybrid search works conceptually
- Common hybrid fusion strategies
- When hybrid search is worth the cost

Hybrid search is not a hack.
It is a design correction.

## 1. Two Retrieval Philosophies

There are two fundamentally different ways to retrieve text:

1. Lexical retrieval (BM25)
2. Semantic retrieval (embeddings)

They answer different questions.

## 2. BM25 (Keyword Search)

BM25 retrieves documents based on:
- exact token matches
- term frequency
- inverse document frequency

BM25 is good at:
- exact terms
- numbers
- identifiers
- legal clauses

BM25 answers:
> “Does this text contain these words?”

## 3. Vector Search

Vector search retrieves based on:
- semantic similarity
- contextual meaning
- paraphrases

Vector search is good at:
- intent matching
- synonyms
- fuzzy queries

Vector search answers:
> “Does this text mean something similar?”

## 4. Failure Modes

BM25 fails when:
- user uses synonyms
- phrasing differs
- intent ≠ keywords

Vector search fails when:
- exact terms matter
- numbers or codes matter
- legal / technical precision matters

## 5. Core Idea

Hybrid search combines:

- BM25 → precision
- Vectors → recall

The goal:
> retrieve candidates that are both relevant AND precise

## 6. Hybrid Architectures

Typical patterns:

1. BM25 first → vector reranking
2. Vector first → BM25 filtering
3. Parallel retrieval → score fusion

All are valid depending on constraints.

## 7. Parallel Hybrid Retrieval

Process:
- Run BM25 search
- Run vector search
- Merge results
- Combine scores

This preserves:
- recall
- precision
- flexibility

## 8. Score Fusion

Common fusion methods:

- Weighted sum
- Rank-based fusion
- Reciprocal rank fusion (RRF)

Fusion strategy matters as much as retrieval.

## 9. Hallucination Reduction

Hybrid search:
- filters out semantically related but wrong chunks
- enforces exact constraints
- narrows answer space

Better retrieval = fewer gaps = less hallucination.

## 10. When Hybrid Search Is Worth It

Hybrid search is recommended when:
- domain is legal / medical / finance
- identifiers or numbers matter
- users ask vague questions
- corpus is large and diverse

It is often overkill for small corpora.

## 11. Hybrid Search vs Metadata Filtering

Metadata filtering:
- enforces hard constraints

Hybrid search:
- improves candidate quality

They are complementary, not substitutes.

## 12. Failure Modes

❌ Poor score normalization  
❌ Overweighting one modality  
❌ Increased latency  
❌ Debugging complexity  

Hybrid search must be observable.

## 13. Design Checklist

Before adopting hybrid search:

- Do exact terms matter?
- Is vector search alone noisy?
- Can latency budget handle dual retrieval?
- Is evaluation in place?

If yes → hybrid search is justified.

## Final Mental Lock

Vector search finds meaning.
BM25 enforces words.

Hybrid search enforces **meaning with discipline**.

## Self-Check

You understand this notebook if you can explain:

- Why BM25 still matters
- Why vectors alone are insufficient
- How hybrid fusion works conceptually
- When hybrid search reduces hallucination

Hybrid search is not about adding complexity.

It is about respecting that:
language has both meaning and structure.

Good retrieval respects both.
