#!/usr/bin/env python3
"""
AgentCode - Smart Multi-Model Coding Agent
==========================================

This module routes coding tasks to the optimal free AI model based on
task type, context requirements, and performance needs.

Supported Models:
- MiMo-V2.5 (opencode/mimo-v2.5-free) - Multimodal tasks
- DeepSeek V4 Flash (opencode/deepseek-v4-flash-free) - High-speed coding
- Laguna S 2.1 (opencode/laguna-s-2.1-free) - Terminal/CLI tasks
- Ling-3.0-flash (opencode/ling-3.0-flash-free) - Token-efficient
- North Mini Code (opencode/north-mini-code-free) - Local deployment
- Nemotron 3 Ultra (opencode/nemotron-3-ultra-free) - Enterprise
- Big Pickle (opencode/big-pickle) - Daily coding

Author: AgentCode Contributors
License: MIT
Version: 0.0.1
"""

from enum import Enum
from typing import Dict, List, Optional


class ModelType(str, Enum):
    """
    Enumeration of available AI model types.
    
    Each model has a unique identifier following the OpenCode format:
    opencode/<model-name>-free
    """
    
    # Multimodal model - supports image, audio, video
    MIMO = "opencode/mimo-v2.5-free"
    
    # High-speed model - 126 tokens/second
    DEEPSEEK = "opencode/deepseek-v4-flash-free"
    
    # Terminal/CLI expert - Terminal-Bench 70.2%
    LAGUNA = "opencode/laguna-s-2.1-free"
    
    # Token-efficient model - 5.1B active parameters
    LING = "opencode/ling-3.0-flash-free"
    
    # Local deployment model - sovereign AI
    NORTH = "opencode/north-mini-code-free"
    
    # Enterprise model - 1M context window
    NEMOTRON = "opencode/nemotron-3-ultra-free"
    
    # Daily coding model - free tier
    BIG_PICKLE = "opencode/big-pickle"


# Model information database
MODEL_DATABASE: Dict[ModelType, Dict] = {
    ModelType.MIMO: {
        "name": "MiMo-V2.5 Free",
        "provider": "Xiaomi",
        "strength": "Multimodal (Image+Audio+Video)",
        "context": "1M tokens",
        "speed": "Medium",
        "verification_url": "https://huggingface.co/Xiaomi-MiMo",
        "best_for": ["image_analysis", "audio_transcription", "video_analysis"],
    },
    ModelType.DEEPSEEK: {
        "name": "DeepSeek V4 Flash Free",
        "provider": "DeepSeek",
        "strength": "High-speed coding",
        "context": "1M tokens",
        "speed": "126 tokens/second",
        "verification_url": "https://platform.deepseek.com/api-docs",
        "best_for": ["quick_code", "batch_processing", "rapid_prototyping"],
    },
    ModelType.LAGUNA: {
        "name": "Laguna S 2.1 Free",
        "provider": "NVIDIA",
        "strength": "Terminal/CLI tasks",
        "context": "1M tokens",
        "speed": "High",
        "verification_url": "https://build.nvidia.com/nvidia/laguna-2-1",
        "best_for": ["bash_scripts", "docker", "cli_tools", "deployment"],
    },
    ModelType.LING: {
        "name": "Ling-3.0-flash Free",
        "provider": "Alibaba",
        "strength": "Token efficiency",
        "context": "256K tokens",
        "speed": "Medium",
        "verification_url": "https://help.aliyun.com/zh/model-studio/getting-started/models",
        "best_for": ["cost_optimization", "high_volume", "budget_tasks"],
    },
    ModelType.NORTH: {
        "name": "North Mini Code Free",
        "provider": "NVIDIA",
        "strength": "Local deployment",
        "context": "256K tokens",
        "speed": "Medium",
        "verification_url": "https://build.nvidia.com/nvidia/north-mini-code",
        "best_for": ["local_processing", "sensitive_data", "sovereign_ai"],
    },
    ModelType.NEMOTRON: {
        "name": "Nemotron 3 Ultra Free",
        "provider": "NVIDIA",
        "strength": "Enterprise & long context",
        "context": "1M tokens",
        "speed": "300+ tokens/second",
        "verification_url": "https://build.nvidia.com/nvidia/nemotron-3-ultra",
        "best_for": ["large_codebase", "complex_reasoning", "enterprise"],
    },
    ModelType.BIG_PICKLE: {
        "name": "Big Pickle",
        "provider": "Stealth (undisclosed)",
        "strength": "Daily coding & planning",
        "context": "200K tokens",
        "speed": "Medium",
        "verification_url": None,
        "best_for": ["planning", "quick_tasks", "exploration"],
    },
}

