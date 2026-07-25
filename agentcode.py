"""
AgentCode - Smart Multi-Model Coding Agent

Smart routing across 7 verified free AI models for OpenCode. MIT License.
"""

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