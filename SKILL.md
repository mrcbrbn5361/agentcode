---
name: agentcode
description: "Smart routing across 7 verified free AI models with system detection and multi-language support for OpenCode."
license: MIT
version: "0.0.2"
author: "AgentCode Contributors"
category: "coding-agent"
---

# AgentCode - Smart Multi-Model Coding Agent

## What It Does

AgentCode routes coding tasks to the best free AI model automatically, with system detection and multi-language support.

## Features

### v0.0.2 New Features
- **System Model Detection**: Detect AI models available on your system
- **Interactive Setup Wizard**: Choose models based on detected capabilities
- **Session Management**: Persistent sessions with context preservation
- **Multi-Language Support**: 14+ programming languages with templates
- **OpenClaw-Inspired Features**: Dynamic model switching and progress tracking

### Core Features
- Smart task routing to optimal AI models
- 7 verified free models with official sources
- MIT licensed, production-ready

## Models

| Model | Provider | Best For | Context |
|-------|----------|----------|---------|
| MiMo-V2.5 | Xiaomi | Multimodal | 1M |
| DeepSeek V4 Flash | DeepSeek | Speed (126 tok/s) | 1M |
| Laguna S 2.1 | NVIDIA | Terminal | 1M |
| Ling-3.0-flash | Alibaba | Efficiency | 256K |
| North Mini Code | NVIDIA | Local | 256K |
| Nemotron 3 Ultra | NVIDIA | Enterprise | 1M |

## Install

```bash
mkdir -p ~/.config/opencode/skills/agentcode
curl -fsSL https://raw.githubusercontent.com/mrcbrbn5361/agentcode/main/SKILL.md -o ~/.config/opencode/skills/agentcode/SKILL.md
```

## Quick Start

```python
from agentcode import route_task, ModelType

# Basic routing
model = route_task("Create FastAPI endpoint")
print(model)  # ModelType.DEEPSEEK

# System detection
from detector import detect_system_models
models = detect_system_models()

# Interactive setup
from wizard import run_setup_wizard
preferences = run_setup_wizard()
```

## API

### `route_task(task_description, has_image=False, context_size=0, is_local_only=False) -> ModelType`

Routes a task to the optimal model.

### `get_model_info(model: ModelType) -> Dict`

Gets model information (name, provider, strength).

### `detect_system_models() -> List[DetectedModel]`

Detects AI models available on the user's system.

### `run_setup_wizard() -> UserPreferences`

Runs interactive setup wizard for model selection.

### `get_session_manager() -> SessionManager`

Gets session manager for persistent coding sessions.

### `detect_project_language(project_path) -> ProgrammingLanguage`

Detects primary language of a project.

## System Detection

AgentCode automatically detects:

- **CLI Tools**: OpenAI, Anthropic, Ollama, llama.cpp, vLLM, LM Studio
- **IDE Extensions**: VS Code Copilot, Cursor, Windsurf, JetBrains AI
- **Cloud APIs**: OpenAI, Anthropic, Google, DeepSeek, Mistral, Groq
- **Local Models**: Ollama models, LM Studio models

## Multi-Language Support

| Language | Expert Model | Linters | Formatters |
|----------|--------------|---------|------------|
| Python | MiMo-V2.5 | flake8, pylint, mypy | black, autopep8 |
| JavaScript | MiMo-V2.5 | eslint, jshint | prettier |
| TypeScript | MiMo-V2.5 | tsc, eslint | prettier |
| Go | Laguna S 2.1 | golangci-lint | gofmt |
| Rust | Laguna S 2.1 | clippy | rustfmt |
| Java | Nemotron 3 Ultra | checkstyle, spotbugs | google-java-format |
| C# | Nemotron 3 Ultra | dotnet format | dotnet format |
| C++ | Laguna S 2.1 | cppcheck, clang-tidy | clang-format |
| PHP | Ling-3.0-flash | phpcs, phpstan | php-cs-fixer |
| Ruby | Ling-3.0-flash | rubocop | rubocop |
| Swift | MiMo-V2.5 | swiftlint | swiftformat |
| Kotlin | MiMo-V2.5 | ktlint, detekt | ktlint |
| Scala | Nemotron 3 Ultra | scalastyle | scalafmt |
| Shell | Laguna S 2.1 | shellcheck | shfmt |

## Routing Rules

1. Image/Audio → MiMo-V2.5
2. Docker/Bash → Laguna S 2.1
3. Speed keywords → DeepSeek V4 Flash
4. Context >256K → Nemotron 3 Ultra
5. Local only → North Mini Code
6. Default → Ling-3.0-flash

## Session Management

```python
from sessions import get_session_manager, get_model_switcher

# Create session
manager = get_session_manager()
session = manager.create_session("mimo", "Create API", "python")

# Switch models
switcher = get_model_switcher()
switcher.switch_model("deepseek")

# Get statistics
stats = manager.get_session_stats()
```

## Configuration

Configuration saved to `~/.agentcode/config.json`:

```json
{
  "version": "0.0.2",
  "selected_models": {
    "primary": "mimo",
    "fallback": ["deepseek", "laguna"],
    "terminal": "laguna",
    "multimodal": "mimo",
    "local": "north"
  },
  "user_preferences": {
    "priority": "speed",
    "privacy_mode": false,
    "auto_fallback": true
  }
}
```

## License

MIT