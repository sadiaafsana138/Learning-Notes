# GeoAI + LLM Satellite Intelligence System

> Step-by-Step Build Guide · Free + Paid Stack · 15 Project Ideas

---

## Section 1: System Architecture Overview

The full system is divided into 4 independent layers. Changing one layer does not break the others.

| Layer | What it does | Tools |
|---|---|---|
| **Data Layer** | Pull and process raw data from satellites | Google Earth Engine, rasterio, xarray |
| **Embedding Layer** | Convert pixels/regions into vectors | AlphaEarth, TESSERA, custom CNN |
| **Knowledge Base** | Index and store vectors + metadata | FAISS, ChromaDB, Qdrant |
| **Intelligence Layer** | Natural language query → answer | Groq, Gemini, RAG pipeline |

**Core idea:** Convert each satellite pixel or region into a vector (number array). Store those vectors in a database. When someone asks a question — embed the query into a vector, find nearest vectors, pass context to an LLM to generate an answer.

### Data Flow

```
Satellite (GEE / Sentinel)  →  Raw Raster Data
        |
        v
Preprocessing (cloud mask, reproject, normalize)
        |
        v
Embedding Model  →  64/128-dim vector per pixel/patch
        |
        v
FAISS Index  <-->  Metadata Store (coords, year, variables)
        |
        v
User Query  →  Query Embedding  →  k-NN Search
        |
        v
Retrieved Context  →  LLM (Groq / Gemini)  →  Response
```

---

## Section 2: Free Tier LLM Options

### 2.1 Groq

Fastest free LLM API. Uses LPU (Language Processing Unit) — response time 200–500ms.

| Model | Context | Speed | Best For | Rate Limit |
|---|---|---|---|---|
| llama-3.3-70b-versatile | 128K | ~800 tok/s | General reasoning, RAG | 30 req/min |
| llama-3.1-8b-instant | 128K | ~2000 tok/s | Fast responses, batch | 30 req/min |
| mixtral-8x7b-32768 | 32K | ~500 tok/s | Technical explanations | 30 req/min |
| gemma2-9b-it | 8K | ~900 tok/s | Lightweight tasks | 30 req/min |

```python
pip install groq
```

```python
from groq import Groq

client = Groq(api_key="gsk_YOUR_KEY_HERE")

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {"role": "system", "content": "You are a GeoAI assistant..."},
        {"role": "user", "content": satellite_context + user_query}
    ],
    temperature=0.1,   # Low temp for factual geo queries
    max_tokens=1024
)
print(response.choices[0].message.content)
```

- Free plan: 14,400 req/day (30 req/min)
- Paid: $0.05–0.09 per million tokens — very cheap
- Streaming and tool/function calling supported

---

### 2.2 Google AI Studio + Gemini Flash

Best for GeoAI because it's multimodal (image + text together), has a large context window, and is in the same ecosystem as Google Earth Engine.

| Model | Context | Image Input | Free Limit | Best For |
|---|---|---|---|---|
| gemini-2.0-flash | 1M tokens | Yes (up to 3600) | 15 req/min, 1M tok/day | Satellite image analysis |
| gemini-1.5-flash-8b | 1M tokens | Yes | 15 req/min | Fast lightweight tasks |
| gemini-1.5-pro | 2M tokens | Yes | 2 req/min (free) | Complex reasoning |
| text-embedding-004 | 2048 tokens | No | 1500 req/min | Query embedding |

```python
pip install google-generativeai Pillow
```

```python
import google.generativeai as genai
from PIL import Image

genai.configure(api_key="AIzaSy...")
model = genai.GenerativeModel("gemini-2.0-flash")

img = Image.open("sentinel2_patch.png")

response = model.generate_content([
    img,
    "This is a Sentinel-2 image of Dhaka. NDVI values: ...",
    "What vegetation changes do you observe?"
])
print(response.text)
```

---

### 2.3 Mistral AI

| Model | Context | Free? | Best For |
|---|---|---|---|
| mistral-small-latest | 32K | Yes (limited) | Fast structured output |
| open-mistral-7b | 32K | Via HuggingFace | Local deployment |
| mistral-embed | 8K | Yes | Text embedding for RAG |

```python
from mistralai import Mistral

client = Mistral(api_key="YOUR_KEY")

# Text embedding for RAG
embeddings = client.embeddings.create(
    model="mistral-embed",
    inputs=["NDVI increased by 0.3 in Sylhet region..."]
)
vector = embeddings.data[0].embedding  # 1024-dim
```

