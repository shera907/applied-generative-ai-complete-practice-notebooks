# 🧠 Basic RAG Architecture

This notebook explains the **minimal, correct architecture**
for a Retrieval-Augmented Generation (RAG) system.

You will learn:
- What RAG actually is (and is not)
- The canonical RAG pipeline
- Why each component exists
- Where hallucinations originate
- What makes a RAG system “basic but correct”

This notebook is about **architecture**, not libraries.

## 1. What Is RAG?

Retrieval-Augmented Generation (RAG) is an architecture where:

- Retrieval provides grounding facts
- Generation provides language and synthesis

Formally:
> Answer = LLM( Query + Retrieved Context )

The LLM does NOT store knowledge.
Knowledge lives outside the model.

## 2. What RAG Is NOT

RAG is NOT:
- a prompt trick
- a larger context window
- fine-tuning with documents
- guaranteed correctness

RAG reduces hallucination.
It does not eliminate it.

## 3. The Canonical RAG Pipeline

A basic RAG system has exactly these stages:

1. User Query
2. Query Embedding
3. Vector Search
4. (Optional) Metadata Filtering
5. Context Selection
6. Prompt Construction
7. LLM Generation
8. Output

Every production RAG system is a variation of this.

## 4. Step 1: User Query

The user provides:
- a question
- often ambiguous
- often underspecified

Important:
> The query is NOT yet suitable for retrieval.

## 5. Step 2: Query Embedding

The query is converted into a vector.

This vector represents:
- semantic intent
- not correctness
- not completeness

If query intent is unclear,
retrieval will drift.

## 6. Step 3: Vector Search

Vector search retrieves:
- top-K semantically similar chunks

It answers:
> “What looks related?”

It does NOT answer:
> “What is correct?”

## 7. Step 4: Metadata Filtering

Metadata filtering enforces constraints:

- domain
- document type
- time
- permissions

This step prevents:
- wrong-but-similar retrieval
- data leakage
- compliance failures

## 8. Step 5: Context Selection

From retrieved chunks:
- select a small, relevant subset
- discard noisy candidates

More context ≠ better answers.

Noise increases hallucination.

## 9. Step 6: Prompt Construction

The system prompt now includes:
- task instruction
- retrieved context
- constraints

The LLM is told:
> “Answer ONLY using this context.”

This is grounding, not trust.

## 10. Step 7: LLM Generation

The LLM:
- synthesizes an answer
- using retrieved text
- shaped by the prompt

The LLM still:
- predicts tokens
- does not verify truth

## 11. Step 8: Output

The output should ideally include:
- answer
- citations
- uncertainty if context is missing

Absence of context
should result in refusal, not fabrication.

## 12. Where Hallucinations Originate

In RAG, hallucinations usually come from:

1. Missing chunks
2. Bad chunking
3. Weak metadata filtering
4. No refusal policy

Rarely from:
- the LLM itself

## 13. Mental Model Diagram

```text
User Question
      ↓
  Embedding
      ↓
Vector Search ──→ Metadata Filter
      ↓
 Top-K Chunks
      ↓
Prompt + Context
      ↓
     LLM
      ↓
    Answer
```

## 14. What Makes This Architecture Correct

This RAG is correct because:

- Knowledge is external
- Retrieval is explicit
- Context is controlled
- Generation is grounded

Nothing fancy.
Nothing unsafe.

## 15. Common Mistakes

❌ Injecting entire documents  
❌ No metadata filtering  
❌ Large K “just in case”  
❌ No refusal behavior  
❌ Prompt-only grounding  

These cause silent failure.

## Final Mental Lock

RAG is not about smarter models.

RAG is about:
> moving knowledge out of the model
> and controlling how it enters.

## Self-Check

You understand this notebook if you can explain:

- Why retrieval comes before generation
- Why similarity is not correctness
- Why metadata matters
- Why RAG reduces hallucination

Every advanced RAG system
is just this architecture with:

- better retrieval
- better filtering
- better evaluation
- better control

Master this first.
Everything else is optimization.

