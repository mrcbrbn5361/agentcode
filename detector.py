"""
AgentCode v0.0.2 - System Model Detection Engine

Detects all AI models available on user's system (CLI tools, IDE extensions, cloud APIs)
and presents them for selection with intelligent recommendations.
"""

import os
import subprocess
import json
import platform
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
from enum import Enum


class ModelCategory(str, Enum):
    """Categories of AI models."""
    CLI = "cli"
    IDE = "ide"
    CLOUD = "cloud"
    LOCAL = "local"


@dataclass
class DetectedModel:
    """Represents a detected AI model."""
    name: str
    category: ModelCategory
    source: str
    version: Optional[str] = None
    capabilities: List[str] = None
    is_available: bool = True
    
    def __post_init__(self):
        if self.capabilities is None:
            self.capabilities = []


class SystemDetector:
    """Detects AI models available on the user's system."""
    
    def __init__(self):
        self.detected_models: List[DetectedModel] = []
        self.system_info = self._get_system_info()
    
    def _get_system_info(self) -> Dict:
        """Get basic system information."""
        return {
            "platform": platform.system(),
            "machine": platform.machine(),
            "python_version": platform.python_version(),
        }
    
    def detect_all(self) -> List[DetectedModel]:
        """Detect all available AI models on the system."""
        self.detected_models = []
        
        # Detect CLI tools
        self._detect_cli_tools()
        
        # Detect IDE extensions
        self._detect_ide_extensions()
        
        # Detect cloud APIs
        self._detect_cloud_apis()
        
        # Detect local models
        self._detect_local_models()
        
        return self.detected_models
    
    def _detect_cli_tools(self):
        """Detect AI CLI tools installed on the system."""
        cli_tools = {
            "openai": {
                "name": "OpenAI CLI",
                "models": ["gpt-4", "gpt-4-turbo", "gpt-4o"],
                "check_cmd": ["which", "openai"],
                "version_cmd": ["openai", "--version"],
            },
            "anthropic": {
                "name": "Anthropic CLI",
                "models": ["claude-3.5-sonnet", "claude-3-opus"],
                "check_cmd": ["which", "anthropic"],
                "version_cmd": ["anthropic", "--version"],
            },
            "gemini": {
                "name": "Google Gemini CLI",
                "models": ["gemini-pro", "gemini-ultra"],
                "check_cmd": ["which", "gemini"],
                "version_cmd": ["gemini", "--version"],
            },
            "ollama": {
                "name": "Ollama",
                "models": ["llama3.1", "codellama", "mistral"],
                "check_cmd": ["which", "ollama"],
                "version_cmd": ["ollama", "--version"],
            },
            "llama.cpp": {
                "name": "llama.cpp",
                "models": ["quantized-gguf"],
                "check_cmd": ["which", "llama-cli"],
                "version_cmd": ["llama-cli", "--version"],
            },
            "vllm": {
                "name": "vLLM",
                "models": ["local-llm"],
                "check_cmd": ["which", "vllm"],
                "version_cmd": ["vllm", "--version"],
            },
            "lmstudio": {
                "name": "LM Studio",
                "models": ["local-models"],
                "check_cmd": ["which", "lmstudio"],
                "version_cmd": ["lmstudio", "--version"],
            },
            "codexbar": {
                "name": "CodexBar",
                "models": ["usage-analytics"],
                "check_cmd": ["which", "codexbar"],
                "version_cmd": ["codexbar", "--version"],
            },
        }
        
        for tool_id, tool_info in cli_tools.items():
            if self._check_command_exists(tool_info["check_cmd"]):
                version = self._get_command_version(tool_info["version_cmd"])
                model = DetectedModel(
                    name=tool_info["name"],
                    category=ModelCategory.CLI,
                    source=tool_id,
                    version=version,
                    capabilities=tool_info["models"],
                )
                self.detected_models.append(model)
    
    def _detect_ide_extensions(self):
        """Detect AI extensions in IDEs."""
        ide_extensions = {
            "vscode": {
                "name": "VS Code",
                "extensions": {
                    "github.copilot": "GitHub Copilot",
                    "codeium.codeium": "Codeium",
                    "continue.continue": "Continue",
                    "tabnine.tabnine-vscode": "Tabnine",
                },
                "config_paths": [
                    "~/.config/Code/User/settings.json",
                    "~/.vscode/extensions",
                ],
            },
            "cursor": {
                "name": "Cursor",
                "extensions": {
                    "cursorAI": "Built-in AI",
                },
                "config_paths": [
                    "~/.cursor/settings.json",
                ],
            },
            "windsurf": {
                "name": "Windsurf",
                "extensions": {
                    "windsurfAI": "Built-in AI",
                },
                "config_paths": [
                    "~/.windsurf/settings.json",
                ],
            },
            "jetbrains": {
                "name": "JetBrains",
                "extensions": {
                    "com.intellij.ai": "AI Assistant",
                    "com.intellij.codegpt": "CodeGPT",
                },
                "config_paths": [
                    "~/.config/JetBrains",
                ],
            },
        }
        
        for ide_id, ide_info in ide_extensions.items():
            if self._check_ide_installed(ide_id):
                for ext_id, ext_name in ide_info["extensions"].items():
                    model = DetectedModel(
                        name=f"{ide_info['name']} - {ext_name}",
                        category=ModelCategory.IDE,
                        source=f"{ide_id}:{ext_id}",
                        capabilities=[ext_name],
                    )
                    self.detected_models.append(model)
    
    def _detect_cloud_apis(self):
        """Detect available cloud API endpoints."""
        cloud_apis = {
            "OPENAI_API_KEY": {
                "name": "OpenAI API",
                "models": ["gpt-4", "gpt-4-turbo", "gpt-4o"],
            },
            "ANTHROPIC_API_KEY": {
                "name": "Anthropic API",
                "models": ["claude-3.5-sonnet", "claude-3-opus"],
            },
            "GOOGLE_API_KEY": {
                "name": "Google Gemini API",
                "models": ["gemini-pro", "gemini-ultra"],
            },
            "DEEPSEEK_API_KEY": {
                "name": "DeepSeek API",
                "models": ["deepseek-v4", "deepseek-v3"],
            },
            "MISTRAL_API_KEY": {
                "name": "Mistral API",
                "models": ["mistral-large", "mixtral"],
            },
            "GROQ_API_KEY": {
                "name": "Groq API",
                "models": ["llama-3.1", "mixtral"],
            },
            "TOGETHER_API_KEY": {
                "name": "Together API",
                "models": ["various-open-source"],
            },
        }
        
        for env_var, api_info in cloud_apis.items():
            if os.environ.get(env_var):
                model = DetectedModel(
                    name=api_info["name"],
                    category=ModelCategory.CLOUD,
                    source=env_var,
                    capabilities=api_info["models"],
                )
                self.detected_models.append(model)
    
    def _detect_local_models(self):
        """Detect locally installed models."""
        local_model_paths = [
            "~/.ollama/models",
            "~/.cache/lm-studio/models",
            "~/.local/share/lm-studio/models",
            "/usr/share/ollama/.ollama/models",
        ]
        
        for path_str in local_model_paths:
            path = Path(path_str).expanduser()
            if path.exists():
                model = DetectedModel(
                    name=f"Local Models ({path_str})",
                    category=ModelCategory.LOCAL,
                    source=str(path),
                    capabilities=["local-inference"],
                )
                self.detected_models.append(model)
    
    def _check_command_exists(self, cmd: List[str]) -> bool:
        """Check if a command exists on the system."""
        try:
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=5,
            )
            return result.returncode == 0
        except (subprocess.TimeoutExpired, FileNotFoundError, OSError):
            return False
    
    def _get_command_version(self, cmd: List[str]) -> Optional[str]:
        """Get version of a command."""
        try:
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=5,
            )
            if result.returncode == 0:
                # Extract version from output
                output = result.stdout.strip()
                if output:
                    return output.split("\n")[0]
        except (subprocess.TimeoutExpired, FileNotFoundError, OSError):
            pass
        return None
    
    def _check_ide_installed(self, ide_id: str) -> bool:
        """Check if an IDE is installed."""
        ide_checks = {
            "vscode": ["which", "code"],
            "cursor": ["which", "cursor"],
            "windsurf": ["which", "windsurf"],
            "jetbrains": ["which", "idea"],
        }
        
        cmd = ide_checks.get(ide_id)
        if cmd:
            return self._check_command_exists(cmd)
        return False
    
    def get_models_by_category(self, category: ModelCategory) -> List[DetectedModel]:
        """Get models filtered by category."""
        return [m for m in self.detected_models if m.category == category]
    
    def get_summary(self) -> Dict:
        """Get summary of detected models."""
        summary = {
            "total": len(self.detected_models),
            "by_category": {},
        }
        
        for category in ModelCategory:
            models = self.get_models_by_category(category)
            summary["by_category"][category.value] = {
                "count": len(models),
                "models": [m.name for m in models],
            }
        
        return summary


def detect_system_models() -> List[DetectedModel]:
    """Convenience function to detect all system models."""
    detector = SystemDetector()
    return detector.detect_all()


def print_detection_report(models: List[DetectedModel]):
    """Print a formatted detection report."""
    print("\n" + "="*60)
    print("AgentCode System Model Detection")
    print("="*60 + "\n")
    
    detector = SystemDetector()
    detector.detected_models = models
    summary = detector.get_summary()
    
    print(f"Total models detected: {summary['total']}\n")
    
    for category, info in summary["by_category"].items():
        if info["count"] > 0:
            print(f"\n{category.upper()} ({info['count']} found):")
            for model_name in info["models"]:
                print(f"  ✓ {model_name}")
    
    print("\n" + "="*60 + "\n")


if __name__ == "__main__":
    models = detect_system_models()
    print_detection_report(models)