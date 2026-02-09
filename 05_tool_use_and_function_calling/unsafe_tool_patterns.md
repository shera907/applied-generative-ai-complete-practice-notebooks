# 🧠 Unsafe Tool Patterns

This notebook documents **dangerous design patterns**
that appear frequently in GenAI systems when
LLMs are connected to tools, APIs, or real-world actions.

You will learn:
- The most common unsafe tool patterns
- Why they seem to work initially
- How they fail in production
- What safe alternatives look like

📌 Core principle:
> If a pattern feels “clever”, it is usually unsafe.

## 1. Why Unsafe Patterns Exist

Unsafe patterns usually emerge because:
- demos are optimized for speed
- prompts feel easier than systems
- failures are rare at small scale
- early success creates false confidence

These patterns often work…
until they don’t.

## 2. Pattern #1: Direct Tool Execution

❌ The LLM directly:
- calls APIs
- runs SQL
- modifies state
- triggers workflows

Why it seems fine:
- fewer components
- faster prototyping

Why it is dangerous:
- no determinism
- no validation
- no auditability

## 3. Why Direct Execution Fails

LLMs are:
- non-deterministic
- hallucination-prone
- unaware of side effects

One wrong token
can become a real-world incident.

## 4. Safe Alternative

LLM:
- proposes an action
- provides structured arguments

System:
- validates
- authorizes
- executes deterministically

Never blur this boundary.

## 5. Pattern #2: LLM Error Recovery

❌ LLM reads error messages and:
- retries tools
- modifies inputs
- guesses fixes

Why it seems smart:
- adaptive behavior
- fewer explicit rules

Why it is unsafe:
- errors become hallucinations
- silent corruption

## 6. Why LLM Error Recovery Fails

Errors require:
- classification
- policy decisions
- deterministic handling

Language cannot do this reliably.

## 7. Safe Alternative

System:
- classifies error type
- applies retry/fallback/refusal

LLM:
- explains outcome to user
- suggests next steps (language only)

## 8. Pattern #3: Prompt-Based Safety

❌ Safety enforced via:
- “Do not do X”
- “Only do Y”
- “Follow all rules above”

Why it seems okay:
- readable
- easy to modify

Why it fails:
- prompts are probabilistic
- constraints decay over time

## 9. Why Prompt Safety Fails

Prompts:
- bias probabilities
- do not enforce boundaries

Safety requires:
> enforcement, not instruction

## 10. Safe Alternative

- schema validation
- permission checks
- allow-lists
- deny-lists
- policy engines

Safety must exist outside language.

## 11. Pattern #4: Unbounded Agents

❌ Agent allowed to:
- call tools repeatedly
- decide when to stop
- escalate privileges

Why it looks powerful:
- autonomy
- flexibility

Why it is dangerous:
- infinite loops
- runaway costs
- unintended actions

## 12. Safe Alternative

Bound agents with:
- max steps
- allowed tools
- fixed budgets
- explicit termination conditions

Autonomy without bounds is a bug.

## 13. Pattern #5: Free-Text Arguments

❌ Tool arguments passed as:
- raw strings
- natural language
- unvalidated JSON

Why it seems flexible:
- fewer schemas
- faster iteration

Why it fails:
- injection risks
- parsing ambiguity
- silent misexecution

## 14. Safe Alternative

Use:
- strict JSON schemas
- enums
- required fields
- validation before execution

Structure prevents creativity where it is unsafe.

## 15. Pattern #6: Hidden Side Effects

❌ Tools that:
- modify state implicitly
- trigger downstream actions
- lack idempotency

Why it fails:
- retries cause duplication
- debugging becomes impossible

## 16. Safe Alternative

Design tools to be:
- explicit
- idempotent
- observable
- reversible when possible

## 17. Pattern #7: Trusting LLM Reasoning

❌ Using:
- chain-of-thought
- reasoning logs
- “thinking” text
as proof of correctness

Why it fails:
- reasoning can be fabricated
- coherence ≠ correctness

## 18. Safe Alternative

Trust:
- validated inputs
- deterministic outputs
- logged executions

Reasoning is for humans.
Validation is for systems.

## 19. Unsafe vs Safe Patterns

| Unsafe Pattern | Safe Alternative |
|---------------|----------------|
| LLM executes tools | System executes tools |
| Prompt safety | Policy enforcement |
| Free-text args | JSON schema |
| Unbounded agents | Bounded agents |
| LLM error handling | System error handling |
| Trusting reasoning | Trusting validation |

## Final Mental Lock

If an LLM can:
- execute
- retry
- fix
- decide consequences

Then the system is unsafe.

Language must never be in control.

## Self-Check

You understand this notebook if you can explain:

- Why each unsafe pattern is tempting
- How each pattern fails
- What the correct alternative is
- Why safety must live outside prompts

Most GenAI incidents are not malicious.

They are accidental —
caused by unsafe patterns that “worked in the demo”.

This notebook exists to prevent that.
