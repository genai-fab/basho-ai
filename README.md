# Build Your First AI-powered Web Application

## Workshop Overview

This repository contains the progressive demos for building AI-powered web applications using Streamlit and local LLMs via Ollama.

## Prerequisites

- **Ollama installed** with at least one model (e.g., `llama3.2`, `qwen2.5:0.5b`)
- **Python 3.8+** with `uv` package manager
- **Basic command line familiarity**

## Setup

1. **Clone this repository:**
   ```bash
   git clone https://github.com/genai-fab/basho-ai.git
   cd basho-ai
   ```

2. **Install dependencies:**
   ```bash
   uv sync
   ```

3. **Activate virtual environment:**
   ```bash
   source .venv/bin/activate  # Mac/Linux
   # or
   .venv\Scripts\activate     # Windows
   ```

4. **Ensure Ollama is running:**
   ```bash
   ollama serve
   ```

## Workshop Progression

### Stage 1: API Fundamentals
**Demo:** Command line with `curl`

Test your local AI with a direct API call:
```bash
curl -X POST http://localhost:11434/api/generate \
  -H "Content-Type: application/json" \
  -d '{
    "model": "llama3.2",
    "prompt": "Explain what an API is in one sentence.",
    "stream": false
  }'
```

### Stage 2: Simple Web Interface
**File:** `01_simple_app.py`

Your first Streamlit app - a basic AI chat interface.

```bash
streamlit run 01_simple_app.py
```

**Key Learning:** Same API call, now with a user-friendly web interface.

### Stage 3: Prompt Engineering
**File:** `02_haiku_app.py`

Demonstrates how prompts control AI behavior - same model, completely different output.

```bash
streamlit run 02_haiku_app.py
```

**Key Learning:** AI applications are really "prompt applications."

### Stage 4: Complex AI Workflows
**File:** `03_haiku_challenge.py`

A complete interactive application with multiple AI roles:
- **AI as Creator** - Generates themes
- **AI as Critic** - Evaluates user haikus
- **AI as Poet** - Creates competing haikus

```bash
streamlit run 03_haiku_challenge.py
```

**Key Learning:** Complex AI apps are built by chaining simple API calls.

### Stage 5: Advanced Features
**File:** `04_haiku_models.py`

Adds model selection and comparison capabilities.

```bash
streamlit run 04_haiku_models.py
```

**Key Learning:** Making applications configurable and production-ready.

## Script Descriptions

| Script | Purpose | Key Concepts |
|--------|---------|--------------|
| `01_simple_app.py` | Basic AI chat interface | API integration, Streamlit basics |
| `02_haiku_app.py` | Prompt engineering demo | Instruction-following, output formatting |
| `03_haiku_challenge.py` | Interactive haiku game | Multiple AI calls, state management |
| `04_haiku_models.py` | Model selection interface | Configuration, model comparison |

## Common Issues

**Ollama not responding:**
```bash
# Check if Ollama is running
ollama list

# Start Ollama if needed
ollama serve
```

**Model not found:**
```bash
# Pull a model if needed
ollama pull llama3.2
```

**Port conflicts:**
```bash
# Streamlit uses port 8501 by default
# Use different port if needed
streamlit run app.py --server.port 8502
```

## Next Steps

After completing the workshop, you can:

1. **Modify the haiku app** for different creative challenges
2. **Apply these patterns** to other AI tasks (summarization, translation, etc.)
3. **Explore advanced features** like streaming responses, memory, or multi-model ensembles
4. **Deploy your app** using Streamlit Cloud, Docker, or other platforms

## Resources

- [Streamlit Documentation](https://docs.streamlit.io/)
- [Ollama Documentation](https://ollama.ai/docs)
- [Anthropic Prompt Engineering Guide](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview)

## Workshop Goals Achieved ✅

By the end of this workshop, you will have:
- ✅ Built a complete AI-powered web application
- ✅ Understood API fundamentals for AI integration
- ✅ Mastered basic prompt engineering techniques
- ✅ Learned to chain multiple AI interactions
- ✅ Gained confidence to build your own AI applications

---

*Built with ❤️ for learning AI application development*