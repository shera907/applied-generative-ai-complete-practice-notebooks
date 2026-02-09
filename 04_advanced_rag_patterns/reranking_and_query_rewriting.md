# 🧠 Reranking & Query Rewriting

This notebook explains **two of the highest-ROI techniques in RAG systems**:

1. Reranking — choosing the best chunks from retrieved candidates
2. Query rewriting — fixing user queries before retrieval

You will learn:
- Why top-K retrieval is rarely enough
- Why the first query is often wrong
- How reranking improves precision
- How query rewriting improves intent alignment

These techniques fix retrieval **without changing embeddings or models**.

## 1. The “Almost Works” Problem

Common situation:
- Correct chunk is retrieved
- But ranked too low
- Or overshadowed by noise

The system fails even though:
> the knowledge exists and is retrievable

## 2. Two Separate Problems

Retrieval actually has two stages:

1. Candidate generation (recall)
2. Candidate selection (precision)

Vector search is good at #1.
Reranking solves #2.

## 3. What Is Reranking?

Reranking means:
> Re-ordering retrieved candidates
> using a stronger, more expensive signal

Typically:
- Vector search → top-K (cheap)
- Reranker → top-N (expensive, precise)

## 4. Limits of Vector Similarity

Vector similarity:
- measures semantic closeness
- ignores task relevance
- ignores constraints

Two chunks can be similar
but only one answers the question.

## 5. Reranking Signals

Common reranking inputs:
- full query + chunk text
- cross-encoder scores
- LLM relevance judgments
- heuristic features (recency, authority)

Rerankers are selective, not exhaustive.

## 6. Cross-Encoder Reranking

Cross-encoders:
- read query and chunk together
- score relevance directly
- are slower but more precise

They answer:
> “Does this chunk answer this question?”

## 7. LLM-Based Reranking

LLMs can rerank by:
- scoring relevance
- classifying usefulness
- selecting best evidence

This is powerful but:
- expensive
- must be bounded
- must be observable

## 8. Reranking Failure Modes

❌ Over-trusting the reranker  
❌ Reranking too many candidates  
❌ Latency blow-ups  
❌ Using reranking to fix bad chunking  

Reranking refines retrieval.
It does not rescue broken retrieval.

## 9. Query Rewriting

Many retrieval failures happen because:
> the user asked the wrong question

Query rewriting reformulates the query
to better match the knowledge base.

## 10. Why Queries Are Bad

User queries are often:
- ambiguous
- underspecified
- conversational
- overloaded

Embeddings cannot infer missing intent reliably.

## 11. Query Rewriting Patterns

Common patterns:
- Clarification (“What policy version?”)
- Expansion (add implied constraints)
- Decomposition (split multi-part queries)
- Normalization (remove conversational fluff)

## 12. Rewrite Before Embedding

Best practice:
> Rewrite query → THEN embed

Embedding the raw query
locks in ambiguity.

## 13. Rewriting vs Agents

Query rewriting:
- deterministic
- bounded
- cheap

Agents:
- dynamic
- flexible
- risky

Prefer rewriting before introducing agents.

## 14. Combined Retrieval Flow

```text
User Query
   ↓
Query Rewriting
   ↓
Vector / Hybrid Retrieval (top-K)
   ↓
Reranking (top-N)
   ↓
Context Injection
   ↓
Generation
```

## 15. High-Impact Scenarios

Reranking & rewriting shine when:
- corpus is large
- questions are vague
- precision matters
- hallucination risk is high

They are often higher ROI
than model upgrades.

## Final Mental Lock

Bad answers often come from:
- bad questions
- bad ranking

Fix those before:
- changing embeddings
- changing models
- changing prompts

## Self-Check

You understand this notebook if you can explain:

- Why top-K retrieval is insufficient
- How reranking improves precision
- Why query rewriting must happen first
- When reranking is worth the cost

The biggest RAG wins rarely come from new models.

They come from:
- asking better questions
- choosing better evidence

Reranking and rewriting do exactly that.
