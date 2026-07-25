# AgentCode - Smart Multi-Model Coding Agent

[![OpenAgentSkill](https://www.openagentskill.com/api/badge/agentcode)](https://www.openagentskill.com/skills/agentcode)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Version](https://img.shields.io/badge/version-0.0.1-green.svg)](https://github.com/mrcbrbn5361/agentcode)

## What is AgentCode?

AgentCode routes coding tasks to the best free AI model automatically. Uses 7 verified models from Xiaomi, DeepSeek, NVIDIA, and Alibaba.

## Verified Models

| Model | Provider | Link | Best For |
|-------|----------|------|----------|
| MiMo-V2.5 | Xiaomi | [HuggingFace](https://huggingface.co/Xiaomi-MiMo) | Multimodal |
| DeepSeek V4 Flash | DeepSeek | [API Docs](https://platform.deepseek.com/api-docs) | Speed (126 tok/s) |
| Laguna S 2.1 | NVIDIA | [NVIDIA Build](https://build.nvidia.com/nvidia/laguna-2-1) | Terminal |
| Ling-3.0-flash | Alibaba | [Alibaba Cloud](https://help.aliyun.com/zh/model-studio/getting-started/models) | Efficiency |
| North Mini Code | NVIDIA | [NVIDIA Build](https://build.nvidia.com/nvidia/north-mini-code) | Local |
| Nemotron 3 Ultra | NVIDIA | [NVIDIA Build](https://build.nvidia.com/nvidia/nemotron-3-ultra) | Enterprise |

## Install

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

1. Image/Audio/Video → MiMo-V2.5
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

## Tests

```bash
pytest test_agentcode.py -v
```

## Privacy

- Free models may use data for training
- Use North Mini Code for sensitive code
- Nemotron 3 Ultra has zero-retention policy

## License

MIT

## Links

- GitHub: https://github.com/mrcbrbn5361/agentcode
- Issues: https://github.com/mrcbrbn5361/agentcode/issues
