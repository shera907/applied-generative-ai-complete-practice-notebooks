# 🧠 Tokens, Embeddings & Context Window

This notebook explains the **three physical constraints** of all LLM systems:

1. Tokens — the atomic cost unit  
2. Embeddings — meaning as geometry  
3. Context Window — the only memory

If these are misunderstood,
GenAI systems will be:
- expensive
- slow
- unreliable
- hallucination-prone

## 1. Tokens: The Atomic Unit of LLMs

LLMs do not read words or characters.
They read **tokens**.

A token can be:
- a word
- part of a word
- punctuation
- symbols

### Examples

"apple"        → 1 token  
"ChatGPT"      → 2 tokens  
"unbelievable" → un + believe + able  

Tokenization is:
- model-specific
- language-dependent
- non-intuitive

## 2. Why Tokens Matter

Tokens determine:

- Billing
- Latency
- Context limits
- Throughput

Every extra token costs:
- money
- time
- memory

### Engineering Rule

> Tokens are the real currency of GenAI.

## 3. Tokenization Pitfalls

Common mistakes:

- Assuming characters ≈ tokens
- Ignoring non-English token inflation
- Sending raw JSON repeatedly
- Copy-pasting long system prompts

Bad token discipline = runaway cost.

## 4. Embeddings: Meaning as Geometry

An embedding converts text into a vector:

- High-dimensional
- Numerical
- Dense

Meaning is represented by **distance**, not logic.

### Mental Model

Think of embeddings as points in space:

- Similar meaning → closer points
- Different meaning → farther points

LLMs do not understand meaning.
They measure **similarity**.

## 5. Why Embeddings Power RAG

RAG works because:

- Questions and documents live in same vector space
- Similar intent → similar embeddings
- Retrieval = nearest neighbors search

If embeddings are poor,
RAG fails regardless of model quality.

## 6. Context Window: The Only Memory

LLMs have no persistent memory.

They only see:
- system prompt
- user input
- injected context

Within the **context window limit**.

### Key Insight

> Context is working memory, not storage.

## 7. Context Overflow

When context exceeds the window:

- Old tokens are dropped
- The model forgets them completely
- There is no warning

This causes:
- contradictions
- repeated questions
- hallucinations

## 8. Context Window Economics

Larger context windows:

- increase memory usage
- increase latency
- reduce throughput
- increase cost

A 2× context window ≠ 2× cost  
Often much worse.

## 9. Retrieval Beats Brute-Force Context

Bad approach:
> “Just increase the context window.”

Good approach:
- Retrieve only relevant chunks
- Inject minimal context
- Summarize aggressively

RAG is a **memory management system**.

## 10. Engineering Tradeoffs

| Choice | Tradeoff |
|-----|--------|
| Large context | Cost & latency |
| Small context | Missed info |
| Many chunks | Noise |
| Few chunks | Recall loss |

There is no free lunch.

## Final Mental Lock

Tokens:
- define cost and speed

Embeddings:
- define meaning and retrieval

Context window:
- defines memory and reliability

Design systems around these constraints,
not against them.

## Self-Check

You understand this notebook if you can explain:

- Why long prompts slow systems
- Why RAG beats large context windows
- Why embeddings fail with bad chunking
- Why tokens are the real budget

These three constraints shape:

- RAG architecture
- Agent design
- Cost optimization
- Platform decisions

Ignore them, and GenAI will quietly fail.
