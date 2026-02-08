# 🧠 Zero-Shot vs Few-Shot Prompting

This notebook explains **how and when examples influence LLM behavior**.

You will learn:
- What zero-shot and few-shot prompting actually do
- Why examples change model behavior
- When few-shot improves results
- When few-shot silently causes failure

This notebook treats prompting as an **interface design problem**, not magic.

## 1. Zero-Shot Prompting

Zero-shot prompting means:

> Asking the model to perform a task **without giving examples**.

You rely entirely on:
- the pretrained model
- instruction clarity
- language patterns learned during training

### Example

"Classify this email as spam or not spam."

The model uses:
- learned patterns
- statistical associations
- prior exposure to similar tasks

## 2. Few-Shot Prompting

Few-shot prompting means:

> Including a small number of input–output examples in the prompt.

These examples act as **behavioral anchors**.

### Example

Email: "Win a free prize!"
Label: Spam

Email: "Meeting rescheduled to tomorrow."
Label: Not Spam

Email: "..."
Label:

## 3. What Few-Shot Actually Does

Few-shot examples do NOT:
- teach new knowledge
- improve reasoning
- change model weights

They DO:
- bias token probabilities
- anchor output format
- steer pattern continuation

## 4. Why Few-Shot Can Dramatically Improve Results

Few-shot works well when:

- Task is ambiguous
- Output format matters
- Model must mimic a specific style
- Decision boundaries are fuzzy

Examples reduce uncertainty by:
> narrowing the probability space

## 5. The Hidden Cost of Few-Shot Prompting

Few-shot prompts:
- increase token count
- increase latency
- increase cost
- consume context window

At scale, this becomes expensive.

## 6. When Few-Shot Prompting Fails

Few-shot hurts when:

- Examples are unrepresentative
- Examples contradict real data
- Task requires factual grounding
- Context window becomes crowded
- Prompt becomes brittle

Bad examples are worse than no examples.

## 7. Zero-Shot Is Often Underrated

Modern LLMs are:
- heavily instruction-tuned
- exposed to many task formats

Zero-shot works well when:
- instructions are clear
- task is common
- output format is simple

Zero-shot is:
- cheaper
- faster
- more scalable

## 8. Few-Shot vs RAG

Few-shot:
- biases behavior
- provides no new facts

RAG:
- injects ground truth
- reduces hallucination

If the task needs knowledge:
> Few-shot is the wrong tool.

## 9. When to Use What

| Scenario | Best Choice |
|-------|-------------|
| Clear task, common pattern | Zero-shot |
| Strict output format | Few-shot |
| New knowledge needed | RAG |
| High-scale system | Zero-shot + rules |
| Safety-critical | No prompting alone |

## 10. Prompting Anti-Patterns

❌ Few-shot to fix hallucinations  
❌ Few-shot as knowledge injection  
❌ Copy-pasting examples everywhere  
❌ Prompt bloating without measurement  

Prompting is not architecture.

## Final Mental Lock

Zero-shot:
> Trusts the model's training

Few-shot:
> Steers behavior, not intelligence

Neither replaces:
> retrieval, validation, or system design

## Self-Check

You understand this notebook if you can explain:

- Why few-shot changes probabilities
- Why few-shot doesn’t add knowledge
- Why few-shot increases cost
- When zero-shot is the better choice

Few-shot prompting is a powerful scalpel.

Used carefully:
- it sharpens behavior

Used blindly:
- it silently breaks systems

