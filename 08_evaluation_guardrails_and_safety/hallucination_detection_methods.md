# 🧠 Hallucination Detection Methods

This notebook explains **how hallucinations arise in LLM systems**
and the **practical methods used to detect them in production**.

You will learn:
- Why hallucinations are inevitable
- Why “just prompt better” does not work
- Core detection strategies (model-level, retrieval-level, system-level)
- Tradeoffs between precision, recall, and cost
- How real systems combine multiple signals

📌 Core principle:
> You cannot eliminate hallucinations.
> You can only detect and contain them.

## 1. What Is a Hallucination?

A hallucination occurs when a model:
- generates fluent output
- that is not supported by evidence
- but is internally plausible

Hallucinations are not random.
They are probability-driven completions.

## 2. Root Cause

LLMs are trained to:
> predict the next token, not verify truth.

They have:
- no grounding by default
- no concept of “I don’t know”
- no built-in fact checker

## 3. Detection Is Hard

Hallucinations:
- sound confident
- look structured
- mimic real facts

The system must detect absence of evidence,
which is fundamentally difficult.

## 4. Hallucination Types

Common categories:
1. Factual hallucinations (wrong facts)
2. Attribution hallucinations (fake citations)
3. Logical hallucinations (invalid reasoning)
4. Fabricated entities (people, papers, laws)
5. Overgeneralization (true but unsupported)

Each requires different detection signals.

## 5. Detection Layers

Hallucination detection works best as layers:

1. Retrieval-grounding checks
2. Consistency checks
3. Verification models
4. Heuristic rules
5. Human review

No single method is sufficient.

## 6. Retrieval Grounding

Check:
- Did the answer use retrieved context?
- Are claims supported by retrieved chunks?

If answer references facts not present
in the context → high hallucination risk.

## 7. Citation Matching

Force the model to:
- cite sources
- reference chunk IDs
- quote spans

Then verify:
- cited source exists
- quoted text matches source

Fake citations = hallucination.

## 8. Self-Consistency

Generate:
- multiple answers
- using different seeds or prompts

Compare:
- agreement level
- key factual overlap

High disagreement → low confidence.

## 9. Claim Decomposition

Break output into:
- atomic claims

Verify each claim independently:
- via retrieval
- via rules
- via verification models

One unverified claim taints the answer.

## 10. Verification Models

Use:
- smaller verifier LLMs
- fact-checking models
- NLI (entailment) models

Verifier checks:
> “Is this claim supported by this evidence?”

## 11. Confidence Signals

Signals include:
- low retrieval similarity
- long reasoning chains
- rare entities
- lack of citations

These are weak signals,
but useful when combined.

## 12. Heuristic Flags

Common red flags:
- excessive specificity
- precise dates with no source
- named people + obscure claims
- “According to studies…” with no citation

Heuristics catch cheap failures.

## 13. Self-Critique Limits

Asking the same model to:
“Check if you’re wrong”

Problems:
- same knowledge base
- same biases
- confidence recycling

Self-critique helps tone,
not correctness.

## 14. RAG-Specific Detection

Key RAG checks:
- retrieval recall coverage
- context utilization
- answer-context overlap
- citation completeness

Poor retrieval ≠ hallucination
but strongly correlates.

## 15. Precision vs Recall Tradeoff

Aggressive detection:
- fewer hallucinations
- more false positives
- more refusals

Loose detection:
- better UX
- higher risk

There is no universal threshold.

## Final Mental Model

Hallucination detection is not:
- a classifier
- a single score
- a prompt

It is:
> evidence checking + uncertainty management.

## Self-Check

You understand this notebook if you can explain:

- Why hallucinations are inevitable
- Why detection requires multiple layers
- Why citations alone are insufficient
- How tradeoffs affect UX and safety

Trustworthy GenAI systems are not the ones
that answer everything.

They are the ones that know
when not to answer.