---

### 2.4 HuggingFace Inference API

Best for open-source embedding models.

| Model | Task | Size | Use Case |
|---|---|---|---|
| sentence-transformers/all-MiniLM-L6-v2 | Embedding | 80MB | Fast text embedding |
| BAAI/bge-large-en-v1.5 | Embedding | 1.3GB | Best quality embedding |
| microsoft/phi-3-mini-128k-instruct | LLM | 3.8B | Local lightweight LLM |
| google/flan-t5-large | Text2Text | 780MB | Structured query output |

```python
pip install sentence-transformers
```

```python
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("BAAI/bge-large-en-v1.5")

texts = [
    "Sylhet 2024: NDVI=0.72, GPP=8500, rainfall=3200mm",
    "Dhaka 2024: LST=38C, impervious=78%, NDVI=0.12",
]
embeddings = model.encode(texts)  # Shape: (2, 1024)
```

---

### 2.5 Cohere

| Feature | Free Tier | Notes |
|---|---|---|
| Command R | 1000 req/month | Good for RAG with citations |
| Embed v3 | 1000 req/month | 1024-dim, multilingual |
| Rerank | 1000 req/month | Re-rank retrieved docs for better accuracy |

---

### 2.6 Ollama — Local, Unlimited

Run models on your own machine — no rate limits, no cost.

```bash
# Install from https://ollama.ai
ollama pull llama3.2   # 3B model, needs 2GB RAM
ollama pull mistral    # 7B model, needs 5GB RAM
```

```python
import requests

response = requests.post("http://localhost:11434/api/generate",
    json={
        "model": "llama3.2",
        "prompt": satellite_context + query,
        "stream": False
    }
)
print(response.json()["response"])
```

---

### 2.7 OpenRouter — All Models, One API

Routes to 50+ models via a single API compatible with OpenAI SDK.

```python
from openai import OpenAI

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="sk-or-..."
)

# Some free models:
# meta-llama/llama-3.2-3b-instruct:free
# google/gemma-2-9b-it:free

response = client.chat.completions.create(
    model="meta-llama/llama-3.2-3b-instruct:free",
    messages=[{"role": "user", "content": query}]
)
```

---

### Provider Comparison

| Provider | Rate Limit | Image Support | Embedding | Bengali Output | Best Use |
|---|---|---|---|---|---|
| Groq | 30 req/min | No | No | Good | Fast RAG responses |
| Google AI Studio | 15 req/min | **Yes (best)** | Yes | Excellent | Satellite image analysis |
| Mistral | Limited free | No | **Yes (best)** | OK | Text embedding + RAG |
| HuggingFace | Limited | No | Yes (local) | OK | Local embeddings |
| Cohere | 1K/month | No | Yes | OK | RAG reranking |
| Ollama | Unlimited | No | Yes (local) | OK | Local dev/testing |
| OpenRouter | Varies | Some | No | Varies | Model comparison |

---

## Section 3: Paid Options

| Provider | Model | Price (per 1M tokens) | Advantage |
|---|---|---|---|
| OpenAI | GPT-4o | $2.50 in / $10 out | Best reasoning, vision |
| OpenAI | GPT-4o-mini | $0.15 / $0.60 | Cheap, good quality |
| Anthropic | Claude 3.5 Sonnet | $3 / $15 | 200K context, best analysis |
| Anthropic | Claude 3 Haiku | $0.25 / $1.25 | Fast, cheap |
| Google | Gemini 1.5 Pro | $1.25 / $5 | 2M context |
| Groq | Llama 3.3 70B | $0.59 / $0.79 | Fastest paid option |
| Cohere | Command R+ | $2.5 / $10 | Best RAG citations |

> Recommendation: Build and test the full pipeline with free tier first. Then switch to paid based on actual volume. For most GeoAI projects, **Groq paid + Google Vertex AI** is the most cost-effective combination.

---

## Section 4: What to Learn — Priority Order

### Install Everything

```bash
pip install numpy pandas matplotlib folium jupyter
pip install rasterio xarray geopandas shapely
pip install earthengine-api geemap
pip install faiss-cpu chromadb sentence-transformers
pip install groq google-generativeai
pip install langchain langchain-community
pip install fastapi uvicorn
```

### Phase 1: Python Basics (Week 1–2)

- numpy, pandas — array operations
- matplotlib, folium — visualization
- requests — API calls
- Jupyter Notebook — development environment

### Phase 2: Satellite Data — Google Earth Engine (Week 3–4)

