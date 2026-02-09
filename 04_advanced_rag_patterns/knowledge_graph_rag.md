# 🧠 Knowledge Graph RAG

This notebook explains **Knowledge Graph–augmented RAG** —
an architecture that combines structured relationships
with unstructured retrieval.

You will learn:
- Why vector search fails on relational queries
- What knowledge graphs add (and what they don’t)
- How KG + RAG architectures work
- When KG RAG is worth the complexity
- Common failure modes and misconceptions

Knowledge graphs add structure.
RAG adds language.
Together, they add precision.

## 1. The Limits of Vector RAG

Vector search is excellent at:
- topical similarity
- paraphrases
- fuzzy intent

Vector search is bad at:
- multi-hop reasoning
- explicit relationships
- constraints across entities

Example failure:
"Which vendors supply parts used in Product X?"

Similarity alone cannot answer this reliably.

## 2. What Is a Knowledge Graph?

A knowledge graph represents:

- entities (nodes)
- relationships (edges)
- attributes (properties)

Formally:
> Facts expressed as (subject, relation, object)

Example:
(Product X) — uses → (Component Y)
(Component Y) — supplied_by → (Vendor Z)

## 3. What KGs Are Good At

Knowledge graphs excel at:
- explicit relationships
- multi-hop queries
- constraints and rules
- provenance and lineage

They are NOT good at:
- natural language generation
- fuzzy similarity
- paraphrase understanding

## 4. Why KG Alone Is Not Enough

Knowledge graphs:
- are brittle to language
- require exact schema
- are expensive to maintain

They struggle with:
- vague questions
- unstructured documents
- incomplete data

This is why KG ≠ GenAI replacement.

## 5. Division of Labor

In KG RAG:

- Knowledge Graph → structure & relationships
- Vector RAG → language & evidence
- LLM → synthesis & explanation

Each does what it is good at.

## 6. KG RAG Architecture
``` text
User Query
   ↓
Query Interpretation
   ↓
KG Query (entities + relations)
   ↓
Relevant Subgraph
   ↓
RAG Retrieval (documents about entities)
   ↓
Context Injection
   ↓
LLM Answer + Citations
```

## 7. KG-First Pattern

Use KG-first when:
- relationships define relevance
- constraints must be enforced
- multi-hop reasoning is required

The graph narrows the search space
before vector retrieval.

## 8. RAG-First Pattern

Use RAG-first when:
- query intent is unclear
- entities must be discovered
- language is vague

RAG extracts candidate entities,
then the KG validates relationships.

## 9. Example Query

"Which GDPR articles apply to data processors handling health data?"

Steps:
1. KG finds:
   - data processor
   - health data
   - GDPR articles
2. KG traverses applicable relations
3. RAG retrieves article text
4. LLM explains applicability

## 10. Hallucination Reduction

KG RAG reduces hallucination by:
- enforcing valid relationships
- preventing invalid entity combinations
- limiting answer space structurally

The model cannot invent edges
that don’t exist in the graph.

## 11. Failure Modes

❌ Incomplete or stale graphs  
❌ Over-trusting the graph  
❌ Schema rigidity blocking valid answers  
❌ Treating KG as “truth oracle”  
❌ Poor entity resolution  

## 12. Scope Control

A KG should model:
- stable relationships
- high-value structure

Do NOT put:
- every sentence
- fast-changing facts
- free text

Graphs rot faster than text if overextended.

## 13. KG RAG vs Fine-Tuning

KG RAG:
- explicit knowledge
- explainable relationships
- auditable

Fine-tuning:
- implicit patterns
- opaque reasoning
- hard to debug

KG RAG favors correctness over fluency.

## 14. When KG RAG Is Worth It

Use KG RAG when:
- relationships are first-class
- compliance matters
- explanations must be defensible
- errors are expensive

Avoid it for:
- small corpora
- purely descriptive Q&A

## Final Mental Lock

Vector RAG answers:
> “What is related?”

Knowledge Graph RAG answers:
> “What is allowed to be related?”

That difference enables reasoning.

## Self-Check

You understand this notebook if you can explain:

- Why vector RAG fails on multi-hop queries
- What KGs add that embeddings cannot
- When to query KG first vs RAG first
- Why KG RAG reduces hallucination

Knowledge graphs do not make models smarter.

They make systems **more disciplined**.

Discipline is what enables trust.


