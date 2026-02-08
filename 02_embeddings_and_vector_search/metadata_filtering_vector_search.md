# 🧠 Metadata Filtering in Vector Search

This notebook explains **why embeddings alone are insufficient**
and how metadata filtering turns vector search into
a controllable, production-grade retrieval system.

You will learn:
- What metadata actually is in RAG
- Why pure semantic search fails
- How metadata reduces hallucination
- How filtering, not prompting, enforces constraints

📌 Core idea:
> Vector similarity finds candidates.
> Metadata decides eligibility.

## 1. The Problem with Pure Vector Search

Pure vector search answers:
> “What is semantically similar?”

But real systems need:
- correct time period
- correct document type
- correct permissions
- correct domain

Similarity alone cannot enforce any of these.

## 2. What Metadata Really Is

Metadata is:
> Structured attributes attached to chunks

Examples:
- source document
- section title
- author
- date / version
- access level
- domain / category

Metadata is **not language**.
It is **control information**.

## 3. Why Embeddings Cannot Replace Metadata

Embeddings encode:
- semantic similarity
- topical association

They do NOT encode:
- time
- authority
- permissions
- correctness constraints

Trying to encode rules into embeddings
creates brittle, opaque systems.

## 4. Candidate → Filter Mental Model

Retrieval should be two-stage:

1. Vector search:
   - find semantically relevant candidates

2. Metadata filtering:
   - remove invalid candidates

Only then:
- rerank
- generate

## 5. Common Metadata Filters

Typical filters include:

- document_type = policy | faq | contract
- date >= last_updated
- domain = finance | legal | medical
- user_role = allowed / denied
- language = en | fr | de

These cannot be reliably enforced by prompts.

## 6. Why Metadata Reduces Hallucination

Hallucination often starts when:
- retrieved chunks are “kind of related”
- but factually invalid

Metadata filtering:
- removes wrong-but-similar chunks
- reduces knowledge gaps
- narrows answer space

Less ambiguity → less hallucination.

## 7. Pre-Filter vs Post-Filter

Pre-filter:
- restricts search space before vector search
- faster
- safer

Post-filter:
- filters after similarity search
- flexible
- may waste retrieval budget

Good systems often use both.

## 8. Metadata Depends on Chunking

Metadata is attached to chunks.

Bad chunking:
- breaks metadata usefulness
- mixes scopes and permissions
- leaks context

Good chunking:
- clean semantic units
- precise metadata
- predictable filtering

## 9. Metadata as a Security Boundary

Never rely on prompts to enforce:
- access control
- document visibility
- tenant separation

Metadata filtering enforces:
> “What the model is allowed to see”

This must happen **before generation**.

## 10. Metadata vs Reranking

Metadata filtering:
- removes invalid candidates

Reranking:
- orders valid candidates

Do not confuse:
- exclusion
with
- prioritization

## 11. Failure Patterns Without Metadata

❌ Old policy cited as current  
❌ Internal doc shown to external user  
❌ Legal answer mixing jurisdictions  
❌ Medical advice from blog content  

All are retrieval failures, not model failures.

## 12. Minimal Metadata Schema

At minimum, each chunk should have:

- source_id
- section_title
- created_at / updated_at
- domain
- access_level

This enables:
- filtering
- auditing
- debugging

## Final Mental Lock

Embeddings answer:
> “What is similar?”

Metadata answers:
> “What is allowed?”

Production RAG requires both.

## Self-Check

You understand this notebook if you can explain:

- Why semantic similarity is insufficient
- Why metadata must be structured
- Why filtering must happen before generation
- Why metadata reduces hallucination

If embeddings are the “brain” of retrieval,
metadata is the “law”.

Without law,
even a smart brain causes harm.
