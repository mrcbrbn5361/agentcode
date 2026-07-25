#!/usr/bin/env python3
"""
Comprehensive Tests for AgentCode Routing Logic
================================================

This module contains unit tests and integration tests for the
AgentCode smart routing system.

Test Coverage:
- Model type validation
- Task detection
- Routing logic
- Model information
- Edge cases
- Integration tests

Author: AgentCode Contributors
License: MIT
Version: 0.0.1
"""

import pytest
from agentcode import (
    ModelType,
    route_task,
    get_model_info,
    get_all_models,
    detect_task_type,
    validate_model_id,
    explain_routing,
    MODEL_DATABASE,
    TERMINAL_KEYWORDS,
    SPEED_KEYWORDS,
)


class TestModelType:
    """Test ModelType enumeration."""
    
    def test_all_models_exist(self):
        """Test that all 7 models are defined."""
        assert len(ModelType) == 7
    
    def test_model_ids_format(self):
        """Test that all model IDs follow OpenCode format."""
        for model in ModelType:
            if model == ModelType.BIG_PICKLE:
                assert model.value == "opencode/big-pickle"
            else:
                assert model.value.startswith("opencode/")
                assert model.value.endswith("-free")
    
    def test_model_ids_are_strings(self):
        """Test that all model IDs are strings."""
        for model in ModelType:
            assert isinstance(model.value, str)
    
    def test_model_ids_unique(self):
        """Test that all model IDs are unique."""
        ids = [model.value for model in ModelType]
        assert len(ids) == len(set(ids))


class TestValidateModelId:
    """Test model ID validation."""
    
    def test_valid_model_ids(self):
        """Test that valid model IDs are accepted."""
        assert validate_model_id("opencode/mimo-v2.5-free") is True
        assert validate_model_id("opencode/deepseek-v4-flash-free") is True
        assert validate_model_id("opencode/big-pickle") is True
    
    def test_invalid_model_ids(self):
        """Test that invalid model IDs are rejected."""
        assert validate_model_id("") is False
        assert validate_model_id("invalid") is False
        assert validate_model_id("openai/gpt-4") is False
        assert validate_model_id("opencode/invalid") is False
    
    def test_empty_string(self):
        """Test that empty string is rejected."""
        assert validate_model_id("") is False
    
    def test_none_value(self):
        """Test that None value is rejected."""
        assert validate_model_id(None) is False


class TestDetectTaskType:
    """Test task type detection."""
    
    def test_multimodal_image(self):
        """Test detection of image tasks."""
        assert detect_task_type("Fix this bug", has_image=True) == "multimodal"
    
    def test_multimodal_audio(self):
        """Test detection of audio tasks."""
        assert detect_task_type("Transcribe this", has_audio=True) == "multimodal"
    
    def test_multimodal_video(self):
        """Test detection of video tasks."""
        assert detect_task_type("Analyze video", has_video=True) == "multimodal"
    
    def test_multimodal_priority(self):
        """Test that multimodal has highest priority."""
        assert detect_task_type(
            "Create docker file",
            has_image=True,
            context_size=500000
        ) == "multimodal"
    
    def test_terminal_bash(self):
        """Test detection of bash tasks."""
        assert detect_task_type("Create a bash script") == "terminal"
    
    def test_terminal_docker(self):
        """Test detection of docker tasks."""
        assert detect_task_type("Create docker compose file") == "terminal"
    
    def test_terminal_cli(self):
        """Test detection of CLI tasks."""
        assert detect_task_type("Build a CLI tool") == "terminal"
    
    def test_terminal_keywords(self):
        """Test all terminal keywords are detected."""
        for keyword in TERMINAL_KEYWORDS:
            assert detect_task_type(f"Task with {keyword}") == "terminal"
    
    def test_large_context(self):
        """Test detection of large context tasks."""
        assert detect_task_type("Analyze this", context_size=500000) == "large_context"
    
    def test_large_context_threshold(self):
        """Test context size threshold."""
        assert detect_task_type("Task", context_size=256001) == "large_context"
        assert detect_task_type("Task", context_size=256000) != "large_context"
    
    def test_local_only(self):
        """Test detection of local-only tasks."""
        assert detect_task_type("Run locally", is_local_only=True) == "local"
    
    def test_budget_conscious(self):
        """Test detection of budget tasks."""
        assert detect_task_type("Process files", is_budget_conscious=True) == "budget"
    
    def test_speed_critical(self):
        """Test detection of speed-critical tasks."""
        assert detect_task_type("Quick code generation") == "speed"
    
    def test_speed_keywords(self):
        """Test all speed keywords are detected."""
        for keyword in SPEED_KEYWORDS:
            assert detect_task_type(f"Task with {keyword}") == "speed"
    
    def test_general_task(self):
        """Test detection of general tasks."""
        assert detect_task_type("Write a function") == "general"
    
    def test_case_insensitive(self):
        """Test that detection is case insensitive."""
        assert detect_task_type("DOCKER compose") == "terminal"
        assert detect_task_type("Quick CODE") == "speed"


