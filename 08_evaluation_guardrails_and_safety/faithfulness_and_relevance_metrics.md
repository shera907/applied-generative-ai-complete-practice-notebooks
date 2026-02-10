# 🧠 Faithfulness & Relevance Metrics

This notebook explains **how to evaluate GenAI outputs**
along the two most important dimensions:

- Faithfulness: Is the answer supported by evidence?
- Relevance: Does the answer actually address the user’s question?

You will learn:
- Precise definitions of faithfulness and relevance
- Why accuracy alone is insufficient
- Common automatic and human-evaluation metrics
- Failure cases each metric misses
- How production systems combine metrics

📌 Core principle:
> A fluent answer can be relevant but unfaithful.
> A faithful answer can still be irrelevant.

## 1. Why Evaluation Is Hard

LLMs produce:
- fluent language
- structured answers
- confident tone

But fluency hides:
- hallucinations
- partial answers
- off-topic responses

Evaluation must target *grounding* and *usefulness*,
not surface quality.

## 2. Definitions

Faithfulness:
> Every factual claim in the answer
> is supported by the provided context or evidence.

Relevance:
> The answer addresses the user’s intent
> and contains information that helps solve the task.

## 3. Accuracy Is Misleading

Accuracy assumes:
- a single correct answer
- a fixed label

GenAI answers:
- are open-ended
- vary in phrasing
- may be partially correct

We evaluate *alignment to evidence and intent*, not labels.

## 4. Faithfulness Failure Examples

- Adding facts not present in context
- Overgeneralizing beyond evidence
- Fabricating details to “complete” an answer
- Incorrect attribution to sources

Faithfulness failures = hallucinations.

## 5. Relevance Failure Examples

- Answering a different question
- Giving generic explanations
- Overly verbose but unhelpful content
- Missing the key constraint or intent

Relevance failures feel polite but useless.

## 6. Relationship

Four possible states:

1. Faithful + Relevant → Ideal
2. Faithful + Irrelevant → Safe but unhelpful
3. Unfaithful + Relevant → Dangerous
4. Unfaithful + Irrelevant → Completely broken

Production systems must detect #3 aggressively.

## 7. Faithfulness Measurement

Common approaches:
- Context–answer overlap
- Citation correctness
- Claim–evidence entailment
- Human verification

Faithfulness always requires *evidence checking*.

## 8. Claim-Level Evaluation

Process:
1. Decompose answer into atomic claims
2. For each claim, check if evidence exists
3. Mark unsupported claims

One unsupported claim
means the answer is unfaithful.

## 9. Automated Metrics

Examples:
- NLI entailment (answer vs context)
- LLM-as-judge (carefully constrained)
- Retrieval overlap scores

Limitations:
- miss subtle hallucinations
- depend on retrieval quality

## 10. Relevance Measurement

Relevance measures:
- alignment to the question
- usefulness of information
- completeness for the task

Relevance is intent-dependent, not factual.

## 11. Automated Relevance

Common methods:
- embedding similarity (question ↔ answer)
- intent classification agreement
- LLM-based relevance scoring

High similarity ≠ high usefulness.

## 12. Human Evaluation

Humans judge relevance by asking:
- Did this help me?
- Did it answer what I asked?
- Is anything important missing?

Human judgment is still the gold standard.

## 13. LLM-as-Judge Caveats

Problems:
- judges share biases with generators
- scoring drift over time
- sensitivity to prompt wording

LLM judges help at scale,
but must be calibrated.

## 14. Metrics in RAG Systems

Faithfulness checks:
- answer supported by retrieved chunks?
- citations valid?

Relevance checks:
- retrieval relevance
- answer relevance
- end-to-end usefulness

RAG evaluation is multi-stage.

## 15. Composite Strategy

Production systems combine:
- retrieval metrics
- faithfulness metrics
- relevance metrics
- refusal rates
- human audits

No single score is trusted.

## Final Mental Model

Faithfulness asks:
“Is this supported?”

Relevance asks:
“Is this useful?”

You need both
to earn trust.

## Self-Check

You understand this notebook if you can explain:

- The difference between faithfulness and relevance
- Why accuracy is insufficient
- Why claim-level checks matter
- Why relevance is subjective but necessary

Evaluation is where GenAI systems
become accountable.

If you cannot measure faithfulness and relevance,
you cannot deploy responsibly.

