# AgentCode - Smart Multi-Model Coding Agent

## License

MIT License - Copyright (c) 2026 AgentCode Contributors. Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the Software), to deal in the Software without restriction.

## Installation

```bash
# Create skill directory
mkdir -p ~/.config/opencode/skills/agentcode

# Download SKILL.md
curl -fsSL https://raw.githubusercontent.com/mrcbrbn5361/agentcode/main/SKILL.md -o ~/.config/opencode/skills/agentcode/SKILL.md

# Restart OpenCode
opencode
```

## Quick Start

```python
from agentcode import route_task, ModelType

# Route a task
model = route_task("Create FastAPI endpoint")
print(model)  # ModelType.DEEPSEEK

# Get model info
from agentcode import get_model_info
info = get_model_info(ModelType.MIMO)
print(info["name"])  # "MiMo-V2.5 Free"
```

## Complete Python Implementation

```python
from enum import Enum
from typing import Dict, List

class ModelType(str, Enum):
    MIMO = "opencode/mimo-v2.5-free"
    DEEPSEEK = "opencode/deepseek-v4-flash-free"
    LAGUNA = "opencode/laguna-s-2.1-free"
    LING = "opencode/ling-3.0-flash-free"
    NORTH = "opencode/north-mini-code-free"
    NEMOTRON = "opencode/nemotron-3-ultra-free"

TERMINAL_KEYWORDS = ["bash", "shell", "docker", "terminal", "cli", "script", "deploy", "compose"]
SPEED_KEYWORDS = ["quick", "fast", "rapid", "batch", "multiple"]

def route_task(task_description: str, has_image: bool = False, context_size: int = 0, is_local_only: bool = False) -> ModelType:
    if has_image: return ModelType.MIMO
    if any(kw in task_description.lower() for kw in TERMINAL_KEYWORDS): return ModelType.LAGUNA
    if context_size > 256000: return ModelType.NEMOTRON
    if is_local_only: return ModelType.NORTH
    if any(kw in task_description.lower() for kw in SPEED_KEYWORDS): return ModelType.DEEPSEEK
    return ModelType.LING

def get_model_info(model: ModelType) -> Dict:
    models = {
        ModelType.MIMO: {"name": "MiMo-V2.5 Free", "provider": "Xiaomi", "strength": "Multimodal"},
        ModelType.DEEPSEEK: {"name": "DeepSeek V4 Flash Free", "provider": "DeepSeek", "strength": "Speed"},
        ModelType.LAGUNA: {"name": "Laguna S 2.1 Free", "provider": "NVIDIA", "strength": "Terminal"},
        ModelType.LING: {"name": "Ling-3.0-flash Free", "provider": "Alibaba", "strength": "Efficiency"},
        ModelType.NORTH: {"name": "North Mini Code Free", "provider": "NVIDIA", "strength": "Local"},
        ModelType.NEMOTRON: {"name": "Nemotron 3 Ultra Free", "provider": "NVIDIA", "strength": "Enterprise"},
    }
    return models.get(model, {})
```

## Complete Test Suite

```python
def test_multimodal_routing():
    assert route_task("Fix bug", has_image=True) == ModelType.MIMO

def test_terminal_routing():
    assert route_task("Create docker file") == ModelType.LAGUNA

def test_speed_routing():
    assert route_task("Quick code") == ModelType.DEEPSEEK

def test_context_routing():
    assert route_task("Analyze", context_size=500000) == ModelType.NEMOTRON

def test_local_routing():
    assert route_task("Run locally", is_local_only=True) == ModelType.NORTH

def test_default_routing():
    assert route_task("Write function") == ModelType.LING

def test_model_info():
    for model in ModelType:
        info = get_model_info(model)
        assert "name" in info
        assert "provider" in info

def run_all_tests():
    test_multimodal_routing()
    test_terminal_routing()
    test_speed_routing()
    test_context_routing()
    test_local_routing()
    test_default_routing()
    test_model_info()
    print("All 7 tests passed!")

run_all_tests()
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

## Usage Examples

```
User: "Create FastAPI endpoint"
→ DeepSeek V4 Flash (fastest)

User: "Fix UI bug [screenshot]"
→ MiMo-V2.5 (multimodal)

User: "Create docker compose"
→ Laguna S 2.1 (terminal expert)

User: "Analyze large codebase"
→ Nemotron 3 Ultra (1M context)

User: "Run locally"
→ North Mini Code (sovereign AI)
```

## API Reference

### route_task()

Route a coding task to the optimal AI model.

**Parameters:**
- `task_description` (str): Description of the coding task
- `has_image` (bool): Whether task includes image input
- `context_size` (int): Estimated context size in tokens
- `is_local_only` (bool): Whether task requires local processing

**Returns:**
- `ModelType`: The optimal model for this task

### get_model_info()

Get information about a model.

**Parameters:**
- `model` (ModelType): The model type

**Returns:**
- `Dict`: Model information (name, provider, strength)

## Links

- GitHub: https://github.com/mrcbrbn5361/agentcode
- OpenAgentSkill: https://www.openagentskill.com/skills/agentcode
- Issues: https://github.com/mrcbrbn5361/agentcode/issues
