# 📘 Applied Generative AI — Complete Practice Path (Notebook-Only)

> **A systems-first, production-oriented Generative AI practice repository**  
> designed to build **Senior → Principal GenAI engineering and architecture capability**.

This repository is **not a collection of prompt tricks**.  
It is a **deliberate, end-to-end learning and practice path** covering:

- Mental models behind Generative AI  
- Retrieval-Augmented Generation (RAG) systems  
- Agentic AI with bounded autonomy  
- Multimodal pipelines  
- Evaluation, safety, and guardrails  
- LLMOps, cost, and platform design  
- Enterprise-scale GenAI architectures  

All work is done using **Jupyter notebooks only**, prioritizing **clarity, reasoning, and explainability** over framework-heavy abstractions.

---

## 🎯 Who This Repository Is For

This repository is intentionally designed for:

- **Applied ML engineers transitioning to GenAI**
- **Senior software engineers building AI systems**
- **GenAI engineers preparing for Staff / Principal roles**
- **Architects designing enterprise AI platforms**
- **Researchers who want system-level intuition, not just models**

If you are looking for:
- “Best prompts”
- Toy chatbots
- Copy-paste LangChain demos  

This repository is **not** for you.

---

## 🧠 Design Philosophy

### 1. Mental Models First
Every topic starts with **why** before **how**.
You will understand:
- Why LLMs hallucinate  
- Why RAG exists  
- Why prompts fail in production  
- Why agents are dangerous when unconstrained  

### 2. Systems > Models
The focus is on:
- Architecture
- Tradeoffs
- Failure modes
- Cost, latency, and risk

Not on:
- Model hype
- Benchmark chasing
- Blind fine-tuning

### 3. Notebook-Only, By Design
All work is implemented in notebooks to:
- Make reasoning explicit
- Encourage experimentation
- Enable teaching & mentoring
- Keep the focus on concepts, not tooling

---

## 📂 Repository Structure

# 📦 Applied Generative AI – Complete Practice Notebooks

```text
applied-generative-ai-complete-practice-notebooks/
│
├── 00_genai_foundations_and_setup/
├── 01_prompting_and_llm_basics/
├── 02_embeddings_and_vector_search/
├── 03_rag_core_systems/
├── 04_advanced_rag_patterns/
├── 05_tool_use_and_function_calling/
├── 06_agentic_ai_and_planning/
├── 07_multimodal_genai/
├── 08_evaluation_guardrails_and_safety/
├── 09_llmops_and_cost_optimization/
├── 10_genai_system_design_case_studies/
├── 11_enterprise_and_platform_genai/
├── 12_capstone_architectures/
│
└── README.md
```
---

Each folder represents a **clear capability boundary**, not just a topic.

---

## 🟢 00. Foundations & Mental Models
**Understand what Generative AI actually is**

- Discriminative vs Generative models  
- Probability vs intelligence  
- Tokens, embeddings, context windows  
- Why LLMs hallucinate  
- Transformers & attention (intuition-first)  
- LLM lifecycle (pretraining → RLHF → inference)

> If this folder feels trivial, you probably misunderstand GenAI.

---

## 🟢 01. Prompting & LLM Basics
**Prompting as an interface, not a solution**

- Zero-shot vs few-shot reasoning  
- System / user / assistant roles  
- Instruction clarity & constraints  
- Temperature and sampling behavior  
- Prompt failure patterns  
- Why prompting cannot fix system problems  

---

## 🟡 02. Embeddings & Vector Search
**Meaning as geometry**

- What embeddings actually represent  
- Cosine similarity vs dot product  
- Chunking strategies (critical)  
- Metadata filtering  
- Debugging retrieval failures  

> 📌 Rule: **Bad chunking = bad RAG**

---

## 🟡 03. RAG Core Systems
**From chatbots to knowledge systems**

- Why RAG beats fine-tuning (usually)  
- Canonical RAG architecture  
- Retrieval vs generation failures  
- Context injection strategies  
- Grounded answers & citations  
- End-to-end RAG pipelines  

---

## 🔵 04. Advanced RAG Patterns
**Architect-grade retrieval systems**

- Hierarchical RAG  
- Agentic RAG (bounded)  
- Hybrid search (BM25 + vectors)  
- Knowledge graph + RAG  
- Query rewriting & reranking  
- Scaling RAG systems  

---

## 🔵 05. Tool Use & Function Calling
**LLMs decide, systems act**

- Tools vs prompts  
- JSON schema design  
- Deterministic tool execution  
- Error handling & retries  
- Unsafe tool patterns  
- Tool-driven GenAI systems  

---

## 🔵 06. Agentic AI & Planning
**Power with restraint**

- Agent vs workflow  
- ReAct (Reason + Act)  
- Plan–Execute architectures  
- Short-term vs long-term memory  
- Tool orchestration  
- ⚠️ Why fully autonomous agents are dangerous  

---

## 🔴 07. Multimodal Generative AI
**Text is not the world**

- Vision–language models (VLMs)  
- Image Q&A  
- Audio pipelines (ASR + TTS)  
- Image generation fundamentals  
- OCR + LLM document systems  
- Multimodal failure modes  

---

## 🔴 08. Evaluation, Guardrails & Safety
**Trust is engineered, not assumed**

- Hallucination detection  
- Faithfulness & relevance metrics  
- Prompt & output validation  
- Red-teaming LLM systems  
- Prompt injection attacks  
- Data leakage, bias & risk analysis  

---

## 🔴 09. LLMOps & Cost Optimization
**Running GenAI in production**

- Prompt & model versioning  
- Logs, traces & observability  
- Feedback loops  
- A/B testing prompts  
- Token economics  
- Latency vs throughput tradeoffs  

---

## ⚫ 10. GenAI System Design Case Studies
**Interview and real-world ready**

- Enterprise knowledge intelligence platforms  
- AI customer support copilots  
- Compliance & risk GenAI systems  
- Research agents  
- Multimodal document intelligence  

Each case study focuses on:
- Architecture diagrams  
- Tradeoffs  
- Failure modes  
- Cost & risk  

---

## ⚫ 11. Enterprise & Platform GenAI
**Principal / Architect territory**

- Internal GenAI platforms  
- Model gateways & routing  
- Multi-team usage patterns  
- Policy & access control  
- Build vs buy model strategy  

---

## ⚫ 12. Capstone Architectures
**Flagship, portfolio-grade systems**

- Enterprise Knowledge Intelligence Platform  
- GenAI Model Gateway & Cost Optimizer  
- Banking Task Orchestration Agent  
- AI Compliance & Risk Monitor  

> One deep capstone here outweighs dozens of shallow projects elsewhere.

---

## 🧠 What You’ll Be Able to Do After This Repo

- Design large-scale GenAI systems  
- Debug hallucinations at the system level  
- Choose RAG vs fine-tuning correctly  
- Build safe, bounded agents  
- Control cost, latency, and risk  
- Design company-wide GenAI platforms  
- Mentor teams and set GenAI strategy  

---

## 🚀 How to Use This Repository

- Follow folders **in order**
- Treat notebooks as **thinking documents**
- Modify, break, and redesign systems
- Add your own case studies and notes

This repository is meant to **grow with your judgment**.

---

## 📌 Final Note

> Models will change.  
> APIs will change.  
> Frameworks will change.  
>  
> **Mental models and system design skills endure.**

This repository is about building the latter.

---

**Author**: *SHARAYU BORKAR*  
**Focus**: Applied Generative AI • Systems • Architecture • Strategy

