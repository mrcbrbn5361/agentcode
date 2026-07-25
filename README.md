# AgentCode

Smart routing across 6 verified free AI models. MIT License.

## Install

```bash
mkdir -p ~/.config/opencode/skills/agentcode
curl -fsSL https://raw.githubusercontent.com/mrcbrbn5361/agentcode/main/SKILL.md -o ~/.config/opencode/skills/agentcode/SKILL.md
```

## Complete Code

```python
from enum import Enum
from typing import Dict

class ModelType(str, Enum):
    MIMO = "opencode/mimo-v2.5-free"
    DEEPSEEK = "opencode/deepseek-v4-flash-free"
    LAGUNA = "opencode/laguna-s-2.1-free"
    LING = "opencode/ling-3.0-flash-free"
    NORTH = "opencode/north-mini-code-free"
    NEMOTRON = "opencode/nemotron-3-ultra-free"

TERMINAL = ["bash", "shell", "docker", "terminal", "cli", "script", "deploy"]
SPEED = ["quick", "fast", "rapid", "batch"]

def route_task(desc: str, img: bool = False, ctx: int = 0, local: bool = False) -> ModelType:
    if img: return ModelType.MIMO
    if any(k in desc.lower() for k in TERMINAL): return ModelType.LAGUNA
    if ctx > 256000: return ModelType.NEMOTRON
    if local: return ModelType.NORTH
    if any(k in desc.lower() for k in SPEED): return ModelType.DEEPSEEK
    return ModelType.LING

def get_model_info(m: ModelType) -> Dict:
    d = {
        ModelType.MIMO: {"name": "MiMo-V2.5", "provider": "Xiaomi"},
        ModelType.DEEPSEEK: {"name": "DeepSeek V4 Flash", "provider": "DeepSeek"},
        ModelType.LAGUNA: {"name": "Laguna S 2.1", "provider": "NVIDIA"},
        ModelType.LING: {"name": "Ling-3.0-flash", "provider": "Alibaba"},
        ModelType.NORTH: {"name": "North Mini Code", "provider": "NVIDIA"},
        ModelType.NEMOTRON: {"name": "Nemotron 3 Ultra", "provider": "NVIDIA"},
    }
    return d.get(m, {})

# Tests
assert route_task("Fix bug", img=True) == ModelType.MIMO
assert route_task("Create docker") == ModelType.LAGUNA
assert route_task("Quick code") == ModelType.DEEPSEEK
assert route_task("Analyze", ctx=500000) == ModelType.NEMOTRON
assert route_task("Run locally", local=True) == ModelType.NORTH
assert route_task("Write func") == ModelType.LING
for m in ModelType: assert "name" in get_model_info(m)
print("All tests passed!")
```

## Models

| Model | Provider | Best For |
|-------|----------|----------|
| MiMo-V2.5 | Xiaomi | Multimodal |
| DeepSeek V4 Flash | DeepSeek | Speed |
| Laguna S 2.1 | NVIDIA | Terminal |
| Ling-3.0-flash | Alibaba | Efficiency |
| North Mini Code | NVIDIA | Local |
| Nemotron 3 Ultra | NVIDIA | Enterprise |

## Usage

```
"Create FastAPI endpoint" → DeepSeek V4 Flash
"Fix UI bug [screenshot]" → MiMo-V2.5
"Create docker compose" → Laguna S 2.1
```

## Links

- GitHub: https://github.com/mrcbrbn5361/agentcode
- OpenAgentSkill: https://www.openagentskill.com/skills/agentcode
