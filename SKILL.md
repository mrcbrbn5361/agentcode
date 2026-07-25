---
name: agentcode
description: "Smart routing across 6 verified free AI models for OpenCode. Auto-selects best model for coding tasks."
license: MIT
version: "0.0.1"
author: "AgentCode Contributors"
category: "coding-agent"
---

# AgentCode - Smart Multi-Model Coding Agent

## What It Does

AgentCode routes coding tasks to the best free AI model automatically.

## Models

| Model | Provider | Best For |
|-------|----------|----------|
| MiMo-V2.5 | Xiaomi | Multimodal |
| DeepSeek V4 Flash | DeepSeek | Speed |
| Laguna S 2.1 | NVIDIA | Terminal |
| Ling-3.0-flash | Alibaba | Efficiency |
| North Mini Code | NVIDIA | Local |
| Nemotron 3 Ultra | NVIDIA | Enterprise |

## Install

```bash
mkdir -p ~/.config/opencode/skills/agentcode
curl -fsSL https://raw.githubusercontent.com/mrcbrbn5361/agentcode/main/SKILL.md -o ~/.config/opencode/skills/agentcode/SKILL.md
```

## Usage

```python
from agentcode import route_task, ModelType

model = route_task("Create FastAPI endpoint")
print(model)  # ModelType.DEEPSEEK
```

## API

### `route_task(task_description, has_image=False, context_size=0, is_local_only=False) -> ModelType`

Routes a task to the optimal model.

### `get_model_info(model: ModelType) -> Dict`

Gets model information (name, provider, strength).

## Routing Rules

1. Image/Audio → MiMo-V2.5
2. Docker/Bash → Laguna S 2.1
3. Speed keywords → DeepSeek V4 Flash
4. Context >256K → Nemotron 3 Ultra
5. Local only → North Mini Code
6. Default → Ling-3.0-flash

## License

MIT
