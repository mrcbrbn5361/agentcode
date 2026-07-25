#!/usr/bin/env python3
"""
AgentCode - Smart Multi-Model Coding Agent
Routes tasks to optimal free AI models based on task type.
"""

from typing import Optional
from enum import Enum


class ModelType(str, Enum):
    """Available AI model types."""
    MIMO = "opencode/mimo-v2.5-free"
    DEEPSEEK = "opencode/deepseek-v4-flash-free"
    LAGUNA = "opencode/laguna-s-2.1-free"
    LING = "opencode/ling-3.0-flash-free"
    NORTH = "opencode/north-mini-code-free"
    NEMOTRON = "opencode/nemotron-3-ultra-free"
    BIG_PICKLE = "opencode/big-pickle"


class TaskType(str, Enum):
    """Task types for routing."""
    CODE = "code"
    MULTIMODAL = "multimodal"
    TERMINAL = "terminal"
    LARGE_CONTEXT = "large_context"
    LOCAL = "local"
    BUDGET = "budget"
    PLANNING = "planning"


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
    Route a task to the optimal AI model.
    
    Args:
        task_description: Description of the coding task
        has_image: Whether task includes image input
        has_audio: Whether task includes audio input  
        has_video: Whether task includes video input
        context_size: Estimated context size in tokens
        is_local_only: Whether task requires local processing
        is_budget_conscious: Whether task is budget-sensitive
        
    Returns:
        ModelType: The optimal model for this task
    """
    # Check for multimodal tasks first
    if has_image or has_audio or has_video:
        return ModelType.MIMO
    
    # Check for terminal/CLI tasks
    terminal_keywords = [
        "bash", "shell", "docker", "terminal", "cli", "script",
        "deploy", "compose", "nginx", "git", "command"
    ]
    if any(kw in task_description.lower() for kw in terminal_keywords):
        return ModelType.LAGUNA
    
    # Check for large context
    if context_size > 256000:
        return ModelType.NEMOTRON
    
    # Check for local-only requirement
    if is_local_only:
        return ModelType.NORTH
    
    # Check for budget-conscious tasks
    if is_budget_conscious:
        return ModelType.LING
    
    # Check for speed-critical tasks
    speed_keywords = ["quick", "fast", "rapid", "batch", "multiple"]
    if any(kw in task_description.lower() for kw in speed_keywords):
        return ModelType.DEEPSEEK
    
    # Default to Big Pickle for general tasks
    return ModelType.BIG_PICKLE


def get_model_info(model: ModelType) -> dict:
    """Get information about a model."""
    models = {
        ModelType.MIMO: {
            "name": "MiMo-V2.5 Free",
            "strength": "Multimodal",
            "context": "1M",
            "speed": "High",
        },
        ModelType.DEEPSEEK: {
            "name": "DeepSeek V4 Flash Free", 
            "strength": "Speed",
            "context": "1M",
            "speed": "126 tok/s",
        },
        ModelType.LAGUNA: {
            "name": "Laguna S 2.1 Free",
            "strength": "Terminal",
            "context": "1M",
            "speed": "High",
        },
        ModelType.LING: {
            "name": "Ling-3.0-flash Free",
            "strength": "Efficiency",
            "context": "256K",
            "speed": "Medium",
        },
        ModelType.NORTH: {
            "name": "North Mini Code Free",
            "strength": "Local",
            "context": "256K",
            "speed": "Medium",
        },
        ModelType.NEMOTRON: {
            "name": "Nemotron 3 Ultra Free",
            "strength": "Enterprise",
            "context": "1M",
            "speed": "300+ tok/s",
        },
        ModelType.BIG_PICKLE: {
            "name": "Big Pickle",
            "strength": "Daily Coding",
            "context": "200K",
            "speed": "Medium",
        },
    }
    return models.get(model, {})


# Example usage
if __name__ == "__main__":
    # Example 1: Code generation task
    model = route_task("Create a Python FastAPI endpoint")
    print(f"Task: Create API endpoint")
    print(f"Model: {get_model_info(model)['name']}")
    print()
    
    # Example 2: Multimodal task
    model = route_task("Fix this UI bug", has_image=True)
    print(f"Task: Fix UI bug with screenshot")
    print(f"Model: {get_model_info(model)['name']}")
    print()
    
    # Example 3: Terminal task
    model = route_task("Create docker compose file")
    print(f"Task: Create Docker compose")
    print(f"Model: {get_model_info(model)['name']}")
    print()
    
    # Example 4: Large context
    model = route_task("Analyze this codebase", context_size=500000)
    print(f"Task: Analyze large codebase")
    print(f"Model: {get_model_info(model)['name']}")
