# AgentCode - Smart Multi-Model Coding Agent

[![Listed on OpenAgentSkill](https://www.openagentskill.com/api/badge/mrcbrbn5361-agentcode?metric=listed&label=Listed)](https://www.openagentskill.com/skills/mrcbrbn5361-agentcode)
[![OpenAgentSkill Trust](https://www.openagentskill.com/api/badge/mrcbrbn5361-agentcode?metric=trust&label=Trust)](https://www.openagentskill.com/skills/mrcbrbn5361-agentcode)
[![OpenAgentSkill Audit](https://www.openagentskill.com/api/badge/mrcbrbn5361-agentcode?metric=audit&label=Audit)](https://www.openagentskill.com/skills/mrcbrbn5361-agentcode/audit)
[![Agent Proven](https://www.openagentskill.com/api/badge/mrcbrbn5361-agentcode?metric=proven&label=Agent%20Proven)](https://www.openagentskill.com/skills/mrcbrbn5361-agentcode)

Intelligent routing across 7 verified free AI models with system detection and multi-language support. MIT License.

## What's New in v0.0.2

- **System Model Detection**: Automatically detect AI models available on your system
- **Interactive Setup Wizard**: Choose models based on your needs and detected capabilities
- **Session Management**: Persistent sessions with context preservation
- **Multi-Language Support**: 14+ programming languages with templates
- **OpenClaw-Inspired Features**: Dynamic model switching and progress tracking

## Installation

```bash
# Create skill directory
mkdir -p ~/.config/opencode/skills/agentcode

# Download SKILL.md
curl -fsSL https://raw.githubusercontent.com/mrcbrbn5361/agentcode/main/SKILL.md \
  -o ~/.config/opencode/skills/agentcode/SKILL.md

# Restart OpenCode
opencode
```

## Quick Start

```python
from agentcode import route_task, get_model_info, ModelType

# Route a task to the best model
model = route_task("Create FastAPI endpoint")
print(model)  # ModelType.DEEPSEEK

# Get model information
info = get_model_info(ModelType.MIMO)
print(info["name"])  # "MiMo-V2.5"
```

## System Detection

AgentCode automatically detects AI models available on your system:

```python
from detector import detect_system_models, print_detection_report

# Detect all available models
models = detect_system_models()

# Print detection report
print_detection_report(models)
```

### Detected Systems

| Category | Examples |
|----------|----------|
| CLI Tools | OpenAI CLI, Anthropic CLI, Ollama, llama.cpp |
| IDE Extensions | VS Code Copilot, Cursor, Windsurf, JetBrains AI |
| Cloud APIs | OpenAI, Anthropic, Google, DeepSeek, Mistral |
| Local Models | Ollama models, LM Studio, quantized models |

## Interactive Setup

Run the setup wizard to configure AgentCode:

```python
from wizard import run_setup_wizard

# Run interactive setup
preferences = run_setup_wizard()
```

### Setup Wizard Features

1. **System Scanning**: Detects all AI models on your system
2. **Priority Selection**: Choose speed, accuracy, privacy, cost, or coding focus
3. **Model Selection**: Pick primary, fallback, terminal, and multimodal models
4. **Configuration**: Saves preferences to `~/.agentcode/config.json`

## Session Management

Manage coding sessions with context preservation:

```python
from sessions import get_session_manager, get_model_switcher

# Create a new session
manager = get_session_manager()
session = manager.create_session("mimo", "Create REST API", "python")

# Switch models during session
switcher = get_model_switcher()
switcher.switch_model("deepseek")

# Get session statistics
stats = manager.get_session_stats()
print(stats)
```

### Session Features

- **Context Preservation**: Maintain task context across model switches
- **Progress Tracking**: Track files modified, tests passed, lines written
- **Model History**: Switch between models and revert if needed
- **Persistent Storage**: Sessions saved to `~/.agentcode/sessions/`

## Multi-Language Support

AgentCode supports 14+ programming languages:

```python
from languages import detect_project_language, get_language_template, ProgrammingLanguage

# Detect project language
language = detect_project_language()
print(language)  # ProgrammingLanguage.PYTHON

# Generate code template
template = get_language_template(
    ProgrammingLanguage.PYTHON,
    "function",
    name="calculate_sum",
    params="a, b",
    docstring="Calculate sum of two numbers"
)
print(template)
```

### Supported Languages

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

## API Reference

### `route_task(task_description, has_image, context_size, is_local_only) -> ModelType`

Routes a coding task to the optimal AI model.

**Parameters:**
- `task_description` (str): Description of the coding task
- `has_image` (bool, optional): Whether task includes image input. Default: False
- `context_size` (int, optional): Estimated context size in tokens. Default: 0
- `is_local_only` (bool, optional): Whether task requires local processing. Default: False

**Returns:**
- `ModelType`: The optimal model for this task

**Example:**
```python
model = route_task("Create docker compose file")
# Returns: ModelType.LAGUNA
```

### `get_model_info(model: ModelType) -> Dict`

Gets information about a model.

**Parameters:**
- `model` (ModelType): The model type to get info about

**Returns:**
- `Dict`: Dictionary with keys: name, provider, strength

**Example:**
```python
info = get_model_info(ModelType.DEEPSEEK)
# Returns: {"name": "DeepSeek V4 Flash", "provider": "DeepSeek", "strength": "Speed"}
```

## Complete Python Implementation

```python
from enum import Enum
from typing import Dict, List, Optional


class ModelType(str, Enum):
    """Available AI model types."""
    MIMO = "opencode/mimo-v2.5-free"
    DEEPSEEK = "opencode/deepseek-v4-flash-free"
    LAGUNA = "opencode/laguna-s-2.1-free"
    LING = "opencode/ling-3.0-flash-free"
    NORTH = "opencode/north-mini-code-free"
    NEMOTRON = "opencode/nemotron-3-ultra-free"


TERMINAL_KEYWORDS: List[str] = ["bash", "shell", "docker", "terminal", "cli", "script", "deploy"]
SPEED_KEYWORDS: List[str] = ["quick", "fast", "rapid", "batch"]


def route_task(
    task_description: str,
    has_image: bool = False,
    context_size: int = 0,
    is_local_only: bool = False
) -> ModelType:
    """Route a task to the optimal AI model."""
    if not task_description:
        raise ValueError("task_description cannot be empty")
    
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


def get_model_info(model: ModelType) -> Dict[str, str]:
    """Get information about a model."""
    models: Dict[ModelType, Dict[str, str]] = {
        ModelType.MIMO: {"name": "MiMo-V2.5", "provider": "Xiaomi", "strength": "Multimodal"},
        ModelType.DEEPSEEK: {"name": "DeepSeek V4 Flash", "provider": "DeepSeek", "strength": "Speed"},
        ModelType.LAGUNA: {"name": "Laguna S 2.1", "provider": "NVIDIA", "strength": "Terminal"},
        ModelType.LING: {"name": "Ling-3.0-flash", "provider": "Alibaba", "strength": "Efficiency"},
        ModelType.NORTH: {"name": "North Mini Code", "provider": "NVIDIA", "strength": "Local"},
        ModelType.NEMOTRON: {"name": "Nemotron 3 Ultra", "provider": "NVIDIA", "strength": "Enterprise"},
    }
    return models.get(model, {})
```

## Test Suite

```python
from agentcode import route_task, get_model_info, ModelType
import pytest


def test_multimodal_routing():
    """Test multimodal task routing."""
    assert route_task("Fix bug", has_image=True) == ModelType.MIMO
    assert route_task("Transcribe audio", has_image=True) == ModelType.MIMO


def test_terminal_routing():
    """Test terminal/CLI task routing."""
    assert route_task("Create docker file") == ModelType.LAGUNA
    assert route_task("Write bash script") == ModelType.LAGUNA
    assert route_task("Build CLI tool") == ModelType.LAGUNA


def test_speed_routing():
    """Test speed-critical task routing."""
    assert route_task("Quick code") == ModelType.DEEPSEEK
    assert route_task("Fast implementation") == ModelType.DEEPSEEK


def test_context_routing():
    """Test large context task routing."""
    assert route_task("Analyze code", context_size=500000) == ModelType.NEMOTRON
    assert route_task("Analyze code", context_size=100000) != ModelType.NEMOTRON


def test_local_routing():
    """Test local-only task routing."""
    assert route_task("Run locally", is_local_only=True) == ModelType.NORTH


def test_default_routing():
    """Test default task routing."""
    assert route_task("Write function") == ModelType.LING
    assert route_task("Create API") == ModelType.LING


def test_empty_description():
    """Test empty description raises error."""
    with pytest.raises(ValueError):
        route_task("")


def test_model_info():
    """Test model info retrieval."""
    for model in ModelType:
        info = get_model_info(model)
        assert "name" in info
        assert "provider" in info
        assert "strength" in info


def test_model_info_unknown():
    """Test unknown model returns empty dict."""
    info = get_model_info("unknown")
    assert info == {}


# Run tests
if __name__ == "__main__":
    pytest.main([__file__, "-v"])
```

## Models

| Model | Provider | Best For | Context |
|-------|----------|----------|---------|
| MiMo-V2.5 | Xiaomi | Multimodal | 1M |
| DeepSeek V4 Flash | DeepSeek | Speed (126 tok/s) | 1M |
| Laguna S 2.1 | NVIDIA | Terminal | 1M |
| Ling-3.0-flash | Alibaba | Efficiency | 256K |
| North Mini Code | NVIDIA | Local | 256K |
| Nemotron 3 Ultra | NVIDIA | Enterprise | 1M |

## Usage Examples

```
User: "Create FastAPI endpoint"
→ DeepSeek V4 Flash (fastest at 126 tokens/s)

User: "Fix UI bug [screenshot]"
→ MiMo-V2.5 (multimodal support)

User: "Create docker compose"
→ Laguna S 2.1 (terminal expert)

User: "Analyze large codebase"
→ Nemotron 3 Ultra (1M context)

User: "Run locally"
→ North Mini Code (sovereign AI)
```

## Configuration

AgentCode saves configuration to `~/.agentcode/config.json`:

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

## Links

- GitHub: https://github.com/mrcbrbn5361/agentcode
- OpenAgentSkill: https://www.openagentskill.com/skills/agentcode

## License

MIT