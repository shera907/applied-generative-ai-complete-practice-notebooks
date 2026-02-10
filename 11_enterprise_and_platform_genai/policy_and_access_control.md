# 🧠 Policy & Access Control in GenAI Systems

This notebook explains how to design **policy and access control**
for GenAI platforms and applications — ensuring that AI capabilities
are used only by the right people, for the right purposes, on the right data.

You will learn:
- Why GenAI breaks traditional access control models
- Different layers of policy in GenAI systems
- How access control applies to data, models, prompts, and tools
- Architectural patterns for enforceable governance
- Common failure modes and how to avoid them

📌 Core principle:
> GenAI safety is enforced by systems, not by prompts.

## 1. Why This Is Hard

Traditional systems:
- control API access
- control database rows
- control UI permissions

GenAI systems:
- synthesize data
- combine multiple sources
- generate new content
- act through tools

Access is no longer binary.

## 2. The Prompt Illusion

- ❌ "You are not allowed to access X"
- ❌ "Do not reveal sensitive data"

LLMs do not enforce policy.
They generate text.

Policies must be enforced
outside the model.

## 3. Definitions

Access control:
- who can access which resource

Policy:
- under what conditions
- for which purposes
- with what constraints

GenAI requires both.

## 4. Policy Layers

Typical layers:
1. User & Identity Policy
2. Data Access Policy
3. Model Usage Policy
4. Prompt & Capability Policy
5. Tool Execution Policy
6. Output Policy

Policies stack.

## 5. Identity

Every GenAI request must be tied to:
- a user
- a service account
- a team / org unit

Anonymous AI is ungovernable AI.

## 6. RBAC vs ABAC

RBAC:
- roles like "admin", "agent"
- simple, coarse

ABAC:
- attributes like region, clearance, purpose
- dynamic, fine-grained

GenAI systems require ABAC.

## 7. Data Access in RAG

Rules:
- retrieval must respect document ACLs
- embeddings must inherit permissions
- filters apply before similarity search

Similarity ≠ authorization.

## 8. Model Policies

Control:
- which teams can use which models
- which data can go to which models
- region & compliance constraints

Not all data can go to all models.

## 9. Prompt Policies

Restrict:
- system-level prompts
- instruction authority
- capability escalation

Teams should not be able to:
- bypass safety prompts
- redefine system behavior

## 10. Tool Policies

For each tool define:
- who can invoke it
- under what conditions
- with which parameters
- at what rate

Tools are the highest-risk surface.

## 11. Purpose Limitation

Users may have access to data,
but not for all purposes.

Example:
- read for support
- not allowed for analytics

Purpose must be enforced at runtime.

## 12. Enforcement Points

Enforce policies:
- at the API gateway
- before retrieval
- before model calls
- before tool execution
- before response delivery

Defense in depth.

## 13. Policy as Code

Policies should be:
- declarative
- versioned
- testable
- auditable

Avoid policies embedded in app logic.

## 14. Auditing

For every GenAI response, record:
- user identity
- data accessed
- model used
- tools executed
- policies applied

If you cannot audit it,
you cannot defend it.

## 15. Failure Modes

❌ Trusting prompts for enforcement  
❌ Applying ACLs after retrieval  
❌ No purpose limitation  
❌ Shared service accounts  
❌ No audit logs  

## 16. Balance

Over-restriction:
- kills adoption
- causes shadow AI

Under-restriction:
- causes incidents

Good systems make
the safe path the easy path.

## Final Mental Lock

GenAI systems are powerful
because they blur boundaries.

Policy and access control
are how organizations redraw
those boundaries safely.

## Self-Check

You understand this notebook if you can explain:

- Why prompts cannot enforce policy
- How ABAC applies to GenAI
- Where policies must be enforced
- Why auditing is mandatory

In GenAI systems,
mistakes are not always malicious.

But regulators and customers
will not care.

Policy is how power is used responsibly.




