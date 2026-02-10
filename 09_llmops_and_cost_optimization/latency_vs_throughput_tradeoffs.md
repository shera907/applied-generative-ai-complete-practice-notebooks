# 🧠 Latency vs Throughput Tradeoffs in GenAI Systems

This notebook explains **why GenAI systems face unique performance tradeoffs**
and how to design architectures that balance latency, throughput, cost,
and reliability.

You will learn:
- What latency and throughput really mean
- Why improving one often hurts the other
- Where LLM-specific bottlenecks arise
- Common architectural tradeoffs in RAG and agents
- How to choose the right performance profile for your product

📌 Core principle:
> You cannot optimize latency and throughput simultaneously.
> You must choose intentionally.

## 1. Definitions

Latency:
- Time taken to respond to a single request
- Measured as p50 / p95 / p99

Throughput:
- Number of requests processed per unit time
- Measured as requests per second (RPS)

Fast ≠ scalable.
Scalable ≠ fast.

## 2. Why the Tradeoff Exists

LLMs are:
- compute-heavy
- sequential at token generation time
- memory intensive

Resources used to serve one request
cannot serve others simultaneously.

## 3. Human Perception

Users feel latency differently:
- **< 300 ms** → instant  
- ~ 1 s → acceptable  
- **> 2 s** → broken  
- **> 5 s** → abandoned

Throughput is invisible to users.
Latency is not.

## 4. Latency Breakdown

A single request may include:
- network overhead
- prompt construction
- retrieval (vector DB)
- reranking
- LLM generation
- tool calls
- validation

LLM inference dominates latency.

## 5. Throughput Bottlenecks

Throughput is limited by:
- GPU availability
- context window size
- concurrent requests
- model batch size
- agent loops

Long contexts reduce throughput.

## 6. Sequential Nature

LLMs generate tokens one at a time.

This means:
- output length directly increases latency
- batching improves throughput
- batching hurts single-request latency

## 7. Streaming Responses

Streaming:
- improves perceived latency
- does NOT reduce total compute
- may increase total cost

Streaming is UX optimization,
not system optimization.

## 8. Batching

Batching:
- combines multiple requests
- increases GPU utilization
- improves throughput

Cost:
- each request waits longer
- higher tail latency (p95/p99)

## 9. Common Profiles

Low-latency systems:
- chat assistants
- voice interfaces
- interactive tools

High-throughput systems:
- document processing
- analytics
- batch summarization

Mixing profiles causes pain.

## 10. RAG Performance Tradeoffs

RAG increases:
- retrieval latency
- context size
- token cost

Optimizations:
- smaller top-k
- aggressive reranking
- cached retrieval
- async pipelines

## 11. Agents vs Latency

Agents add:
- planning steps
- multiple LLM calls
- tool waits

Agents destroy latency predictability.
Never put agents on critical paths.

## 12. Parallelism

Parallelize:
- retrieval + preprocessing
- tool calls
- validation

But:
- LLM generation is mostly sequential
- over-parallelization increases contention

## 13. Caching

Cache:
- retrieval results
- prompt templates
- embeddings
- common responses

Caching improves:
- latency
- throughput
- cost

At the expense of freshness.

## 14. Tail Latency

Average latency lies.

Users experience:
- p95 / p99

Tail latency is driven by:
- retries
- long generations
- tool timeouts
- cold starts

## 15. Choosing Intentionally

Ask:
- Is this interactive or batch?
- Do users tolerate delay?
- Is cost or UX more critical?
- Can we degrade gracefully?

Design for the dominant constraint.

## 16. Anti-Patterns

❌ Agents on hot paths  
❌ Unbounded context windows  
❌ No batching strategy  
❌ No p95/p99 monitoring  
❌ Treating streaming as optimization  

## Final Mental Lock

Latency is about experience.
Throughput is about scale.

Optimizing both
without tradeoffs
is a fantasy.

## Self-Check

You understand this notebook if you can explain:

- Why token generation is sequential
- Why batching hurts latency
- Why agents kill predictability
- How to choose a performance profile

Fast demos impress.

Predictable systems survive.

Design for reality, not benchmarks.