1. Register: [earthengine.google.com/signup](https://earthengine.google.com/signup)
2. Authenticate: `ee.Authenticate()` + `ee.Initialize()`
3. Filter image collections by date, location, cloud cover
4. Calculate band indices (NDVI, EVI, MNDWI)
5. Extract time series per location
6. Export to Google Drive / GCS

```python
import ee
import geemap

ee.Authenticate()
ee.Initialize(project="your-project-id")

aoi = ee.Geometry.Rectangle([88.0, 20.5, 92.7, 26.6])  # Bangladesh

collection = (ee.ImageCollection("MODIS/006/MOD13A2")
    .filterDate("2020-01-01", "2024-12-31")
    .filterBounds(aoi))

def add_ndvi(img):
    ndvi = img.normalizedDifference(["sur_refl_b02", "sur_refl_b01"])
    return img.addBands(ndvi.rename("NDVI"))

with_ndvi = collection.map(add_ndvi)
```

### Phase 3: Embeddings (Week 5–6)

**Option A — AlphaEarth (easiest, start here):**

```python
# Pre-built 64-dim vectors available directly in GEE
embedding_dataset = ee.ImageCollection("GOOGLE/SATELLITE_EMBEDDING/V1/ANNUAL")
emb_2023 = embedding_dataset.filterDate("2023-01-01", "2023-12-31").first()

point = ee.Geometry.Point([90.4125, 23.8103])  # Dhaka

values = emb_2023.sample(region=point, scale=10, numPixels=1).first().toDictionary()
# Returns 64-dimensional vector: A00 through A63
```

**Option B — Custom Patch Encoder:**

```python
import torch
import torch.nn as nn

class SatellitePatchEncoder(nn.Module):
    def __init__(self, in_channels=12, embed_dim=128):
        super().__init__()
        self.encoder = nn.Sequential(
            nn.Conv2d(in_channels, 64, 3, padding=1),
            nn.ReLU(),
            nn.Conv2d(64, 128, 3, padding=1),
            nn.AdaptiveAvgPool2d(4),
            nn.Flatten(),
            nn.Linear(128*4*4, embed_dim)
        )

    def forward(self, x):
        return self.encoder(x)

# Input: (batch, 12_bands, 64, 64)
# Output: (batch, 128)
```

### Phase 4: Vector Store (Week 7–8)

**FAISS — fastest, best for millions of vectors:**

```python
import faiss
import numpy as np
import json

dim = 64
index = faiss.IndexFlatIP(dim)  # Inner product (cosine similarity)

vectors = np.random.randn(10000, dim).astype("float32")
faiss.normalize_L2(vectors)
index.add(vectors)

faiss.write_index(index, "satellite_index.faiss")

# Query
query_vec = np.random.randn(1, dim).astype("float32")
faiss.normalize_L2(query_vec)
distances, indices = index.search(query_vec, k=10)
```

**ChromaDB — easier, persistent, with metadata filtering:**

```python
import chromadb

client = chromadb.PersistentClient(path="./satellite_db")
collection = client.get_or_create_collection("bangladesh_2023")

collection.add(
    embeddings=vectors.tolist(),
    metadatas=[{"lat": 23.8, "lon": 90.4, "ndvi": 0.45, "region": "Dhaka"}],
    ids=["loc_001"]
)

# Query with metadata filter
results = collection.query(
    query_embeddings=[query_vec.tolist()],
    n_results=10,
    where={"region": "Sylhet"}
)
```

| Vector Store | Setup | Speed | Persistence | Filtering | Best For |
|---|---|---|---|---|---|
| FAISS | pip install | Fastest | Manual save | Post-filter | Large scale (millions) |
| ChromaDB | pip install | Fast | Auto | Pre-filter | Medium scale + metadata |
| Qdrant | Docker | Fast | Auto | Advanced | Production deployment |
| Pinecone | Cloud API | Fast | Cloud | Advanced | Managed cloud |

> **Recommendation:** Start with ChromaDB — simple, persistent, supports filtering. Move to Qdrant or Pinecone for production.

### Phase 5: Full RAG Pipeline (Week 9–10)

```python
from groq import Groq
import chromadb
from sentence_transformers import SentenceTransformer

groq_client = Groq(api_key="gsk_...")
chroma = chromadb.PersistentClient("./satellite_db")
collection = chroma.get_collection("bangladesh_2023")
embedder = SentenceTransformer("BAAI/bge-large-en-v1.5")

def satellite_rag(user_query: str, region: str = None):
    # Step 1: Embed the query
    query_emb = embedder.encode([user_query])[0].tolist()

    # Step 2: Find similar locations
    filter_dict = {"region": region} if region else None
    results = collection.query(
        query_embeddings=[query_emb],
        n_results=5,
        where=filter_dict
    )

    # Step 3: Build context
    context = "\n".join([
        f"Location: {m['region']}, Lat: {m['lat']}, Lon: {m['lon']}"
        f", NDVI: {m.get('ndvi', 'N/A')}, LST: {m.get('lst', 'N/A')}"
        for m in results["metadatas"][0]
    ])

    # Step 4: LLM response
    response = groq_client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": """You are a GeoAI assistant.
             Answer based on satellite data. Be specific with numbers.
             Respond in Bengali if the question is in Bengali."""},
            {"role": "user", "content": f"Context:\n{context}\n\nQuestion: {user_query}"}
        ],
        temperature=0.1
    )
    return response.choices[0].message.content
```

---

## Section 5: Cost Optimization Strategies

### Embedding Caching (biggest saver — 80–90% compute reduction)

```python
import hashlib
import pickle
from pathlib import Path

CACHE_DIR = Path("./embedding_cache")
CACHE_DIR.mkdir(exist_ok=True)

def get_cached_embedding(lat, lon, year, model):
    cache_key = f"{lat:.4f}_{lon:.4f}_{year}"
    cache_file = CACHE_DIR / f"{hashlib.md5(cache_key.encode()).hexdigest()}.pkl"

    if cache_file.exists():
        with open(cache_file, "rb") as f:
            return pickle.load(f)

    embedding = compute_embedding(lat, lon, year, model)
    with open(cache_file, "wb") as f:
        pickle.dump(embedding, f)
    return embedding
```

### GEE Batch Extraction

```python
# Wrong (slow): one by one
for point in points:
    embedding = get_embedding(point)  # N API calls

# Right (fast): batch
fc = geemap.geopandas_to_ee(gdf)
result = embedding_image.sampleRegions(
    collection=fc,
    scale=10,
    geometries=True
)
# 1 call, N results
```

### Token Optimization

| Strategy | Token Saving | How |
|---|---|---|
| Context pruning | 40–60% | Send top-3 results, not 10 |
| Structured prompt | 20–30% | Request JSON output, not narrative |
| Response caching | 100% for repeats | Cache common queries with Redis/dict |
| Smart model routing | 5–10x cheaper | Simple queries → Llama 8B, hard → 70B |

### Recommended Stack by Budget

| Budget | Data | Embedding | Vector Store | LLM | Monthly Cost |
|---|---|---|---|---|---|
| Zero (Learning) | GEE free | AlphaEarth GEE | ChromaDB local | Groq free + Gemini free | $0 |
| Low ($10–50) | GEE free | TESSERA API | ChromaDB local | Groq paid | $10–30 |
| Medium ($50–200) | GEE + S2 API | AlphaEarth API | Qdrant cloud | Groq + Gemini Flash | $50–150 |
| Production ($200+) | GEE Pro | Custom model | Pinecone | GPT-4o mini / Claude Haiku | $200+ |

---

## Section 6: 15 Project Ideas — Bangladesh Focus

### Tier 1 — Easy (1–2 weeks)

| # | Project | What it does | Data + Stack |
|---|---|---|---|
| 1 | Flood Early Warning | Flash flood risk in haor areas with LLM Bengali alerts | MODIS NDVI, ERA5 rainfall, Groq Llama |
| 2 | Urban Heat Map | LST time series — which ward is hottest? Where to plant trees? | MODIS MOD11A2, Gemini Flash, ChromaDB |
| 3 | Crop Calendar Q&A | NDVI seasonality → optimal planting time query | MODIS NDVI, Groq, FAISS |
| 4 | River Width Tracker | Padma/Jamuna width change 2000–2024, annual trend | Landsat MNDWI, Gemini analysis |
| 5 | Air Quality Proxy | Sentinel-5P AOD → Dhaka air quality trend | Sentinel-5P, Groq, simple RAG |

### Tier 2 — Medium (2–4 weeks)

| # | Project | What it does | Data + Stack |
|---|---|---|---|
| 6 | Mangrove Health Monitor | Sundarbans NDVI+MNDWI time series, sector degradation | Sentinel-2, AlphaEarth, ChromaDB, Groq |
| 7 | Cyclone Impact Assessment | Before/after Sentinel-1 SAR comparison, LLM damage report | Sentinel-1 GRD, change detection, Gemini |
| 8 | Shrimp Farm Monitor | Coastal gher water quality proxy, turbidity anomaly alerts | Sentinel-2, custom embedding, Groq |
| 9 | Land Use Change Q&A | 10-year land cover change, natural language queries | Dynamic World, AlphaEarth, RAG |
| 10 | Multi-hazard Risk Score | Flood + drought + erosion combined per upazila | Multiple MODIS products, FAISS, Groq |

### Tier 3 — Advanced (1–2 months, paper-level)

| # | Project | What it does | Data + Stack |
|---|---|---|---|
| 11 | Bangladesh ESE System | Paper 1 approach: 12 ecological vars + satellite embedding + LLM reasoning | MODIS 12 vars, Prithvi-EO, GeoChat, LoRA |
| 12 | Fishing Ground AI | Bay of Bengal SST + chlorophyll embedding, Bengali output | MODIS Aqua, VIIRS, custom model, Groq |
| 13 | Carbon Stock Estimator | AGB proxy → pixel-level carbon map, forest credit calculation | GEDI, Sentinel-2, AlphaEarth, RAG |
| 14 | Crop Yield Predictor | NDVI phenology + weather + soil → upazila-level forecast | MODIS, ERA5, SoilGrids, Transformer |
| 15 | Real-time Flood Mapper | SAR + optical fusion, live flood extent, emergency LLM | Sentinel-1+2, Copernicus EMS, GPT-4o |

---

## Section 7: Step-by-Step Roadmap

### Day 1–3: Environment Setup

1. Open Google Colab — enable T4 GPU runtime (free)
2. Sign up for Google Earth Engine: [earthengine.google.com/signup](https://earthengine.google.com/signup)
3. Get Groq API key: [console.groq.com](https://console.groq.com) (free)
4. Get Google AI Studio key: [aistudio.google.com](https://aistudio.google.com) (free)
5. Run this to verify everything works:

```python
!pip install earthengine-api geemap groq google-generativeai
!pip install faiss-cpu chromadb sentence-transformers

import ee
ee.Authenticate()
ee.Initialize(project="your-gee-project")

# Test: Bangladesh NDVI
point = ee.Geometry.Point([90.4, 23.8])
ndvi = ee.ImageCollection("MODIS/006/MOD13A2").first()
val = ndvi.sample(region=point, scale=250).first().get("NDVI")
print("NDVI:", ee.Number(val).getInfo())

# Test: Groq
from groq import Groq
client = Groq(api_key="gsk_...")
r = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[{"role": "user", "content": "Say hello in Bengali"}]
)
print(r.choices[0].message.content)
```

### Week 1: First Mini Project — Dhaka Urban Heat

1. Pull Dhaka LST data from GEE (2020–2024)
2. Calculate ward-level averages
3. Store in ChromaDB
4. Q&A with Groq: "Which ward is hottest?"
5. Keep demo running in Colab

### Week 2–3: Embedding Pipeline

1. Extract AlphaEarth embeddings from GEE (64-dim)
2. Build FAISS index
3. Test similarity search — find physically similar locations
4. Generate answers from retrieved context using Groq

### Week 4: Full RAG System

1. Complete the query pipeline (see Section 5 code)
2. Add Bengali + English dual language support
3. Build a simple API with FastAPI
4. Build a demo UI with Streamlit

### Month 2+: Scale Up

1. Add time series data (2000–2024)
2. Add more variables (NDVI, GPP, LST, rainfall)
3. Pick a specific project from the 15 ideas above
4. Validate against ground truth data
5. Consider writing a paper

---

## Quick Reference Links

| Resource | URL | Purpose |
|---|---|---|
| GEE Signup | earthengine.google.com/signup | Satellite data access |
| Groq Console | console.groq.com | Free LLM API key |
| Google AI Studio | aistudio.google.com | Gemini API key |
| AlphaEarth Paper | arxiv.org/abs/2507.22291 | Embedding model docs |
| Geemap Docs | geemap.org | Python GEE wrapper |
| FAISS Docs | faiss.ai | Vector search library |
| ChromaDB Docs | docs.trychroma.com | Vector database |
| LangChain Docs | python.langchain.com | RAG framework |
| HuggingFace Models | huggingface.co/models | Open source models |
| Colab | colab.research.google.com | Free GPU compute |
| Copernicus Data | dataspace.copernicus.eu | Free Sentinel data |
| Bangladesh Admin | data.humdata.org | Admin boundaries |