# Terminal/CLI related keywords for task detection
TERMINAL_KEYWORDS: List[str] = [
    "bash", "shell", "docker", "terminal", "cli", "script",
    "deploy", "compose", "nginx", "git", "command", "pipeline",
    "ci/cd", "automation", "workflow", "orchestration",
]

# Speed-related keywords for task detection
SPEED_KEYWORDS: List[str] = [
    "quick", "fast", "rapid", "batch", "multiple", "speed",
    "performance", "optimize", "parallel", "concurrent",
]


def validate_model_id(model_id: str) -> bool:
    """
    Validate that a model ID follows the correct format.
    
    Args:
        model_id: The model ID to validate
        
    Returns:
        bool: True if valid, False otherwise
        
    Examples:
        >>> validate_model_id("opencode/mimo-v2.5-free")
        True
        >>> validate_model_id("invalid-model")
        False
    """
    if not model_id:
        return False
    
    # Check format: opencode/<name>-free
    if not model_id.startswith("opencode/"):
        return False
    
    if not model_id.endswith("-free") and model_id != "opencode/big-pickle":
        return False
    
    # Check for valid characters
    valid_chars = set("abcdefghijklmnopqrstuvwxyz0123456789-._/")
    return all(c in valid_chars for c in model_id)


def detect_task_type(
    task_description: str,
    has_image: bool = False,
    has_audio: bool = False,
    has_video: bool = False,
    context_size: int = 0,
    is_local_only: bool = False,
    is_budget_conscious: bool = False,
) -> str:
    """
    Detect the type of task based on description and parameters.
    
    Args:
        task_description: Natural language description of the task
        has_image: Whether task includes image input
        has_audio: Whether task includes audio input
        has_video: Whether task includes video input
        context_size: Estimated context size in tokens
        is_local_only: Whether task requires local processing
        is_budget_conscious: Whether task is budget-sensitive
        
    Returns:
        str: Detected task type
        
    Examples:
        >>> detect_task_type("Fix this bug", has_image=True)
        "multimodal"
        >>> detect_task_type("Create docker compose file")
        "terminal"
    """
    # Check for multimodal tasks first (highest priority)
    if has_image or has_audio or has_video:
        return "multimodal"
    
    # Check for terminal/CLI tasks
    task_lower = task_description.lower()
    if any(keyword in task_lower for keyword in TERMINAL_KEYWORDS):
        return "terminal"
    
    # Check for large context requirements
    if context_size > 256000:
        return "large_context"
    
    # Check for local-only requirement
    if is_local_only:
        return "local"
    
    # Check for budget-conscious tasks
    if is_budget_conscious:
        return "budget"
    
    # Check for speed-critical tasks
    if any(keyword in task_lower for keyword in SPEED_KEYWORDS):
        return "speed"
    
    # Default to general coding task
    return "general"


