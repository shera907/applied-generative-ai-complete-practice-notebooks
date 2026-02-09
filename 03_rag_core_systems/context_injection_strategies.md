# 🧠 Context Injection Strategies

This notebook explains **how retrieved context should be injected
into LLM prompts** and why poor injection strategies
cause hallucination, bias, and fragile answers.

You will learn:
- Why context placement matters
- Different injection patterns
- Tradeoffs between verbosity and precision
- How to prevent context from overwhelming the model

Context is not neutral.
How you inject it shapes the answer.

## 1. Why Context Injection Matters

LLMs do not:
- “understand” context
- prioritize important facts automatically
- ignore irrelevant text

They treat context as:
> probabilistic continuation material

Bad injection = bad answers.

## 2. Naive Injection Pattern

Common pattern:

"Here is some context:
<big block of text>

Answer the question."

Problems:
- No structure
- No prioritization
- No constraints

## 3. Instruction + Context Separation

Better pattern:

- Clear task instruction
- Explicit context section
- Explicit usage constraints

This tells the model:
> “This text is evidence, not conversation.”

## 4. Context as Evidence

Treat retrieved text as:
- quotes
- references
- evidence

Not as:
- background knowledge
- optional reading

This framing reduces hallucination.

## 5. Chunk Ordering

LLMs attend more to:
- early context
- recent tokens

Ordering chunks by:
- relevance score
- confidence
- recency

Improves answer quality.

## 6. Limiting Context Scope

More context:
- increases noise
- dilutes attention
- raises hallucination risk

Inject:
- only what is needed
- for the specific question

## 7. Context Windows Are Not Buckets

Filling the context window:
- does not improve answers
- often makes them worse

Attention is finite.
Signal competes with noise.

## 8. Explicit Usage Constraints

Always tell the model:

- Use ONLY the provided context
- Cite the context
- If context is insufficient, say so

This does not guarantee compliance,
but significantly reduces fabrication.

## 9. Common Context Injection Patterns

1. Inline context (fragile)
2. Delimited context blocks (better)
3. Structured context (best)
4. Evidence tables / bullet points (best for precision)

## 10. Structured Context Injection

Example:

Context:
- [Doc 1 | Section 2] : ...
- [Doc 2 | Clause 5] : ...

Question:
...

Benefits:
- Clear provenance
- Reduced blending
- Easier citation

## 11. Context Length Tradeoff

Long context:
- more coverage
- less precision

Short context:
- higher precision
- risk of missing info

Tune context size empirically.

## 12. Failure Modes

❌ Context ignored  
❌ Wrong chunk dominates  
❌ Facts blended incorrectly  
❌ Model answers from prior knowledge  
❌ Hallucinated citations  

## Final Mental Lock

Retrieval finds candidates.
Context injection decides influence.

Poor injection negates good retrieval.

## Self-Check

You understand this notebook if you can explain:

- Why placement matters
- Why more context can hurt
- Why structure reduces hallucination
- Why constraints are necessary

RAG does not fail only at retrieval.

It also fails quietly at the moment
knowledge enters the model.

Treat context injection as a first-class design problem.
