# 🧠 System, User, and Assistant Roles

This notebook explains how LLMs interpret different message roles:
- system
- user
- assistant

You will learn:
- what roles actually do
- what they do NOT do
- why system prompts are not security boundaries
- how role misuse leads to hallucinations and prompt injection

Understanding this is critical for **safe GenAI system design**.

## 1. Why Do Roles Exist?

Roles exist to:
- structure conversation context
- guide model behavior
- separate instruction types

They are NOT:
- permission systems
- security mechanisms
- hard constraints

## 2. The Three Core Roles

Most LLM APIs expose three roles:

- System
- User
- Assistant

All three are ultimately just **text inside the context window**.

## 3. System Role

The system role is used to:
- set global behavior
- define tone and scope
- describe what the assistant "is"

Examples:
- "You are a helpful assistant"
- "You are a financial compliance assistant"

System prompts influence behavior,
but they do not enforce truth or safety.

### Critical Insight

The system role:
- biases probability
- does not override physics

It cannot:
- add knowledge
- guarantee refusal
- prevent hallucination

## 4. User Role

The user role represents:
- external input
- potentially malicious text
- ambiguous intent

From the model’s perspective:
> user input is just more tokens

### Dangerous Assumption

Assuming the model understands:
- trust
- authority
- intent

It does not.

## 5. Assistant Role

The assistant role contains:
- previous model outputs
- explanations
- commitments

The model treats assistant messages as:
> examples of how it should respond

### Side Effect

Incorrect assistant responses:
- reinforce wrong behavior
- propagate hallucinations
- bias future outputs

## 6. How Roles Are Actually Used

Internally, most models:
- concatenate all messages
- add role tokens or embeddings
- process everything together

There is no hard separation.

## 7. The Illusion of Authority

System > User > Assistant
is a **soft convention**, not a law.

A cleverly written user message can:
- override system intent
- confuse instructions
- trigger unsafe behavior

This is called **prompt injection**.

## 8. Why System Prompts Are Not Security Boundaries

System prompts cannot:
- block malicious instructions
- enforce data access rules
- prevent leakage
- guarantee refusals

Security must live:
- outside the model
- in system architecture

## 9. Correct Use of Roles

System role:
- define scope
- define tone
- define format

User role:
- treated as untrusted input

Assistant role:
- treated as probabilistic output

Control lives outside the model.

## 10. Common Role Misuse Patterns

❌ Putting secrets in system prompts  
❌ Encoding business logic in prompts  
❌ Trusting system role for safety  
❌ Letting assistant outputs drive actions directly  

These lead to silent failures.

## 11. Roles vs Architecture

Roles:
- shape language
- guide behavior

Architecture:
- enforces rules
- controls data
- validates actions

Roles ≠ control.

## Final Mental Lock

System role:
> Sets expectations

User role:
> Supplies untrusted input

Assistant role:
> Generates probabilistic output

None of them:
> guarantee safety or truth

## Self-Check

You understand this notebook if you can explain:

- Why system prompts can be overridden
- Why roles do not imply trust
- Why prompt injection is inevitable
- Why architecture must enforce safety

Roles help with communication.
They do not replace system design.

If your safety depends on a system prompt,
your system is already unsafe.