def route_task(
    task_description: str,
    has_image: bool = False,
    has_audio: bool = False,
    has_video: bool = False,
    context_size: int = 0,
    is_local_only: bool = False,
    is_budget_conscious: bool = False,
) -> ModelType:
    """
    Route a coding task to the optimal AI model.
    
    This function analyzes the task requirements and selects the best
    model based on task type, context size, and other constraints.
    
    Args:
        task_description: Natural language description of the coding task
        has_image: Whether task includes image input
        has_audio: Whether task includes audio input
        has_video: Whether task includes video input
        context_size: Estimated context size in tokens
        is_local_only: Whether task requires local processing
        is_budget_conscious: Whether task is budget-sensitive
        
    Returns:
        ModelType: The optimal model for this task
        
    Examples:
        >>> route_task("Create a FastAPI endpoint")
        ModelType.DEEPSEEK
        
        >>> route_task("Fix this UI bug", has_image=True)
        ModelType.MIMO
        
        >>> route_task("Create docker compose file")
        ModelType.LAGUNA
    """
    # Detect task type
    task_type = detect_task_type(
        task_description=task_description,
        has_image=has_image,
        has_audio=has_audio,
        has_video=has_video,
        context_size=context_size,
        is_local_only=is_local_only,
        is_budget_conscious=is_budget_conscious,
    )
    
    # Route based on task type
    routing_map = {
        "multimodal": ModelType.MIMO,
        "terminal": ModelType.LAGUNA,
        "large_context": ModelType.NEMOTRON,
        "local": ModelType.NORTH,
        "budget": ModelType.LING,
        "speed": ModelType.DEEPSEEK,
        "general": ModelType.BIG_PICKLE,
    }
    
    return routing_map.get(task_type, ModelType.BIG_PICKLE)


def get_model_info(model: ModelType) -> Dict:
    """
    Get detailed information about a model.
    
    Args:
        model: The model type to get information about
        
    Returns:
        Dict: Model information including name, provider, strengths
        
    Examples:
        >>> info = get_model_info(ModelType.MIMO)
        >>> print(info["name"])
        "MiMo-V2.5 Free"
    """
    return MODEL_DATABASE.get(model, {})


def get_all_models() -> List[Dict]:
    """
    Get information about all available models.
    
    Returns:
        List[Dict]: List of all model information
    """
    return [
        {
            "model_id": model.value,
            **info
        }
        for model, info in MODEL_DATABASE.items()
    ]


def explain_routing(task_description: str, model: ModelType) -> str:
    """
    Generate a human-readable explanation of why a model was selected.
    
    Args:
        task_description: The original task description
        model: The selected model
        
    Returns:
        str: Explanation text
    """
    info = get_model_info(model)
    
    explanation = f"📊 Görev Analizi: {task_description}\n"
    explanation += f"🎯 Seçilen Model: {info.get('name', 'Unknown')}\n"
    explanation += f"🏢 Sağlayıcı: {info.get('provider', 'Unknown')}\n"
    explanation += f"💪 Güçlü Yön: {info.get('strength', 'Unknown')}\n"
    explanation += f"📝 Context: {info.get('context', 'Unknown')}\n"
    explanation += f"⚡ Hız: {info.get('speed', 'Unknown')}\n"
    
    if info.get("verification_url"):
        explanation += f"🔗 Doğrulama: {info['verification_url']}\n"
    
    return explanation


# Example usage and demonstration
if __name__ == "__main__":
    print("=" * 60)
    print("AgentCode - Smart Multi-Model Routing Demo")
    print("=" * 60)
    print()
    
    # Example 1: Code generation task
    print("Example 1: Code Generation")
    print("-" * 40)
    model = route_task("Create a Python FastAPI endpoint")
    print(explain_routing("Create a Python FastAPI endpoint", model))
    print()
    
    # Example 2: Multimodal task
    print("Example 2: Image Analysis")
    print("-" * 40)
    model = route_task("Fix this UI bug", has_image=True)
    print(explain_routing("Fix this UI bug", model))
    print()
    
    # Example 3: Terminal task
    print("Example 3: Terminal Task")
    print("-" * 40)
    model = route_task("Create docker compose file")
    print(explain_routing("Create docker compose file", model))
    print()
    
    # Example 4: Large context
    print("Example 4: Large Codebase Analysis")
    print("-" * 40)
    model = route_task("Analyze this codebase", context_size=500000)
    print(explain_routing("Analyze this codebase", model))
    print()
    
    # List all models
    print("All Available Models:")
    print("-" * 40)
    for model_info in get_all_models():
        print(f"  {model_info['model_id']}: {model_info['name']}")