class TestRouteTask:
    """Test the route_task function."""
    
    def test_multimodal_routes_to_mimo(self):
        """Test that multimodal tasks route to MiMo."""
        model = route_task("Fix this bug", has_image=True)
        assert model == ModelType.MIMO
    
    def test_terminal_routes_to_laguna(self):
        """Test that terminal tasks route to Laguna."""
        model = route_task("Create docker compose file")
        assert model == ModelType.LAGUNA
    
    def test_large_context_routes_to_nemotron(self):
        """Test that large context tasks route to Nemotron."""
        model = route_task("Analyze this", context_size=500000)
        assert model == ModelType.NEMOTRON
    
    def test_local_routes_to_north(self):
        """Test that local tasks route to North."""
        model = route_task("Run locally", is_local_only=True)
        assert model == ModelType.NORTH
    
    def test_budget_routes_to_ling(self):
        """Test that budget tasks route to Ling."""
        model = route_task("Process files", is_budget_conscious=True)
        assert model == ModelType.LING
    
    def test_speed_routes_to_deepseek(self):
        """Test that speed tasks route to DeepSeek."""
        model = route_task("Quick code generation")
        assert model == ModelType.DEEPSEEK
    
    def test_general_routes_to_big_pickle(self):
        """Test that general tasks route to Big Pickle."""
        model = route_task("Write a function")
        assert model == ModelType.BIG_PICKLE
    
    def test_routing_returns_model_type(self):
        """Test that routing returns ModelType enum."""
        model = route_task("Any task")
        assert isinstance(model, ModelType)
    
    def test_routing_with_multiple_params(self):
        """Test routing with multiple parameters."""
        model = route_task(
            "Create docker file",
            has_image=False,
            context_size=100000,
            is_local_only=False,
            is_budget_conscious=False
        )
        assert model == ModelType.LAGUNA


class TestGetModelInfo:
    """Test the get_model_info function."""
    
    def test_all_models_have_info(self):
        """Test that all models have complete information."""
        for model in ModelType:
            info = get_model_info(model)
            assert "name" in info
            assert "provider" in info
            assert "strength" in info
            assert "context" in info
            assert "speed" in info
    
    def test_model_names_correct(self):
        """Test that model names are correct."""
        assert get_model_info(ModelType.MIMO)["name"] == "MiMo-V2.5 Free"
        assert get_model_info(ModelType.DEEPSEEK)["name"] == "DeepSeek V4 Flash Free"
        assert get_model_info(ModelType.LAGUNA)["name"] == "Laguna S 2.1 Free"
        assert get_model_info(ModelType.LING)["name"] == "Ling-3.0-flash Free"
        assert get_model_info(ModelType.NORTH)["name"] == "North Mini Code Free"
        assert get_model_info(ModelType.NEMOTRON)["name"] == "Nemotron 3 Ultra Free"
        assert get_model_info(ModelType.BIG_PICKLE)["name"] == "Big Pickle"
    
    def test_model_providers_correct(self):
        """Test that model providers are correct."""
        assert get_model_info(ModelType.MIMO)["provider"] == "Xiaomi"
        assert get_model_info(ModelType.DEEPSEEK)["provider"] == "DeepSeek"
        assert get_model_info(ModelType.LAGUNA)["provider"] == "NVIDIA"
        assert get_model_info(ModelType.LING)["provider"] == "Alibaba"
        assert get_model_info(ModelType.NORTH)["provider"] == "NVIDIA"
        assert get_model_info(ModelType.NEMOTRON)["provider"] == "NVIDIA"
    
    def test_model_context_windows(self):
        """Test that context windows are correct."""
        assert get_model_info(ModelType.MIMO)["context"] == "1M tokens"
        assert get_model_info(ModelType.DEEPSEEK)["context"] == "1M tokens"
        assert get_model_info(ModelType.LAGUNA)["context"] == "1M tokens"
        assert get_model_info(ModelType.LING)["context"] == "256K tokens"
        assert get_model_info(ModelType.NORTH)["context"] == "256K tokens"
        assert get_model_info(ModelType.NEMOTRON)["context"] == "1M tokens"
        assert get_model_info(ModelType.BIG_PICKLE)["context"] == "200K tokens"
    
    def test_verification_urls(self):
        """Test that verification URLs are provided."""
        assert get_model_info(ModelType.MIMO)["verification_url"] is not None
        assert get_model_info(ModelType.DEEPSEEK)["verification_url"] is not None
        assert get_model_info(ModelType.LAGUNA)["verification_url"] is not None
        assert get_model_info(ModelType.LING)["verification_url"] is not None
        assert get_model_info(ModelType.NORTH)["verification_url"] is not None
        assert get_model_info(ModelType.NEMOTRON)["verification_url"] is not None
    
    def test_invalid_model_returns_empty(self):
        """Test that invalid model returns empty dict."""
        info = get_model_info("invalid")
        assert info == {}


