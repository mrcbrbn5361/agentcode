---
name: agentcode
description: "Intelligent coding agent combining 7 free AI models with smart routing. Auto-selects best model based on task type. Supports multimodal, fast coding, terminal tasks, and more. Trigger: code, refactor, debug, analyze, plan, edit file, write test, create project."
license: MIT
compatibility: opencode
metadata:
  version: "0.0.1"
  author: "AgentCode Contributors"
  models: "7"
  category: "coding-agent"
---

# AgentCode - Intelligent Multi-Model Coding Agent

## Overview

AgentCode is a smart routing system that combines **7 free AI models** into a single, intelligent coding agent. It analyzes your task and automatically selects the optimal model based on task type, context requirements, and performance needs.

### Key Features

- **Automatic Model Selection**: Routes tasks to the best model
- **7 Free Models**: No API costs during free tier
- **Multimodal Support**: Image, audio, video analysis
- **High-Speed Coding**: Up to 126 tokens/s
- **Enterprise Ready**: 1M context window
- **Local Deployment**: Sovereign AI support

---

## When to Use AgentCode

Use AgentCode when you need to:

- Write, edit, or refactor code
- Analyze images or screenshots
- Run terminal commands
- Create project structures
- Debug and fix errors
- Plan architecture
- Process large codebases

---

## Model Selection Guide

### 1. MiMo-V2.5 Free

**Model ID:** `opencode/mimo-v2.5-free`

**Best for:** Multimodal tasks, image/sound/video analysis

**When to use:**
- User provides screenshot of error
- Audio file needs transcription
- Video content analysis
- Long-term agent tasks requiring multiple tool calls

**Example:**
```
User: "What's wrong with this UI? [attaches screenshot]"
AgentCode: Uses MiMo-V2.5 to analyze the image and identify issues
```

**Capabilities:**
- Native image understanding
- Audio processing
- Video analysis
- 1M context window
- Multimodal reasoning

---

### 2. DeepSeek V4 Flash Free

**Model ID:** `opencode/deepseek-v4-flash-free`

**Best for:** High-speed code generation, high-volume tasks

**When to use:**
- Quick code writing
- Multiple file edits
- Repetitive tasks
- Rapid prototyping
- Batch processing

**Example:**
```
User: "Write 10 API endpoints for a REST API"
AgentCode: Uses DeepSeek V4 Flash (126 tokens/s) for fast generation
```

**Capabilities:**
- 126 tokens/s generation speed
- 1M context window
- Code generation
- Refactoring
- Bug fixing

---

### 3. Laguna S 2.1 Free

**Model ID:** `opencode/laguna-s-2.1-free`

**Best for:** Terminal/CLI tasks, agentic coding

**When to use:**
- Terminal commands
- CLI tool creation
- SWE-bench tasks
- Agent workflows
- Docker/script creation

**Example:**
```
User: "Create a bash script to automate deployment"
AgentCode: Uses Laguna S 2.1 (Terminal-Bench 70.2%) for terminal expertise
```

**Capabilities:**
- Terminal-Bench 70.2% (highest for open-weight)
- CLI command generation
- Script writing
- Docker configuration
- Agent workflows

---

### 4. Ling-3.0-flash Free

**Model ID:** `opencode/ling-3.0-flash-free`

**Best for:** Token efficiency, low-cost inference

**When to use:**
- Budget-conscious tasks
- High-volume API calls
- Cost optimization
- Simple code tasks

**Example:**
```
User: "Process 1000 files and extract data"
AgentCode: Uses Ling-3.0-flash (most efficient) for cost optimization
```

**Capabilities:**
- 5.1B active parameters (most efficient)
- 256K context window
- Token-efficient inference
- Cost-effective processing

---

### 5. North Mini Code Free

**Model ID:** `opencode/north-mini-code-free`

**Best for:** Local deployment, sovereign AI

**When to use:**
- Sensitive projects
- Local-only processing
- Offline requirements
- Compliance needs

**Example:**
```
User: "Run this analysis locally without cloud"
AgentCode: Uses North Mini Code (runs on single H100)
```

**Capabilities:**
- Runs on single H100
- Apache 2.0 license
- Local processing
- 256K context window
- Sovereign AI

---

### 6. Nemotron 3 Ultra Free

**Model ID:** `opencode/nemotron-3-ultra-free`

**Best for:** Enterprise, long-context tasks

**When to use:**
- Large codebase analysis
- Long-horizon workflows
- Enterprise projects
- Complex reasoning

