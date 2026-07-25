---
name: agentcode
description: "Intelligent coding agent with smart routing across 7 free AI models. Auto-selects best model for task type."
license: MIT
version: "0.0.1"
author: "AgentCode Contributors"
category: "coding-agent"
---

# AgentCode - Smart Multi-Model Coding Agent

## What It Does

AgentCode routes your coding task to the best free AI model automatically.

**7 Free Models:**
- MiMo-V2.5 - Multimodal (image/audio/video)
- DeepSeek V4 Flash - Fastest (126 tok/s)
- Laguna S 2.1 - Terminal expert (Terminal-Bench 70.2%)
- Ling-3.0-flash - Most efficient
- North Mini Code - Local/sovereign AI
- Nemotron 3 Ultra - Enterprise (1M context)
- Big Pickle - Free daily coding

## Quick Start

### Install

```bash
mkdir -p ~/.config/opencode/skills/agentcode
curl -fsSL https://raw.githubusercontent.com/mrcbrbn5361/agentcode/main/SKILL.md -o ~/.config/opencode/skills/agentcode/SKILL.md
```

### Configure

Add to `opencode.json`:
```json
{
  "skills": { "paths": ["~/.config/opencode/skills"] }
}
```

## Usage Examples

### Code Generation
```
User: "Create a Python FastAPI endpoint"
Model: DeepSeek V4 Flash (fastest)
Output: FastAPI code with async endpoint
```

### Image Analysis
```
User: "Fix this UI bug [screenshot]"
Model: MiMo-V2.5 (multimodal)
Output: Bug analysis with CSS fix
```

### Terminal Tasks
```
User: "Create Docker compose file"
Model: Laguna S 2.1 (terminal expert)
Output: docker-compose.yml with services
```

## Routing Logic

1. **Multimodal task?** → MiMo-V2.5
2. **Terminal task?** → Laguna S 2.1
3. **Speed critical?** → DeepSeek V4 Flash
4. **Large context (>256K)?** → Nemotron 3 Ultra
5. **Local only?** → North Mini Code
6. **Budget concern?** → Ling-3.0-flash
7. **Default** → Big Pickle

## Privacy Warning

- Free models may use data for training
- Use North Mini Code for sensitive code
- Big Pickle is stealth model - low-risk only

## License

MIT

## Links

- GitHub: https://github.com/mrcbrbn5361/agentcode
- Issues: https://github.com/mrcbrbn5361/agentcode/issues