class TestGetAllModels:
    """Test the get_all_models function."""
    
    def test_returns_list(self):
        """Test that function returns a list."""
        models = get_all_models()
        assert isinstance(models, list)
    
    def test_returns_all_models(self):
        """Test that function returns all 7 models."""
        models = get_all_models()
        assert len(models) == 7
    
    def test_models_have_required_fields(self):
        """Test that all models have required fields."""
        models = get_all_models()
        for model in models:
            assert "model_id" in model
            assert "name" in model
            assert "provider" in model
            assert "strength" in model


class TestExplainRouting:
    """Test the explain_routing function."""
    
    def test_returns_string(self):
        """Test that function returns a string."""
        explanation = explain_routing("Test task", ModelType.MIMO)
        assert isinstance(explanation, str)
    
    def test_contains_model_name(self):
        """Test that explanation contains model name."""
        explanation = explain_routing("Test task", ModelType.MIMO)
        assert "MiMo-V2.5 Free" in explanation
    
    def test_contains_provider(self):
        """Test that explanation contains provider."""
        explanation = explain_routing("Test task", ModelType.MIMO)
        assert "Xiaomi" in explanation
    
    def test_contains_strength(self):
        """Test that explanation contains strength."""
        explanation = explain_routing("Test task", ModelType.MIMO)
        assert "Multimodal" in explanation
    
    def test_contains_task_description(self):
        """Test that explanation contains task description."""
        explanation = explain_routing("My test task", ModelType.DEEPSEEK)
        assert "My test task" in explanation


class TestModelDatabase:
    """Test the MODEL_DATABASE constant."""
    
    def test_database_has_all_models(self):
        """Test that database has all 7 models."""
        assert len(MODEL_DATABASE) == 7
    
    def test_database_keys_match_enum(self):
        """Test that database keys match ModelType enum."""
        for model in ModelType:
            assert model in MODEL_DATABASE
    
    def test_database_values_are_dicts(self):
        """Test that all database values are dictionaries."""
        for model, info in MODEL_DATABASE.items():
            assert isinstance(info, dict)


class TestEdgeCases:
    """Test edge cases and boundary conditions."""
    
    def test_empty_task_description(self):
        """Test routing with empty task description."""
        model = route_task("")
        assert isinstance(model, ModelType)
    
    def test_very_long_task_description(self):
        """Test routing with very long task description."""
        long_description = "x" * 10000
        model = route_task(long_description)
        assert isinstance(model, ModelType)
    
    def test_special_characters_in_task(self):
        """Test routing with special characters."""
        model = route_task("Task with special chars: !@#$%^&*()")
        assert isinstance(model, ModelType)
    
    def test_context_size_zero(self):
        """Test routing with zero context size."""
        model = route_task("Task", context_size=0)
        assert isinstance(model, ModelType)
    
    def test_context_size_negative(self):
        """Test routing with negative context size."""
        model = route_task("Task", context_size=-100)
        assert isinstance(model, ModelType)


class TestIntegration:
    """Integration tests for complete workflows."""
    
    def test_complete_routing_workflow(self):
        """Test complete routing workflow."""
        # Step 1: Detect task type
        task_type = detect_task_type("Create docker compose file")
        assert task_type == "terminal"
        
        # Step 2: Route task
        model = route_task("Create docker compose file")
        assert model == ModelType.LAGUNA
        
        # Step 3: Get model info
        info = get_model_info(model)
        assert info["name"] == "Laguna S 2.1 Free"
        
        # Step 4: Get explanation
        explanation = explain_routing("Create docker compose file", model)
        assert "Laguna S 2.1 Free" in explanation
    
    def test_multimodal_workflow(self):
        """Test multimodal task workflow."""
        task_type = detect_task_type("Fix UI bug", has_image=True)
        assert task_type == "multimodal"
        
        model = route_task("Fix UI bug", has_image=True)
        assert model == ModelType.MIMO
        
        info = get_model_info(model)
        assert "Multimodal" in info["strength"]
    
    def test_speed_workflow(self):
        """Test speed-critical task workflow."""
        task_type = detect_task_type("Quick API endpoint")
        assert task_type == "speed"
        
        model = route_task("Quick API endpoint")
        assert model == ModelType.DEEPSEEK
        
        info = get_model_info(model)
        assert "126 tokens/second" in info["speed"]


if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])
