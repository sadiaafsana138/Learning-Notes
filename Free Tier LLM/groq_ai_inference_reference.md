# Groq & Free AI Inference — Reference Guide

> Models · Categories · Free API Providers · Use-Case Mapping

---

## 1. What is Groq?

Groq is an **ultra-fast AI inference platform**. It does not train its own models — instead it runs open-source community models at extreme speed using custom **LPU (Language Processing Unit)** hardware.

**Key points:**
- Does not train models — hosts open-source ones
- LPU is faster than GPU for inference
- API-first, developer-friendly
- Free tier available — ideal for personal projects and experimentation
- Production-grade speed: 500+ tokens/second possible

**Official links:**
- Console: [console.groq.com](https://console.groq.com)
- Docs: [console.groq.com/docs](https://console.groq.com/docs)

---

## 2. Model Categories

### 2.1 Reasoning Models

Optimized for complex logic, multi-step thinking, coding, math, and AI agent tasks.

| Model | Size | Best For | Notes |
|---|---|---|---|
| GPT OSS 120B | 120B | Complex coding, multi-step agents, research | Largest & strongest — slower but most capable |
| GPT OSS 20B | 20B | Chatbot, basic automation, fast tasks | Cheaper + faster than 120B |
| Qwen 3 32B | 32B | Multilingual reasoning, coding, Bangla | Alibaba Cloud — very efficient per token |

### 2.2 Function Calling / Tool Use

Used in AI agent pipelines. The model can call real-world APIs, databases, calculators, etc.

**Example flow:**
```
User: "What's the weather in Dhaka?"
→ Model calls: weather_api("Dhaka")
→ Returns structured result
```

| Model | Tool Calling Quality | Use Case |
|---|---|---|
| GPT OSS 120B | Excellent | Complex multi-tool agents |
| GPT OSS 20B | Good | Simple function calls |
| Llama 4 Scout | Very Good | Fast agentic workflows |
| Qwen 3 32B | Good | Multilingual tool use |

### 2.3 Text to Speech (TTS)

Generates natural human-like voice from text input.

| Model | Language | Use Case |
|---|---|---|
| Orpheus English | English | AI caller, audiobook, voice assistant, IVR |
| Orpheus Arabic Saudi | Arabic (Saudi) | Arabic voice bot, IVR, customer support |

Common use cases: AI interview bots, voice-enabled dashboards, call center automation.

### 2.4 Speech to Text (STT)

Takes audio/voice input and returns accurate transcribed text. Uses OpenAI Whisper architecture.

| Model | Speed | Accuracy | Best For |
|---|---|---|---|
| Whisper Large v3 | Slower | Very High | Meeting transcription, subtitles, archival |
| Whisper Large v3 Turbo | Fast | High | Real-time apps, voice bots, live transcription |

> Bangla speech support exists in Whisper — accuracy is moderate.

### 2.5 Text to Text (LLM Chat)

Standard LLM for chat, summarization, Q&A, code generation, etc.

| Model | Context Window | Strength | Speed |
|---|---|---|---|
| GPT OSS 120B | Long | Best quality output | Slower |
| GPT OSS 20B | Medium | Balanced quality/speed | Fast |
| Llama 4 Scout | Very Long (10M+) | Vision + text, agent workflows | Very Fast |
| Llama 3.3 70B | Medium | Strong open-source general model | Fast |

### 2.6 Vision Models

Understands image input. Multimodal — processes text + image together.

| Model | Capability |
|---|---|
| Llama 4 Scout | Image captioning, OCR, chart analysis, UI screenshot understanding, diagram parsing |

Use cases: document analysis, dashboard screenshot reading, product image tagging.

### 2.7 Multilingual Models

| Model | Bangla Quality | Other Languages |
|---|---|---|
| GPT OSS 120B | Decent | 100+ languages |
| GPT OSS 20B | Mixed | 100+ languages |
| Qwen 3 32B | Surprisingly Good | CJK, Arabic, Bengali strong |
| Llama 3.3 70B | Moderate | Major European + Asian languages |
| Whisper Large v3 | Good (speech) | 98+ languages for STT |

### 2.8 Safety / Content Moderation

Detects harmful, toxic, and NSFW content. Used as a filter in production pipelines.

| Model | Use Case |
|---|---|
| Safety GPT OSS 20B | Toxic content filtering, NSFW detection, moderation pipeline, safety scoring |

> Common practice: run this model on user input **before** the main LLM to sanitize requests.

---

## 3. Free API Platforms

| Platform | Free Tier | Notable Models | Best For |
|---|---|---|---|
| **Groq** | Yes — generous | Llama, Qwen, Whisper, GPT OSS | Fastest inference, easiest to start |
| **OpenRouter** | Some free models | Claude, GPT, Llama, Qwen, DeepSeek | Multi-model experimentation |
| **Hugging Face Inference** | Limited free | Llama, Mistral, Qwen, Whisper, SDXL | Open-source model hub, research |
| **Together AI** | Free credits (new users) | Open-source LLMs, image, embeddings | Production-grade open-source API |
| **Fireworks AI** | Free trial | Llama, Qwen, DeepSeek, vision | Fast inference, structured output |
| **Cerebras Inference** | Free tier | Llama variants | Extremely fast, long context |
| **Google AI Studio** | Free (Gemini) | Gemini Flash, Pro | Vision, long context, multimodal |
| **Cloudflare Workers AI** | Free edge AI | Llama, Mistral, Whisper | Edge deployment, serverless |

### Groq Quick Start

```python
pip install groq
```

```python
from groq import Groq

client = Groq(api_key="YOUR_KEY")

response = client.chat.completions.create(
    model="qwen-qwq-32b",
    messages=[{"role": "user", "content": "Explain transformers"}]
)

print(response.choices[0].message.content)
```

---

## 4. Available Free / Open-Source Model Families

| Model Family | Parameter Range | Strengths | Free Platforms |
|---|---|---|---|
| Llama 3 / 4 (Meta) | 8B – 405B | General chat, coding, vision (Scout) | Groq, Together, Fireworks |
| Qwen 2.5 / 3 (Alibaba) | 7B – 72B | Multilingual, coding, reasoning | Groq, OpenRouter, Together |
| DeepSeek R1 | 7B – 671B | Math, reasoning, chain-of-thought | OpenRouter, Together, Fireworks |
| Mistral / Mixtral | 7B – 8x22B | Fast, lightweight, European language | OpenRouter, Together, HuggingFace |
| Gemma (Google) | 2B – 27B | Small, efficient, mobile-friendly | OpenRouter, HuggingFace |
| Whisper (OpenAI) | Small – Large | Speech-to-text, multilingual STT | Groq, HuggingFace |
| Phi (Microsoft) | 1B – 14B | Tiny but capable, local AI | OpenRouter, HuggingFace |
| Stable Diffusion | Various | Image generation | HuggingFace, Together |

---

## 5. Use Case → Best Model Mapping

| Task | Recommended Model | Platform | Notes |
|---|---|---|---|
| Python / Data coding | Qwen 3 32B | Groq | Strong code generation |
| Complex AI agent | GPT OSS 120B | Groq | Multi-step tool calling |
| Bangla chat / NLP | Qwen 3 32B | Groq / OpenRouter | Best open-source Bangla support |
| Voice STT | Whisper Large v3 Turbo | Groq | Fast, good accuracy |
| Vision / Screenshot | Llama 4 Scout | Groq / Together | Multimodal, long context |
| Cheap fast chat | Llama 3.3 70B | Groq | Fast inference, free tier |
| Safety filtering | Safety GPT OSS 20B | Groq | Pre-production moderation |
| Math / Reasoning | DeepSeek R1 | OpenRouter | Chain-of-thought specialist |
| Long context tasks | Llama 4 Scout | Groq | 10M+ token context window |
| Multimodal / Vision+Text | Gemini Flash | Google AI Studio | Free, very capable |

---

## 6. Recommended Free Stack

For Data / ML Engineers building voice bots, AI agents, or FastAPI-based systems:

| Layer | Tool / Model | Cost | Notes |
|---|---|---|---|
| API Provider | Groq | Free | Fastest inference, easy SDK |
| Chat Model | Qwen 3 32B | Free (Groq) | Best for Bangla + coding |
| Agent Model | GPT OSS 120B | Free (Groq) | Complex workflows |
| STT | Whisper Large v3 Turbo | Free (Groq) | Real-time voice transcription |
| Backend | FastAPI (Python) | Free | Async, production-ready |
| UI / Demo | Streamlit | Free | Rapid prototyping |
| Orchestration | LangChain / LlamaIndex | Free | Agent + RAG pipelines |
| Deployment | Railway / Render | Free tier | Easy deploy from GitHub |
| Database | Supabase / SQLite | Free tier | Memory + logging |

### Architecture — Voice AI Agent Flow

```
User speaks
    → Whisper Turbo (STT) → text
    → [Safety GPT OSS 20B] → moderated text   (optional)
    → Groq LLM (Qwen / Llama) → response
    → Orpheus TTS → voice output
    
FastAPI handles all routing and orchestration
```

---

## Quick Links

| Resource | URL |
|---|---|
| Groq Console (API key) | console.groq.com |
| OpenRouter | openrouter.ai |
| HuggingFace Inference | huggingface.co/inference-api |
| Together AI | together.ai |
| Google AI Studio (Gemini) | aistudio.google.com |
