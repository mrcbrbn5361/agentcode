# AgentCode

Smart coding agent that routes tasks to the best free AI model.

## License

MIT License - Copyright (c) 2026 AgentCode Contributors

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

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
    """Available AI model types."""
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
    """
    Route a task to the optimal AI model.
    
    Args:
        task_description: Description of the coding task
        has_image: Whether task includes image input
        context_size: Estimated context size in tokens
        is_local_only: Whether task requires local processing
        
    Returns:
        ModelType: The optimal model for this task
    """
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
# Test routing logic
def test_route_task():
    """Test route_task function."""
    assert route_task("Fix bug", has_image=True) == ModelType.MIMO
    assert route_task("Create docker file") == ModelType.LAGUNA
    assert route_task("Quick code") == ModelType.DEEPSEEK
    assert route_task("Analyze", context_size=500000) == ModelType.NEMOTRON
    assert route_task("Run locally", is_local_only=True) == ModelType.NORTH
    assert route_task("Write function") == ModelType.LING
    print("All tests passed!")

test_route_task()
```

## Links

- GitHub: https://github.com/mrcbrbn5361/agentcode
- Issues: https://github.com/mrcbrbn5361/agentcode/issues
