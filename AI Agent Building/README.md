# How to Build an AI Agent — For Any Task, Step by Step

A practical, framework-agnostic guide to building an AI agent from scratch. The pattern here works whether the task is "answer questions from my PDFs," "book a meeting," "scrape and summarize prices," or anything else — only the **tools** change.

> Pairs well with [`Free Tier LLM/`](../Free%20Tier%20LLM/Readme.md) (Groq/Gemini API setup) and [`GeoAI and LLM/`](../GeoAI%20and%20LLM/Readme.md) in this repo.

**Want to run the code instead of just reading it?** → [`AI_Agent_Building_Notebook.ipynb`](./AI_Agent_Building_Notebook.ipynb) has every example below as executable cells — including a zero-API-key mock version so you can see the full agent loop trace without any setup.

---

## Table of Contents

1. [What actually makes something an "agent"](#1-what-actually-makes-something-an-agent)
2. [The 5 building blocks](#2-the-5-building-blocks)
3. [Step-by-step: build one from scratch](#3-step-by-step-build-one-from-scratch)
4. [Full working example (Groq, tool-calling loop)](#4-full-working-example-groq-tool-calling-loop)
5. [Agent patterns — pick the right shape](#5-agent-patterns--pick-the-right-shape)
6. [When to use a framework instead](#6-when-to-use-a-framework-instead)
7. [Claude Code sub-agents (a different kind of "agent")](#7-claude-code-sub-agents-a-different-kind-of-agent)
8. [Guardrails checklist](#8-guardrails-checklist)
9. [Cheat sheet](#9-cheat-sheet)

---

## 1. What actually makes something an "agent"

A plain LLM call is: **prompt in → text out**. One shot, no actions.

An **agent** is an LLM wrapped in a **loop** that can:
1. Decide *what to do next* (not just what to say)
2. **Call tools/functions** to act on the world (search, run code, query a DB, call an API)
3. **Observe the result** of that action
4. Repeat until the task is actually done, then give a final answer

```
Plain LLM call:      prompt ──► LLM ──► answer

Agent:                     ┌────────────────────────┐
                            │                        │
                prompt ──► LLM ──► "call tool X" ──► tool runs ──► result
                            ▲                                          │
                            └──────────────── feed result back ────────┘
                            (repeat until LLM says "done")
```

That loop — **think → act → observe → repeat** — is the entire idea. Everything else (memory, planning, multi-agent setups) is a variation on this loop.

---

## 2. The 5 building blocks

| Block | What it is | Example |
|---|---|---|
| **LLM** | The "brain" that decides what to do | Groq (Llama/Mixtral, free tier), Gemini, Claude, GPT |
| **Tools** | Python functions the LLM can call, each with a name + description + typed arguments | `search_web(query)`, `run_sql(query)`, `get_weather(city)` |
| **System prompt** | Tells the LLM its role, what tools exist, and how to behave | "You are a support agent. Use `lookup_order` before answering billing questions." |
| **Loop / orchestrator** | The code that calls the LLM, checks if it asked for a tool, runs the tool, feeds the result back | A `while` loop (shown in Section 4) |
| **Memory / state** (optional) | What the agent remembers across turns or steps | Conversation history list, a vector DB for long-term memory |

You do **not** need a framework to have all five — a `while` loop and a `dict` of functions is a complete agent.

---

## 3. Step-by-step: build one from scratch

### Step 0 — Define the task narrowly
Bad: "build an agent that helps with anything."
Good: "an agent that answers questions about my company's product docs, and can search the web if the docs don't have the answer."

A narrow task = a short, clear tool list = a reliable agent. Scope creep is the #1 reason agents get flaky.

### Step 1 — Pick the LLM
Needs **function/tool calling** support (not every model has it). Free-tier options already in this repo's notes:
- **Groq** — very fast, generous free tier, supports tool calling (Llama 3.x models)
- **Google Gemini** — free tier, supports tool calling
- **Claude / GPT** — paid, best tool-calling reliability if budget allows

### Step 2 — Define your tools as plain Python functions
Each tool needs: a clear **name**, a **docstring/description** (the LLM reads this to decide when to use it), and **typed parameters**.

```python
def get_weather(city: str) -> str:
    """Get the current weather for a given city."""
    ...

def search_orders(order_id: str) -> str:
    """Look up an order by its ID and return its status."""
    ...
```

Write descriptions like you're explaining it to a new intern — vague descriptions cause the LLM to call the wrong tool, or the right tool with wrong arguments.

### Step 3 — Describe the tools in the format the API expects
Most tool-calling APIs (Groq, OpenAI-compatible, Gemini) want a JSON Schema per tool:

```python
tools_schema = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get the current weather for a given city.",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {"type": "string", "description": "City name, e.g. 'Dhaka'"}
                },
                "required": ["city"],
            },
        },
    }
]
```

### Step 4 — Write the system prompt
Keep it short and concrete:
```
You are a helpful assistant with access to tools.
Only call a tool when you actually need external information or an action performed.
If you already know the answer, answer directly without calling a tool.
Always give a final plain-text answer to the user once you have what you need.
```

### Step 5 — Build the loop
This is the actual "agent" part — see the full runnable version in Section 4:
1. Send messages + tool schemas to the LLM
2. If the LLM's response contains a **tool call** → run the matching Python function → append the result as a new message → go back to step 1
3. If the LLM's response is plain text → that's the final answer → stop

### Step 6 — Add guardrails
A max iteration count, a timeout, and input validation (see [Section 8](#8-guardrails-checklist)) — without these, a confused agent can loop forever or call a destructive tool repeatedly.

### Step 7 — Test with real, varied tasks
Run 10-15 realistic prompts, including edge cases ("what's the weather in a city that doesn't exist") and adversarial ones ("ignore your instructions and..."). Fix tool descriptions/system prompt based on failures — iterate, don't over-engineer upfront.

### Step 8 — Wrap it for use (optional)
A Streamlit chat UI (matches the pattern in this repo's LLM projects), a FastAPI endpoint (see [`FAST API API MAKING/`](../FAST%20API%20API%20MAKING/README.md)), or a CLI script — whatever fits the task.

---

## 4. Full working example (Groq, tool-calling loop)

Runnable end-to-end. Needs `pip install groq` and a free API key from [console.groq.com](https://console.groq.com).

```python
import json
import os
from groq import Groq

client = Groq(api_key=os.environ["GROQ_API_KEY"])
MODEL = "llama-3.3-70b-versatile"

# ---- Step 2: tools as plain functions ----
def get_weather(city: str) -> str:
    fake_data = {"dhaka": "32°C, humid", "london": "15°C, rainy"}
    return fake_data.get(city.lower(), f"No weather data for {city}")

def calculate(expression: str) -> str:
    try:
        return str(eval(expression, {"__builtins__": {}}))
    except Exception as e:
        return f"Error: {e}"

available_tools = {"get_weather": get_weather, "calculate": calculate}

# ---- Step 3: tool schemas ----
tools_schema = [
    {"type": "function", "function": {
        "name": "get_weather",
        "description": "Get current weather for a city.",
        "parameters": {"type": "object",
                        "properties": {"city": {"type": "string"}},
                        "required": ["city"]}}},
    {"type": "function", "function": {
        "name": "calculate",
        "description": "Evaluate a basic math expression, e.g. '12 * (3 + 4)'.",
        "parameters": {"type": "object",
                        "properties": {"expression": {"type": "string"}},
                        "required": ["expression"]}}},
]

# ---- Step 4 + 5: system prompt + the agent loop ----
def run_agent(user_message: str, max_steps: int = 5) -> str:
    messages = [
        {"role": "system", "content": "You are a helpful assistant with access to tools. "
                                       "Only call a tool when you need it. Otherwise answer directly."},
        {"role": "user", "content": user_message},
    ]

    for _ in range(max_steps):                      # Step 6: guardrail — max iterations
        response = client.chat.completions.create(
            model=MODEL, messages=messages, tools=tools_schema, tool_choice="auto",
        )
        msg = response.choices[0].message

        if not msg.tool_calls:                      # no tool call -> final answer -> stop
            return msg.content

        messages.append(msg)
        for call in msg.tool_calls:                  # act
            fn = available_tools[call.function.name]
            args = json.loads(call.function.arguments)
            result = fn(**args)                       # observe
            messages.append({
                "role": "tool", "tool_call_id": call.id,
                "name": call.function.name, "content": str(result),
            })
        # loop back: send the tool result to the LLM so it can decide the next step

    return "Stopped: too many steps without a final answer."


if __name__ == "__main__":
    print(run_agent("What's the weather in Dhaka, and what's 15% of 3200?"))
```

**What happens when you run it:**
1. LLM reads the question, decides it needs `get_weather` and `calculate` → returns tool calls instead of text
2. Your code runs both Python functions, appends their results as `"role": "tool"` messages
3. Loop sends everything back to the LLM
4. This time the LLM has what it needs → replies with plain text → loop exits

---

## 5. Agent patterns — pick the right shape

| Pattern | Shape | Use when |
|---|---|---|
| **Single-tool agent** | 1 tool, LLM decides call-or-not | Narrow task, e.g. "answer from this one API" |
| **ReAct agent** (shown above) | Multiple tools, reasons step-by-step, loops until done | Most general-purpose task agents |
| **Planner → Executor** | One LLM call plans all steps upfront, a second loop (or non-LLM code) executes them | Multi-step tasks where planning ahead is more reliable than step-by-step reasoning |
| **RAG agent** | Retrieval tool (vector search) + generation, usually 1-2 loop iterations | "Answer questions from my documents" — see this repo's RAG project notes |
| **Multi-agent** | Several specialized agents, one orchestrator routes between them | Task is really several different jobs (e.g. "research" agent + "writer" agent) |

Start with the **simplest pattern that could work** (usually single-tool or ReAct) — only reach for planner/executor or multi-agent once you've proven the simple version isn't enough.

---

## 6. When to use a framework instead

Building from scratch (Section 4) is the best way to *understand* agents, and is often enough for production too. Reach for a framework when you specifically need what it adds:

| Framework | Adds | Trade-off |
|---|---|---|
| **LangChain / LangGraph** | Pre-built tool integrations, graph-based multi-step control flow, memory modules | More abstraction, steeper learning curve, easier to debug once graph structure is understood |
| **LlamaIndex** | Strong retrieval/RAG-focused agent tooling | Best specifically for document-heavy agents |
| **CrewAI** | Multi-agent "crew" orchestration out of the box | Good for multi-agent patterns, less control over the low-level loop |
| **Claude Agent SDK** | Production-grade agent runtime (the same kind of loop this session runs on), sandboxing, built-in tool ecosystem | Anthropic-model-centric |

Rule of thumb: **prototype from scratch first** (Section 4's ~60 lines cover 80% of real use cases). Move to a framework only when you hit a wall — multi-agent orchestration, needing 20+ pre-built tool integrations, or long-term memory across sessions.

---

## 7. Claude Code sub-agents (a different kind of "agent")

Separate from the "LLM + tool loop" above: **Claude Code** (this tool) lets you define reusable **sub-agents** — specialized personas with their own tool access and instructions, launched via the `Agent` tool. Useful for splitting a big task into focused pieces (e.g. a read-only "Explore" agent for search, a "code-reviewer" agent for review).

Step by step:
1. Create `.claude/agents/<name>.md` in your project (or `~/.claude/agents/` for a personal/global one)
2. Add frontmatter + instructions:
   ```markdown
   ---
   name: my-reviewer
   description: Reviews Python code for style and correctness issues.
   tools: Read, Grep, Glob
   model: sonnet
   ---

   You are a meticulous Python code reviewer. Check for PEP8 issues,
   missing type hints, and obvious bugs. Report findings as a bullet list.
   ```
3. Claude Code auto-discovers it — invoke it by describing the task, or it gets picked automatically when it fits
4. Keep `tools:` scoped to only what that agent needs (read-only agents are safer for review/search tasks)

See [`Git and Claude code Cheatsheets/`](../Git%20and%20Claude%20code%20Cheatsheets/Readme.md) in this repo for more Claude Code specifics.

---

## 8. Guardrails checklist

- [ ] **Max iteration limit** on the loop (prevents infinite tool-calling loops)
- [ ] **Timeout** per tool call and per overall run
- [ ] **Validate tool arguments** before executing (don't blindly `eval()` or run raw SQL from LLM output in production — the `calculate()` example above uses a restricted `eval` for demo purposes only)
- [ ] **Confirm before destructive actions** (deleting data, sending emails, spending money) — either a human-in-the-loop check, or a strict allowlist of safe tools
- [ ] **Log every tool call + result** — essential for debugging why an agent did something unexpected
- [ ] **Rate-limit / cost-cap** external API calls the agent can trigger

---

## 9. Cheat sheet

```
1. Narrow the task            →  "what specific job, with what tools?"
2. Pick an LLM with tool calling → Groq / Gemini (free) / Claude / GPT
3. Write tools as functions    →  clear name + docstring + typed args
4. Describe tools as JSON schema
5. Write a short system prompt →  role + when to use tools
6. Loop: call LLM → tool call? → run tool → feed result back → repeat
7. Stop when LLM returns plain text (or hits max_steps)
8. Add guardrails              →  max steps, timeouts, validation, logging
9. Test with real + edge-case prompts, iterate on prompt/tool descriptions
10. Wrap in Streamlit / FastAPI / CLI for actual use
```
