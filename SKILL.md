---
name: agentcode
description: "Intelligent coding agent with smart routing across 7 verified free AI models. Auto-selects best model for task type. Supports multimodal, fast coding, terminal tasks, and more."
license: MIT
version: "0.0.1"
author: "AgentCode Contributors"
category: "coding-agent"
models:
  - "opencode/mimo-v2.5-free"
  - "opencode/deepseek-v4-flash-free"
  - "opencode/laguna-s-2.1-free"
  - "opencode/ling-3.0-flash-free"
  - "opencode/north-mini-code-free"
  - "opencode/nemotron-3-ultra-free"
  - "opencode/big-pickle"
verification:
  - "https://huggingface.co/Xiaomi-MiMo"
  - "https://platform.deepseek.com/api-docs"
  - "https://build.nvidia.com/nvidia/laguna-2-1"
  - "https://help.aliyun.com/zh/model-studio/getting-started/models"
  - "https://build.nvidia.com/nvidia/north-mini-code"
  - "https://build.nvidia.com/nvidia/nemotron-3-ultra"
---

# AgentCode - Smart Multi-Model Coding Agent

## Overview

AgentCode is an intelligent routing system that combines **7 verified free AI models** into a single coding agent. It automatically analyzes your task and selects the optimal model based on task type, context requirements, and performance needs.

### Key Features

- **Smart Routing**: Automatically selects the best model for each task
- **7 Verified Models**: All models linked to official documentation
- **Multimodal Support**: Image, audio, and video analysis
- **High Performance**: Up to 126 tokens/second
- **Enterprise Ready**: 1M context window
- **Local Deployment**: Sovereign AI support

---

## Verified Models

