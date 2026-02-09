# 🧠 Grounding & Citation in RAG

This notebook explains **how to ground LLM outputs in retrieved evidence**
and **how citations turn answers into auditable artifacts**.

You will learn:
- What grounding actually means (not just “use context”)
- Why citations reduce hallucination and overconfidence
- How to design citation-aware RAG outputs
- Common failure modes where “citations” lie

Without grounding and citations,
RAG systems cannot be trusted in production.

## 1. What Is Grounding?

Grounding means:

> Every factual claim in the answer
> is supported by retrieved evidence.

Grounding is NOT:
- asking the model to “be accurate”
- trusting the model’s training data
- hoping the model uses the context

## 2. Why RAG Still Hallucinates Without Grounding

Even with retrieved context:
- the model may ignore it
- blend it with prior knowledge
- fill gaps confidently

Because:
> The LLM is still a next-token predictor

## 3. What Citations Do

Citations force the model to:
- anchor statements to specific text
- avoid inventing unsupported claims
- expose uncertainty

Citations create:
- traceability
- auditability
- debuggability

## 4. Evidence vs Knowledge

In RAG:

Retrieved text = evidence  
LLM output = synthesis  

The LLM must be treated as:
> a narrator, not a source

## 5. Minimal Grounded Answer Contract

A grounded answer must:

1. Use only retrieved context
2. Cite the source for each claim
3. Refuse when evidence is insufficient

If any part is missing,
grounding is broken.

## 6. Citation Granularity

Bad citations:
- “Source: Document A”

Good citations:
- Document ID
- Section / chunk ID
- Optional quote span

Granularity enables verification.

## 7. Citation Formats

Common patterns:

- Inline citations: (Doc1, Sec2)
- Footnotes: [1], [2]
- Bullet evidence lists
- Answer + Evidence table

Choose format based on:
- user trust needs
- domain requirements

## 8. Instructing the Model to Cite

Effective instruction pattern:

- “Answer ONLY using the provided context.”
- “For every factual claim, include a citation.”
- “If the answer is not in the context, say ‘NOT FOUND’.”

This does not guarantee compliance,
but drastically improves grounding.

## 9. The Citation Lie

A dangerous failure mode:

- Model fabricates a plausible answer
- Then attaches a citation to look grounded

This happens when:
- retrieved chunks are weak
- citations are not validated

## 10. Preventing Citation Lies

Mitigations:

- Restrict citations to retrieved chunk IDs
- Validate cited chunk IDs programmatically
- Reject answers with missing or invalid citations
- Require quotes for critical claims

## 11. Grounding vs Answer Quality

Grounded answers may be:
- shorter
- less fluent
- more cautious

This is a feature, not a bug.

Trust beats fluency in production.

## 12. Refusal Is Part of Grounding

If:
- no retrieved chunk supports the answer
- evidence is incomplete or conflicting

The correct behavior is:
> refusal, not speculation

## 13. Grounding Failure Patterns

❌ Ungrounded summaries  
❌ Overgeneralization beyond evidence  
❌ Mixing multiple sources incorrectly  
❌ Citing irrelevant but related chunks  
❌ Answering when context is missing  

## Grounded RAG Mental Model

Retrieval finds evidence  
Citations expose evidence  
Grounding enforces discipline  

The model narrates.
The system verifies.

## Self-Check

You understand this notebook if you can explain:

- Why RAG still hallucinates without grounding
- Why citations improve trust and debuggability
- How citation lies occur
- Why refusal is a correct outcome

Grounding and citations are not UX polish.

They are **safety mechanisms**.

Without them,
GenAI systems cannot be trusted at scale.


