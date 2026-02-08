# 🧠 Temperature & Top-p Effects

This notebook explains **how sampling parameters change LLM behavior**.

You will learn:
- What temperature actually does (mathematically & intuitively)
- What top-p (nucleus sampling) does
- Why these parameters affect hallucination
- How to choose values for production systems

These are not “creativity sliders”.
They are **risk controls**.

## 1. Why Sampling Exists

At each step, an LLM predicts:
P(next_token | previous_tokens)

There is never a single correct next token.
There is a probability distribution.

Sampling decides:
> how that distribution is converted into a choice

## 2. Deterministic vs Probabilistic Generation

Deterministic:
- Always pick the highest-probability token
- Same input → same output

Probabilistic:
- Sample from the distribution
- Same input → different outputs

Temperature and top-p control this tradeoff.

## 3. Temperature: Intuition

Temperature controls:
> how sharp or flat the probability distribution is

Low temperature:
- peaks get sharper
- high-probability tokens dominate

High temperature:
- distribution flattens
- lower-probability tokens appear

### Mental Model

Temperature = confidence amplifier or dampener

- Low T → conservative, repetitive
- High T → creative, risky

## 4. Temperature Extremes

Temperature ≈ 0:
- Almost deterministic
- Very consistent
- Low creativity
- Lower hallucination risk

Temperature > 1:
- Highly variable
- Creative
- Higher hallucination risk

## 5. Top-p: Intuition

Top-p controls:
> how much of the probability mass is considered

Instead of:
- considering all tokens

The model:
- keeps the smallest set of tokens
- whose probabilities sum to p

### Example

If top_p = 0.9:
- Only tokens that together account for 90% probability
- Rare tokens are excluded completely

## 6. Temperature vs Top-p

Temperature:
- reshapes probabilities

Top-p:
- truncates the distribution

They solve different problems.

## 7. Why Using Both Can Be Dangerous

Using:
- high temperature
- high top-p

Creates:
- wide sampling space
- high randomness
- high hallucination risk

Many production systems misuse both.

## 8. Common Misconceptions

❌ Higher temperature = smarter reasoning  
❌ Lower temperature = more factual  
❌ Top-p controls creativity  
❌ Sampling fixes hallucination  

None are strictly true.

## 9. Low Temperature Use Cases

- RAG-based QA
- Summarization
- Data extraction
- Compliance reports
- Tool-calling systems

Goal:
> consistency and reliability

## 10. Higher Temperature Use Cases

- Brainstorming
- Creative writing
- Ideation
- Exploration tasks

Even here:
- grounding still matters

## 11. Sampling and Hallucination

Higher randomness:
- increases hallucination probability
- increases novelty

Lower randomness:
- reduces hallucination
- increases repetition

Sampling does not create truth.

## 12. Engineering Decision Table

| Task Type | Temperature | Top-p |
|---------|------------|-------|
| RAG QA | Low (0–0.3) | Low–Medium |
| Data extraction | Near 0 | Low |
| Tool calling | Near 0 | Low |
| Summarization | Low | Medium |
| Creative writing | Medium–High | Medium–High |

## Final Mental Lock

Temperature and top-p:
- shape probability
- not intelligence
- not truth

Use them to control:
- variance
- risk
- consistency

## Self-Check

You understand this notebook if you can explain:

- Why low temperature improves reliability
- Why top-p truncates rare tokens
- Why sampling cannot fix hallucination
- Why defaults are dangerous at scale

Sampling parameters are not creativity knobs.

They are **operational controls** that determine:
- risk
- cost
- trustworthiness

Treat them accordingly.



