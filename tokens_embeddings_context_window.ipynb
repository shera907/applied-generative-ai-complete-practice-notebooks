{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "8656d535",
   "metadata": {},
   "source": [
    "# 🧠 Tokens, Embeddings & Context Window\n",
    "\n",
    "This notebook explains the **three physical constraints** of all LLM systems:\n",
    "\n",
    "1. Tokens — the atomic cost unit  \n",
    "2. Embeddings — meaning as geometry  \n",
    "3. Context Window — the only memory\n",
    "\n",
    "If these are misunderstood,\n",
    "GenAI systems will be:\n",
    "- expensive\n",
    "- slow\n",
    "- unreliable\n",
    "- hallucination-prone\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5c8ee569",
   "metadata": {},
   "source": [
    "## 1. Tokens: The Atomic Unit of LLMs\n",
    "\n",
    "LLMs do not read words or characters.\n",
    "They read **tokens**.\n",
    "\n",
    "A token can be:\n",
    "- a word\n",
    "- part of a word\n",
    "- punctuation\n",
    "- symbols\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a9737c7e",
   "metadata": {},
   "source": [
    "### Examples\n",
    "\n",
    "\"apple\"        → 1 token  \n",
    "\"ChatGPT\"      → 2 tokens  \n",
    "\"unbelievable\" → un + believe + able  \n",
    "\n",
    "Tokenization is:\n",
    "- model-specific\n",
    "- language-dependent\n",
    "- non-intuitive\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c41862df",
   "metadata": {},
   "source": [
    "## 2. Why Tokens Matter\n",
    "\n",
    "Tokens determine:\n",
    "\n",
    "- Billing\n",
    "- Latency\n",
    "- Context limits\n",
    "- Throughput\n",
    "\n",
    "Every extra token costs:\n",
    "- money\n",
    "- time\n",
    "- memory\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2f3f1e12",
   "metadata": {},
   "source": [
    "### Engineering Rule\n",
    "\n",
    "> Tokens are the real currency of GenAI.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "cdbf214b",
   "metadata": {},
   "source": [
    "## 3. Tokenization Pitfalls\n",
    "\n",
    "Common mistakes:\n",
    "\n",
    "- Assuming characters ≈ tokens\n",
    "- Ignoring non-English token inflation\n",
    "- Sending raw JSON repeatedly\n",
    "- Copy-pasting long system prompts\n",
    "\n",
    "Bad token discipline = runaway cost.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7cde0289",
   "metadata": {},
   "source": [
    "## 4. Embeddings: Meaning as Geometry\n",
    "\n",
    "An embedding converts text into a vector:\n",
    "\n",
    "- High-dimensional\n",
    "- Numerical\n",
    "- Dense\n",
    "\n",
    "Meaning is represented by **distance**, not logic.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "dc44deb2",
   "metadata": {},
   "source": [
    "### Mental Model\n",
    "\n",
    "Think of embeddings as points in space:\n",
    "\n",
    "- Similar meaning → closer points\n",
    "- Different meaning → farther points\n",
    "\n",
    "LLMs do not understand meaning.\n",
    "They measure **similarity**.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "281fbd7f",
   "metadata": {},
   "source": [
    "## 5. Why Embeddings Power RAG\n",
    "\n",
    "RAG works because:\n",
    "\n",
    "- Questions and documents live in same vector space\n",
    "- Similar intent → similar embeddings\n",
    "- Retrieval = nearest neighbors search\n",
    "\n",
    "If embeddings are poor,\n",
    "RAG fails regardless of model quality.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2d4290cd",
   "metadata": {},
   "source": [
    "## 6. Context Window: The Only Memory\n",
    "\n",
    "LLMs have no persistent memory.\n",
    "\n",
    "They only see:\n",
    "- system prompt\n",
    "- user input\n",
    "- injected context\n",
    "\n",
    "Within the **context window limit**.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2e7671d2",
   "metadata": {},
   "source": [
    "### Key Insight\n",
    "\n",
    "> Context is working memory, not storage.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "dfecc1c6",
   "metadata": {},
   "source": [
    "## 7. Context Overflow\n",
    "\n",
    "When context exceeds the window:\n",
    "\n",
    "- Old tokens are dropped\n",
    "- The model forgets them completely\n",
    "- There is no warning\n",
    "\n",
    "This causes:\n",
    "- contradictions\n",
    "- repeated questions\n",
    "- hallucinations\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "50d7a294",
   "metadata": {},
   "source": [
    "## 8. Context Window Economics\n",
    "\n",
    "Larger context windows:\n",
    "\n",
    "- increase memory usage\n",
    "- increase latency\n",
    "- reduce throughput\n",
    "- increase cost\n",
    "\n",
    "A 2× context window ≠ 2× cost  \n",
    "Often much worse.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "46f8b2d2",
   "metadata": {},
   "source": [
    "## 9. Retrieval Beats Brute-Force Context\n",
    "\n",
    "Bad approach:\n",
    "> “Just increase the context window.”\n",
    "\n",
    "Good approach:\n",
    "- Retrieve only relevant chunks\n",
    "- Inject minimal context\n",
    "- Summarize aggressively\n",
    "\n",
    "RAG is a **memory management system**.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "54141e23",
   "metadata": {},
   "source": [
    "## 10. Engineering Tradeoffs\n",
    "\n",
    "| Choice | Tradeoff |\n",
    "|-----|--------|\n",
    "| Large context | Cost & latency |\n",
    "| Small context | Missed info |\n",
    "| Many chunks | Noise |\n",
    "| Few chunks | Recall loss |\n",
    "\n",
    "There is no free lunch.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "02181f25",
   "metadata": {},
   "source": [
    "## Final Mental Lock\n",
    "\n",
    "Tokens:\n",
    "- define cost and speed\n",
    "\n",
    "Embeddings:\n",
    "- define meaning and retrieval\n",
    "\n",
    "Context window:\n",
    "- defines memory and reliability\n",
    "\n",
    "Design systems around these constraints,\n",
    "not against them.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4090e149",
   "metadata": {},
   "source": [
    "## Self-Check\n",
    "\n",
    "You understand this notebook if you can explain:\n",
    "\n",
    "- Why long prompts slow systems\n",
    "- Why RAG beats large context windows\n",
    "- Why embeddings fail with bad chunking\n",
    "- Why tokens are the real budget\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b59e5845",
   "metadata": {},
   "source": [
    "These three constraints shape:\n",
    "\n",
    "- RAG architecture\n",
    "- Agent design\n",
    "- Cost optimization\n",
    "- Platform decisions\n",
    "\n",
    "Ignore them, and GenAI will quietly fail.\n"
   ]
  }
 ],
 "metadata": {
  "language_info": {
   "name": "python"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
