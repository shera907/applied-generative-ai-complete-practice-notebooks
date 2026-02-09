# 🧠 Retrieval Failures Analysis

This notebook provides a **structured framework to analyze and debug
retrieval failures in RAG systems**.

You will learn:
- The major classes of retrieval failure
- How to distinguish retrieval failure from generation failure
- Why “top-K looks fine” is often misleading
- A repeatable workflow to diagnose issues

If you cannot explain *why* retrieval failed,
you cannot reliably fix RAG.

## 1. First Principle

Before debugging anything, enforce this rule:

> If the correct chunk is NOT retrieved,
> the LLM is not at fault.

Generation can only work with what retrieval provides.

## 2. What Is a Retrieval Failure?

Retrieval failure occurs when:

- The correct document exists
- But the correct chunk is not surfaced
- Or is surfaced too low to be used
- Or is mixed with misleading context

This includes:
- partial retrieval
- noisy retrieval
- wrong-but-similar retrieval

## 3. Retrieval Failure Taxonomy

Most failures fall into one of these categories:

1. Query failure
2. Chunking failure
3. Embedding failure
4. Similarity metric failure
5. Metadata filtering failure
6. Ranking / selection failure

## 4. Query Failure

Symptoms:
- Slight rephrasing changes results drastically
- Retrieval matches keywords, not intent

Causes:
- Ambiguous queries
- Missing constraints
- Overloaded questions

This is not an embedding problem.

### Diagnostic Questions

- Is the user intent clear?
- Does the query mix multiple tasks?
- Would a human need clarification?

## 5. Chunking Failure

Symptoms:
- Answer exists but split across chunks
- Retrieved chunks are vague or incomplete

Causes:
- Chunks too large (semantic dilution)
- Chunks too small (context loss)
- Fixed-size splitting

Chunking is the #1 root cause of RAG failure.

## 6. Embedding Failure

Symptoms:
- Top results are topically related but useless
- Important domain terms ignored

Causes:
- Domain mismatch
- Poor embedding model choice
- Ambiguous language

Embeddings capture association, not task relevance.

## 7. Similarity Metric Failure

Symptoms:
- Long documents dominate results
- Precise chunks are ranked lower

Causes:
- Dot product used with non-normalized vectors
- Metric mismatch with embedding model

This is a math + assumption mismatch.

## 8. Metadata Filtering Failure

Symptoms:
- Old policies retrieved
- Wrong domain or jurisdiction
- Internal docs exposed externally

Causes:
- Missing metadata
- Incorrect filters
- Filtering applied after retrieval

This is a system design failure.

## 9. Ranking & Selection Failure

Symptoms:
- Correct chunk is in top-K
- But not used by the LLM

Causes:
- K too large
- No reranking
- Context stuffing

Retrieval ≠ context injection.

## 10. Why “Top-K Looks Fine” Is Misleading

Common trap:
> “The correct chunk is in top-10, so retrieval works.”

Reality:
- The LLM only attends to a fraction of context
- Noise overwhelms signal
- Wrong chunks bias generation

Correctness at rank 7 is often useless.

## 11. Retrieval vs Generation Failure Test

Ask:

“If I gave the retrieved chunks to a human,
could they answer correctly?”

If no:
- retrieval failed

If yes:
- generation or prompting failed

## 12. Retrieval Debug Workflow

1. Log the user query
2. Log top-K retrieved chunks
3. Inspect chunks manually
4. Classify failure type
5. Fix the earliest failing layer
6. Re-test before changing anything else

## 13. What NOT to Do

❌ Increase temperature  
❌ Add more prompt instructions  
❌ Switch to a larger LLM  
❌ Increase context window blindly  

These hide the problem.

## 14. Failure → Fix Mapping

| Failure Type | Primary Fix |
|-------------|-------------|
| Query failure | Query rewriting |
| Chunking failure | Semantic chunking |
| Embedding failure | Better model / domain tuning |
| Metric failure | Align similarity metric |
| Metadata failure | Structured filters |
| Ranking failure | Reranking / smaller K |

## Retrieval Mental Model

Retrieval is a pipeline, not a step.

Failure anywhere upstream
propagates downstream as hallucination.

## Self-Check

You understand this notebook if you can explain:

- Why retrieval failures masquerade as hallucinations
- How to classify retrieval failures
- Why fixing the earliest layer matters
- Why prompts rarely fix retrieval issues

Good RAG systems are not lucky.

They are debuggable.

If retrieval is observable and classifiable,
it is fixable.