| Model | Provider | Strength | Context | Speed | Verification |
|-------|----------|----------|---------|-------|--------------|
| MiMo-V2.5 | Xiaomi | Multimodal | 1M | Medium | [Link](https://huggingface.co/Xiaomi-MiMo) |
| DeepSeek V4 Flash | DeepSeek | Speed | 1M | 126 tok/s | [Link](https://platform.deepseek.com/api-docs) |
| Laguna S 2.1 | NVIDIA | Terminal | 1M | High | [Link](https://build.nvidia.com/nvidia/laguna-2-1) |
| Ling-3.0-flash | Alibaba | Efficiency | 256K | Medium | [Link](https://help.aliyun.com/zh/model-studio/getting-started/models) |
| North Mini Code | NVIDIA | Local | 256K | Medium | [Link](https://build.nvidia.com/nvidia/north-mini-code) |
| Nemotron 3 Ultra | NVIDIA | Enterprise | 1M | 300+ tok/s | [Link](https://build.nvidia.com/nvidia/nemotron-3-ultra) |
| Big Pickle | Stealth | Daily Coding | 200K | Medium | N/A |

---

## Installation

### Option 1: Manual Install (Recommended)

```bash
# Create skill directory
mkdir -p ~/.config/opencode/skills/agentcode

# Download SKILL.md
curl -fsSL https://raw.githubusercontent.com/mrcbrbn5361/agentcode/main/SKILL.md \
  -o ~/.config/opencode/skills/agentcode/SKILL.md
```

### Option 2: Git Clone

```bash
# Clone into skills directory
cd ~/.config/opencode/skills
git clone https://github.com/mrcbrbn5361/agentcode.git
```

### Option 3: OpenCode Config

Add to your `opencode.json`:

```json
{
  "$schema": "https://opencode.ai/config.json",
  "skills": {
    "paths": ["~/.config/opencode/skills"]
  }
}
```

---

## Usage Examples

### Example 1: Quick Code Generation

**Input:**
```
User: "Create a Python FastAPI endpoint for user authentication"
```

**AgentCode Analysis:**
- Task type: Quick code generation
- Recommended model: DeepSeek V4 Flash
- Reason: 126 tokens/second, fastest for code generation

**Result:**
```python
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

app = FastAPI()

@app.post("/auth/login")
async def login(credentials: LoginRequest, db: Session = Depends(get_db)):
    user = authenticate_user(db, credentials.email, credentials.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"access_token": create_token(user.id), "token_type": "bearer"}
```

---

### Example 2: Image Analysis

**Input:**
```
User: "What's wrong with this UI? [attaches screenshot]"
```

**AgentCode Analysis:**
- Task type: Multimodal (image analysis)
- Recommended model: MiMo-V2.5
- Reason: Native image understanding

**Result:**
```
I can see the issue in your UI:
1. The button is overlapping with the text label
2. The padding is too small (currently 8px)
3. The color contrast doesn't meet WCAG standards

Here's the fix:
```css
.submit-button {
  padding: 16px 24px;
  margin-top: 16px;
  background-color: #007bff;
  color: white;
}
```

---

### Example 3: Terminal Task

**Input:**
```
User: "Create a Docker compose file for a Node.js app with PostgreSQL and Redis"
```

**AgentCode Analysis:**
- Task type: Terminal/CLI task
- Recommended model: Laguna S 2.1
- Reason: Terminal-Bench 70.2% (highest for open-weight)

**Result:**
```yaml
version: '3.8'
services:
  app:
    build: .
    ports:
      - "3000:3000"
    environment:
      - DATABASE_URL=postgresql://user:pass@db:5432/mydb
      - REDIS_URL=redis://redis:6379
    depends_on:
      - db
      - redis
  db:
    image: postgres:15-alpine
    environment:
      - POSTGRES_USER=user
      - POSTGRES_PASSWORD=pass
      - POSTGRES_DB=mydb
    volumes:
      - postgres_data:/var/lib/postgresql/data
  redis:
    image: redis:alpine
    ports:
      - "6379:6379"
volumes:
  postgres_data:
```

---

## Routing Logic

AgentCode automatically selects the optimal model based on:

| Factor | Consideration |
|--------|---------------|
| **Task Type** | Coding, analysis, planning, multimodal |
| **Context Size** | Small (<256K) vs Large (1M) |
| **Speed Requirement** | Real-time vs batch processing |
| **Cost Sensitivity** | Free tier vs premium models |
| **Privacy Needs** | Cloud vs local processing |

### Routing Decision Tree

```
Task Received
    │
    ├─→ Is it multimodal (image/sound/video)?
    │       YES → MiMo-V2.5
    │       NO ↓
    │
    ├─→ Is it terminal/CLI task?
    │       YES → Laguna S 2.1
    │       NO ↓
    │
    ├─→ Is speed critical?
    │       YES → DeepSeek V4 Flash
    │       NO ↓
    │
    ├─→ Is context >256K?
    │       YES → Nemotron 3 Ultra
    │       NO ↓
    │
    ├─→ Is it sensitive/local required?
    │       YES → North Mini Code
    │       NO ↓
    │
    ├─→ Is cost a concern?
    │       YES → Ling-3.0-flash
    │       NO ↓
    │
    └─→ Default → Big Pickle
```

---

## API Reference

### route_task()

Route a coding task to the optimal AI model.

```python
from agentcode import route_task, ModelType

model = route_task(
    task_description="Create a FastAPI endpoint",
    has_image=False,
    has_audio=False,
    has_video=False,
    context_size=0,
    is_local_only=False,
    is_budget_conscious=False
)

print(model)  # ModelType.DEEPSEEK
```

**Parameters:**
- `task_description` (str): Natural language description of the task
- `has_image` (bool): Whether task includes image input
- `has_audio` (bool): Whether task includes audio input
- `has_video` (bool): Whether task includes video input
- `context_size` (int): Estimated context size in tokens
- `is_local_only` (bool): Whether task requires local processing
- `is_budget_conscious` (bool): Whether task is budget-sensitive

**Returns:**
- `ModelType`: The optimal model for this task

---

### get_model_info()

Get detailed information about a model.

```python
from agentcode import get_model_info, ModelType

info = get_model_info(ModelType.MIMO)
print(info["name"])  # "MiMo-V2.5 Free"
print(info["provider"])  # "Xiaomi"
```

---

### get_all_models()

Get information about all available models.

```python
from agentcode import get_all_models

models = get_all_models()
for model in models:
    print(f"{model['model_id']}: {model['name']}")
```

---

## Privacy & Security

### Important Warnings

| Model | Privacy Note | Recommendation |
|-------|--------------|----------------|
| **Big Pickle** | Stealth model - identity undisclosed | Use only for low-risk tasks |
| **All Free Models** | Data may be used for training | Never use for confidential code |
| **North Mini Code** | Sovereign AI - local processing | Best for sensitive projects |
| **Nemotron 3 Ultra** | Zero-retention policy | Suitable for enterprise |

### Best Practices

1. **Review model selection** before executing sensitive operations
2. **Use local models** (North Mini Code) for confidential code
3. **Verify outputs** before deploying to production
4. **Check model availability** - free tiers are time-limited

---

## Troubleshooting

### Skill Not Loading

1. Verify `SKILL.md` filename is uppercase
2. Check frontmatter has `name` and `description`
3. Ensure skill path is in `opencode.json`
4. Restart OpenCode

### Model Not Selected

1. Verify task type matches model strength
2. Check model ID format: `opencode/model-id`
3. Ensure provider is configured
4. Check if model is available

### Performance Issues

1. Use DeepSeek V4 Flash for speed
2. Use Ling-3.0-flash for cost efficiency
3. Use Nemotron 3 Ultra for large contexts
4. Check network connectivity

---

## Version History

### v0.0.1 (2026-07-25)
- Initial release
- 7 verified model integration
- Smart routing system
- Comprehensive documentation
- Unit tests

---

## License

MIT License

## Links

- **Repository**: https://github.com/mrcbrbn5361/agentcode
- **OpenAgentSkill**: https://www.openagentskill.com/skills/agentcode
- **OpenCode Docs**: https://opencode.ai/docs
- **Issues**: https://github.com/mrcbrbn5361/agentcode/issues
