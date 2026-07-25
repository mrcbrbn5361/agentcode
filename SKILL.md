---
name: agentcode
description: "Intelligent coding agent with smart routing across 7 verified free AI models. Auto-selects best model for task type."
license: MIT
version: "0.0.1"
author: "AgentCode Contributors"
category: "coding-agent"
---

# AgentCode - Smart Multi-Model Coding Agent

## Overview

AgentCode routes coding tasks to the best free AI model automatically. Uses 7 verified models from Xiaomi, DeepSeek, NVIDIA, and Alibaba.

## Verified Models

| Model | Provider | Best For | Context |
|-------|----------|----------|---------|
| MiMo-V2.5 | Xiaomi | Multimodal | 1M |
| DeepSeek V4 Flash | DeepSeek | Speed (126 tok/s) | 1M |
| Laguna S 2.1 | NVIDIA | Terminal | 1M |
| Ling-3.0-flash | Alibaba | Efficiency | 256K |
| North Mini Code | NVIDIA | Local | 256K |
| Nemotron 3 Ultra | NVIDIA | Enterprise | 1M |
| Big Pickle | Stealth | Daily Coding | 200K |

## Installation

```bash
mkdir -p ~/.config/opencode/skills/agentcode
curl -fsSL https://raw.githubusercontent.com/mrcbrbn5361/agentcode/main/SKILL.md -o ~/.config/opencode/skills/agentcode/SKILL.md
```

## Usage

```
User: "Create FastAPI endpoint"
→ DeepSeek V4 Flash (fastest)

User: "Fix UI bug [screenshot]"
→ MiMo-V2.5 (multimodal)

User: "Create docker compose"
→ Laguna S 2.1 (terminal expert)
```

## Routing Logic

1. Multimodal (image/audio/video) → MiMo-V2.5
2. Terminal/Docker → Laguna S 2.1
3. Speed critical → DeepSeek V4 Flash
4. Large context (>256K) → Nemotron 3 Ultra
5. Local only → North Mini Code
6. Default → Ling-3.0-flash

## Python Code

```python
from agentcode import route_task, ModelType

# Route to best model
model = route_task("Create FastAPI endpoint")
print(model)  # ModelType.DEEPSEEK

# Get model info
from agentcode import get_model_info
info = get_model_info(ModelType.MIMO)
print(info["name"])  # "MiMo-V2.5 Free"
```

## Privacy

- Free models may use data for training
- Use North Mini Code for sensitive code
- Nemotron 3 Ultra has zero-retention policy

## License

MIT