**Example:**
```
User: "Analyze this 100K line codebase and suggest improvements"
AgentCode: Uses Nemotron 3 Ultra (1M context) for comprehensive analysis
```

**Capabilities:**
- 550B total parameters
- 1M context window
- Enterprise-grade
- 300+ tokens/s
- Long-horizon tasks

---

### 7. Big Pickle

**Model ID:** `opencode/big-pickle`

**Best for:** Daily coding, quick planning

**When to use:**
- Quick start tasks
- Planning and analysis
- Low-risk operations
- Initial exploration

**Example:**
```
User: "Plan this feature implementation"
AgentCode: Uses Big Pickle (free, fast) for planning
```

**Capabilities:**
- Free tier
- 200K context window
- Quick response
- Planning support

---

## Smart Routing Logic

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

## Configuration

### Basic Setup

Add to `opencode.json`:

```json
{
  "$schema": "https://opencode.ai/config.json",
  "skills": {
    "paths": ["~/.config/opencode/skills"]
  }
}
```

### Set as Default Agent

```json
{
  "$schema": "https://opencode.ai/config.json",
  "default_agent": "agentcode"
}
```

### Custom Model Preference

```json
{
  "agent": {
    "agentcode": {
      "model": "opencode/deepseek-v4-flash-free"
    }
  }
}
```

### Permission Settings

```json
{
  "permission": {
    "skill": {
      "agentcode": "allow"
    }
  }
}
```

---

## Privacy & Security

### Important Warnings

1. **Big Pickle** is a stealth model - never use for confidential code
2. **Free models** may use data for training
3. **North Mini Code** is best for sensitive projects
4. **Always** verify model selection before execution

### Data Handling by Model

| Model | Data Policy | Recommendation |
|-------|-------------|----------------|
| MiMo-V2.5 | May use data for training | Avoid confidential data |
| DeepSeek V4 Flash | May use data for training | Avoid confidential data |
| Laguna S 2.1 | May use data for training | Avoid confidential data |
| Ling-3.0-flash | May use data for training | Avoid confidential data |
| North Mini Code | Data stays on device | Safe for sensitive data |
| Nemotron 3 Ultra | Zero-retention policy | Safe for enterprise |
| Big Pickle | Stealth model, unknown | Low-risk tasks only |

### Best Practices

1. **Review model selection** before processing sensitive data
2. **Use local models** for confidential code
3. **Verify outputs** before deployment
4. **Check model availability** - free tiers are time-limited

---

## Troubleshooting

### Skill Not Loading

1. Check `SKILL.md` filename is uppercase
2. Verify frontmatter has `name` and `description`
3. Check permissions in `opencode.json`
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

## Examples

### Example 1: Code Generation

**Input:**
```
Create a Python FastAPI endpoint for user registration
```

**Analysis:**
- Task type: Quick code generation
- Recommended model: DeepSeek V4 Flash
- Reason: Fastest at 126 tokens/s

**Output:**
```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session

app = FastAPI()

class UserRegistration(BaseModel):
    email: str
    password: str
    name: str

@app.post("/users/register")
async def register_user(user: UserRegistration, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    new_user = User(email=user.email, name=user.name)
    new_user.set_password(user.password)
    db.add(new_user)
    db.commit()
    
    return {"message": "User registered successfully", "user_id": new_user.id}
```

---

### Example 2: Image Analysis

**Input:**
```
Fix this UI bug from the screenshot [attaches image]
```

**Analysis:**
- Task type: Multimodal (image analysis)
- Recommended model: MiMo-V2.5
- Reason: Native image understanding

**Output:**
```
I can see the issue in your UI:
1. The button is overlapping with the text label
2. The padding is too small (currently 8px)
3. The color contrast doesn't meet WCAG standards

Here's the fix:
```css
.button {
  padding: 16px 24px;
  margin-top: 8px;
  background-color: #007bff;
  color: white;
}
```

---

### Example 3: Terminal Task

**Input:**
```
Create a Docker compose file for a Node.js app with PostgreSQL and Redis
```

**Analysis:**
- Task type: Terminal/CLI task
- Recommended model: Laguna S 2.1
- Reason: Terminal-Bench 70.2%

**Output:**
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

## Version History

### v0.0.1 (2026-07-25)
- Initial release
- 7 model integration
- Smart routing system
- Basic documentation

---

## License

MIT License

## Support

- **GitHub**: https://github.com/mrcbrbn5361/agentcode
- **Issues**: https://github.com/mrcbrbn5361/agentcode/issues
- **OpenAgentSkill**: https://www.openagentskill.com/skills/agentcode
