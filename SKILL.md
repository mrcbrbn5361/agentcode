---
name: agentcode
description: "Smart routing across 6 verified free AI models. Auto-selects best model for coding tasks."
license: MIT
version: "0.0.1"
---

# AgentCode

Routes coding tasks to the best free AI model automatically.

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

## Routing

1. Multimodal → MiMo-V2.5
2. Terminal → Laguna S 2.1
3. Speed → DeepSeek V4 Flash
4. Large context → Nemotron 3 Ultra
5. Local → North Mini Code
6. Default → Ling-3.0-flash

## License

MIT
