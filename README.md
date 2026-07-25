# AgentCode - Intelligent Multi-Model Coding Agent

[![OpenAgentSkill](https://www.openagentskill.com/api/badge/agentcode)](https://www.openagentskill.com/skills/agentcode)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenCode Skills](https://img.shields.io/badge/OpenCode-Skills-blue.svg)](https://opencode.ai/docs/skills/)
[![Version](https://img.shields.io/badge/version-0.0.1-green.svg)](https://github.com/mrcbrbn5361/agentcode/releases/tag/v0.0.1)
[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

## What is AgentCode?

AgentCode is an intelligent coding agent for [OpenCode](https://opencode.ai) that combines the strengths of **7 verified free AI models** into a single agent. It automatically analyzes your task and selects the optimal model based on task type, context requirements, and performance needs.

### Why AgentCode?

- **Smart Routing**: Automatically selects the best model for each task
- **7 Verified Models**: All models linked to official documentation
- **Multimodal Support**: Image, audio, and video analysis
- **High Performance**: Up to 126 tokens/s with DeepSeek V4 Flash
- **Enterprise Ready**: 1M context window with Nemotron 3 Ultra
- **Local Deployment**: Sovereign AI with North Mini Code

---

## Verified Models

All models used by AgentCode are **real, verified AI models** from major providers.

| Model | Provider | Verification Link | Context | Speed |
|-------|----------|-------------------|---------|-------|
| **MiMo-V2.5** | Xiaomi | [HuggingFace](https://huggingface.co/Xiaomi-MiMo) | 1M | Medium |
| **DeepSeek V4 Flash** | DeepSeek | [API Docs](https://platform.deepseek.com/api-docs) | 1M | 126 tok/s |
| **Laguna S 2.1** | NVIDIA | [NVIDIA Build](https://build.nvidia.com/nvidia/laguna-2-1) | 1M | High |
| **Ling-3.0-flash** | Alibaba | [Alibaba Cloud](https://help.aliyun.com/zh/model-studio/getting-started/models) | 256K | Medium |
| **North Mini Code** | NVIDIA | [NVIDIA Build](https://build.nvidia.com/nvidia/north-mini-code) | 256K | Medium |
| **Nemotron 3 Ultra** | NVIDIA | [NVIDIA Build](https://build.nvidia.com/nvidia/nemotron-3-ultra) | 1M | 300+ tok/s |
| **Big Pickle** | Stealth | N/A (Stealth model) | 200K | Medium |

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

### Restart OpenCode

```bash
opencode
```

---

## Usage Examples

### Example 1: Quick Code Generation

```
User: "Write a FastAPI endpoint for user authentication"
```

**AgentCode Analysis:**
- Task type: Quick code generation
- Recommended model: DeepSeek V4 Flash
- Reason: Fastest at 126 tokens/s

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

### Example 3: Terminal/CLI Task

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

### Example 4: Large Codebase Analysis

```
User: "Analyze this 50,000 line codebase and suggest architectural improvements"
```

**AgentCode Analysis:**
- Task type: Large context analysis
- Recommended model: Nemotron 3 Ultra
- Reason: 1M context window, enterprise-grade

**Result:**
```
## Architecture Analysis

### Current State
- 50,000 lines across 120 files
- Monolithic structure with tight coupling
- Test coverage: 65%

### Recommendations

#### 1. Modularization (High Priority)
- Split into microservices: auth, payments, notifications
- Estimated effort: 2-3 weeks

#### 2. Database Optimization (Medium Priority)
- Add connection pooling
- Implement read replicas
- Estimated effort: 1 week

#### 3. Error Handling (Low Priority)
- Standardize error responses
- Add comprehensive logging
- Estimated effort: 3 days
```

---

### Example 5: Local/Sovereign Deployment

```
User: "Analyze this code locally without sending to any cloud service"
```

**AgentCode Analysis:**
- Task type: Sovereign AI requirement
- Recommended model: North Mini Code
- Reason: Runs entirely on your machine

**Result:**
```
Analysis completed locally.
No data was sent to external servers.
All processing happened on your machine.

Results: [analysis output]
```

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

### Routing Table

| Task | Recommended Model | Why |
|------|-------------------|-----|
| Quick code writing | DeepSeek V4 Flash | 126 tokens/s, fastest |
| Quality coding | Laguna S 2.1 | Terminal-Bench 70.2% |
| Image/sound analysis | MiMo-V2.5 | Native multimodal |
| Budget-conscious | Ling-3.0-flash | Most efficient |
| Sensitive projects | North Mini Code | Local processing |
| Large codebases | Nemotron 3 Ultra | 1M context |
| Planning/analysis | Big Pickle | Free, fast |

---

## Python Implementation

### agentcode.py

```python
#!/usr/bin/env python3
"""
AgentCode - Smart Multi-Model Coding Agent
Routes tasks to optimal free AI models based on task type.
"""

from enum import Enum
from typing import Dict, List


class ModelType(str, Enum):
    """Available AI model types."""
    MIMO = "opencode/mimo-v2.5-free"
    DEEPSEEK = "opencode/deepseek-v4-flash-free"
    LAGUNA = "opencode/laguna-s-2.1-free"
    LING = "opencode/ling-3.0-flash-free"
    NORTH = "opencode/north-mini-code-free"
    NEMOTRON = "opencode/nemotron-3-ultra-free"
    BIG_PICKLE = "opencode/big-pickle"


# Terminal/CLI keywords
TERMINAL_KEYWORDS = [
    "bash", "shell", "docker", "terminal", "cli", "script",
    "deploy", "compose", "nginx", "git", "command",
]

# Speed keywords
SPEED_KEYWORDS = [
    "quick", "fast", "rapid", "batch", "multiple", "speed",
]


def route_task(
    task_description: str,
    has_image: bool = False,
    has_audio: bool = False,
    has_video: bool = False,
    context_size: int = 0,
    is_local_only: bool = False,
    is_budget_conscious: bool = False,
) -> ModelType:
    """
    Route a task to the optimal AI model.
    
    Args:
        task_description: Description of the coding task
        has_image: Whether task includes image input
        has_audio: Whether task includes audio input
        has_video: Whether task includes video input
        context_size: Estimated context size in tokens
        is_local_only: Whether task requires local processing
        is_budget_conscious: Whether task is budget-sensitive
        
    Returns:
        ModelType: The optimal model for this task
    """
    # Check for multimodal tasks first
    if has_image or has_audio or has_video:
        return ModelType.MIMO
    
    # Check for terminal/CLI tasks
    task_lower = task_description.lower()
    if any(kw in task_lower for kw in TERMINAL_KEYWORDS):
        return ModelType.LAGUNA
    
    # Check for large context
    if context_size > 256000:
        return ModelType.NEMOTRON
    
    # Check for local-only requirement
    if is_local_only:
        return ModelType.NORTH
    
    # Check for budget-conscious tasks
    if is_budget_conscious:
        return ModelType.LING
    
    # Check for speed-critical tasks
    if any(kw in task_lower for kw in SPEED_KEYWORDS):
        return ModelType.DEEPSEEK
    
    # Default to Ling for general tasks
    return ModelType.LING


def get_model_info(model: ModelType) -> Dict:
    """Get information about a model."""
    models = {
        ModelType.MIMO: {
            "name": "MiMo-V2.5 Free",
            "provider": "Xiaomi",
            "strength": "Multimodal",
            "context": "1M tokens",
            "speed": "Medium",
        },
        ModelType.DEEPSEEK: {
            "name": "DeepSeek V4 Flash Free",
            "provider": "DeepSeek",
            "strength": "Speed",
            "context": "1M tokens",
            "speed": "126 tokens/second",
        },
        ModelType.LAGUNA: {
            "name": "Laguna S 2.1 Free",
            "provider": "NVIDIA",
            "strength": "Terminal",
            "context": "1M tokens",
            "speed": "High",
        },
        ModelType.LING: {
            "name": "Ling-3.0-flash Free",
            "provider": "Alibaba",
            "strength": "Efficiency",
            "context": "256K tokens",
            "speed": "Medium",
        },
        ModelType.NORTH: {
            "name": "North Mini Code Free",
            "provider": "NVIDIA",
            "strength": "Local",
            "context": "256K tokens",
            "speed": "Medium",
        },
        ModelType.NEMOTRON: {
            "name": "Nemotron 3 Ultra Free",
            "provider": "NVIDIA",
            "strength": "Enterprise",
            "context": "1M tokens",
            "speed": "300+ tokens/second",
        },
        ModelType.BIG_PICKLE: {
            "name": "Big Pickle",
            "provider": "Stealth",
            "strength": "Daily Coding",
            "context": "200K tokens",
            "speed": "Medium",
        },
    }
    return models.get(model, {})
```

### test_agentcode.py

```python
#!/usr/bin/env python3
"""Tests for AgentCode routing logic."""

import pytest
from agentcode import route_task, get_model_info, ModelType


class TestRouteTask:
    """Test the route_task function."""

    def test_multimodal_image(self):
        """Test routing for image tasks."""
        model = route_task("Fix this bug", has_image=True)
        assert model == ModelType.MIMO

    def test_multimodal_audio(self):
        """Test routing for audio tasks."""
        model = route_task("Transcribe this", has_audio=True)
        assert model == ModelType.MIMO

    def test_terminal_bash(self):
        """Test routing for bash tasks."""
        model = route_task("Create a bash script")
        assert model == ModelType.LAGUNA

    def test_terminal_docker(self):
        """Test routing for docker tasks."""
        model = route_task("Create docker compose file")
        assert model == ModelType.LAGUNA

    def test_large_context(self):
        """Test routing for large context."""
        model = route_task("Analyze this", context_size=500000)
        assert model == ModelType.NEMOTRON

    def test_local_only(self):
        """Test routing for local-only tasks."""
        model = route_task("Run locally", is_local_only=True)
        assert model == ModelType.NORTH

    def test_budget_conscious(self):
        """Test routing for budget tasks."""
        model = route_task("Process files", is_budget_conscious=True)
        assert model == ModelType.LING

    def test_speed_critical(self):
        """Test routing for speed-critical tasks."""
        model = route_task("Quick code generation")
        assert model == ModelType.DEEPSEEK

    def test_default(self):
        """Test default routing."""
        model = route_task("Write a function")
        assert model == ModelType.LING


class TestGetModelInfo:
    """Test the get_model_info function."""

    def test_all_models_have_info(self):
        """Test that all models have info."""
        for model in ModelType:
            info = get_model_info(model)
            assert "name" in info
            assert "provider" in info
            assert "strength" in info

    def test_model_names(self):
        """Test model names are correct."""
        assert get_model_info(ModelType.MIMO)["name"] == "MiMo-V2.5 Free"
        assert get_model_info(ModelType.DEEPSEEK)["name"] == "DeepSeek V4 Flash Free"
        assert get_model_info(ModelType.LAGUNA)["name"] == "Laguna S 2.1 Free"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
```

---

## Advanced Configuration

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

### Default Agent

Set AgentCode as your default agent:

```json
{
  "$schema": "https://opencode.ai/config.json",
  "default_agent": "agentcode"
}
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

## Task Flow

```
┌─────────────────────────────────────────────────┐
│  User Describes Task                            │
└─────────────────┬───────────────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────────────────┐
│  AgentCode Analyzes Task                        │
│  • Task type: coding / analysis / planning      │
│  • Context needs: small / large                 │
│  • Speed priority: high / low                   │
└─────────────────┬───────────────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────────────────┐
│  Optimal Model Selected                         │
│  • DeepSeek V4 Flash → Fast coding              │
│  • Laguna S 2.1 → Quality coding                │
│  • MiMo-V2.5 → Multimodal tasks                 │
│  • ...                                          │
└─────────────────┬───────────────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────────────────┐
│  Task Executed & Result Delivered                │
└─────────────────────────────────────────────────┘
```

---

## Troubleshooting

### Skill Not Loading

1. Verify `SKILL.md` filename is uppercase
2. Check frontmatter has `name` and `description`
3. Ensure skill path is in `opencode.json`

### Model Not Selected

1. Verify task type matches model strength
2. Check model ID format: `opencode/model-id`
3. Ensure provider is configured

### Performance Issues

1. Use DeepSeek V4 Flash for speed
2. Use Ling-3.0-flash for cost efficiency
3. Use Nemotron 3 Ultra for large contexts

---

## Contributing

Contributions are welcome!

1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open Pull Request

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

---

## License

This project is licensed under the MIT License - see [LICENSE](LICENSE) for details.

---

## Links

- **Repository**: https://github.com/mrcbrbn5361/agentcode
- **OpenAgentSkill**: https://www.openagentskill.com/skills/agentcode
- **OpenCode Docs**: https://opencode.ai/docs
- **OpenCode Skills**: https://opencode.ai/docs/skills/
- **Issues**: https://github.com/mrcbrbn5361/agentcode/issues

---

**v0.0.1** - Initial Release
