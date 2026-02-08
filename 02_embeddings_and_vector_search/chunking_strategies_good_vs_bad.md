# 🧠 Chunking Strategies: Good vs Bad

This notebook explains **why chunking is the single most important
design decision in Retrieval-Augmented Generation (RAG)**.

You will learn:
- What chunking actually does
- Why naive chunking fails
- How bad chunking causes hallucinations
- How to design chunks that retrieve meaning, not noise

📌 Rule:
> Bad chunking = bad RAG (no exceptions)

## 1. What Chunking Really Is

Chunking is the process of:

> Breaking source documents into retrievable units
> that embeddings and similarity search can work with

Chunking is NOT:
- text splitting
- a preprocessing detail
- something embeddings “fix”

## 2. Why Chunking Exists

LLMs and vector search have constraints:
- limited context windows
- finite embedding size
- similarity works on chunks, not documents

Chunking is:
> how meaning is exposed to retrieval

## 3. Bad Chunking Anti-Patterns

- ❌ Fixed-size splitting (e.g., every 500 tokens)
- ❌ Splitting by characters blindly
- ❌ Ignoring document structure
- ❌ Mixing unrelated topics in one chunk
- ❌ Chunks that are too small or too large

## 4. Why Fixed-Size Chunking Fails

Fixed-size chunking:
- cuts concepts mid-thought
- separates definitions from usage
- breaks logical continuity

Embeddings capture:
> partial meaning → noisy vectors

## 5. Two Chunking Failure Modes

1. Chunks too small:
   - lose context
   - increase ambiguity
   - retrieve fragments

2. Chunks too large:
   - dilute meaning
   - include irrelevant content
   - reduce retrieval precision

## 6. Good Chunking Principles

Good chunks are:
- semantically coherent
- self-contained
- aligned with human understanding

A chunk should answer:
> “What is this about?”

## 7. Structure-Aware Chunking

Prefer chunking by:
- headings
- sections
- paragraphs
- logical boundaries

Documents already encode meaning.
Use it.

## 8. Chunk Overlap

Overlap helps when:
- concepts span boundaries
- references cross sections

But overlap:
- increases storage
- increases retrieval noise

Use overlap intentionally, not blindly.

## 9. Chunking Is Query-Dependent

Chunk size depends on:
- expected question type
- granularity of answers
- domain precision

Legal, medical, and technical docs
require smaller, precise chunks.

## 10. Metadata Is Part of Chunking

A good chunk includes:
- source
- section title
- timestamps
- document type

Metadata helps:
- filtering
- reranking
- grounding

## 11. Chunking and Hallucination

Bad chunking causes:
- missing facts
- partial truths
- vague retrieval

The LLM fills gaps with hallucination.

Hallucination often starts at chunking.

## 12. Good vs Bad Chunking

| Bad Chunking | Good Chunking |
|-------------|---------------|
| Fixed-size | Semantic |
| Blind splitting | Structure-aware |
| Mixed topics | Single concept |
| No metadata | Rich metadata |

## Final Mental Lock

Chunking decides:
- what retrieval sees
- what the model can ground on

If chunking is wrong,
everything downstream lies.

## Self-Check

You understand this notebook if you can explain:

- Why fixed-size chunking fails
- Why chunk size is domain-dependent
- Why overlap is a tradeoff
- Why chunking affects hallucination

Chunking is not preprocessing.

It is **knowledge architecture**.

Treat it with the same care
as database schema design.












