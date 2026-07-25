# AgentCode

Smart coding agent that routes tasks to the best free AI model.

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

```
User: "Create FastAPI endpoint"
→ DeepSeek V4 Flash

User: "Fix UI bug [screenshot]"
→ MiMo-V2.5

User: "Create docker compose"
→ Laguna S 2.1
```

## Python Code

```python
from enum import Enum

class ModelType(str, Enum):
    MIMO = "opencode/mimo-v2.5-free"
    DEEPSEEK = "opencode/deepseek-v4-flash-free"
    LAGUNA = "opencode/laguna-s-2.1-free"
    LING = "opencode/ling-3.0-flash-free"
    NORTH = "opencode/north-mini-code-free"
    NEMOTRON = "opencode/nemotron-3-ultra-free"

TERMINAL_KEYWORDS = ["bash", "shell", "docker", "terminal", "cli", "script"]
SPEED_KEYWORDS = ["quick", "fast", "rapid", "batch"]

def route_task(task_description: str, has_image: bool = False, 
               context_size: int = 0, is_local_only: bool = False) -> ModelType:
    if has_image:
        return ModelType.MIMO
    if any(kw in task_description.lower() for kw in TERMINAL_KEYWORDS):
        return ModelType.LAGUNA
    if context_size > 256000:
        return ModelType.NEMOTRON
    if is_local_only:
        return ModelType.NORTH
    if any(kw in task_description.lower() for kw in SPEED_KEYWORDS):
        return ModelType.DEEPSEEK
    return ModelType.LING
```

## Tests

```python
def test_route_task():
    assert route_task("Fix bug", has_image=True) == ModelType.MIMO
    assert route_task("Create docker file") == ModelType.LAGUNA
    assert route_task("Quick code") == ModelType.DEEPSEEK
    assert route_task("Write function") == ModelType.LING

test_route_task()
print("All tests passed!")
```

## License

MIT
