#!/usr/bin/env python3
"""
Tests for AgentCode routing logic.
"""

import pytest
from agentcode import route_task, get_model_info, ModelType


class TestRouteTask:
    """Test the route_task function."""

    def test_multimodal_image(self):
        """Test routing for image tasks."""
        model = route_task("Fix this bug", has_image=True)
        assert model == ModelType.MIMO

    def test_multimodal_audio(self):
        """Test routing for audio tasks."""
        model = route_task("Transcribe this", has_audio=True)
        assert model == ModelType.MIMO

    def test_multimodal_video(self):
        """Test routing for video tasks."""
        model = route_task("Analyze this video", has_video=True)
        assert model == ModelType.MIMO

    def test_terminal_bash(self):
        """Test routing for bash tasks."""
        model = route_task("Create a bash script")
        assert model == ModelType.LAGUNA

    def test_terminal_docker(self):
        """Test routing for docker tasks."""
        model = route_task("Create docker compose file")
        assert model == ModelType.LAGUNA

    def test_terminal_cli(self):
        """Test routing for CLI tasks."""
        model = route_task("Build a CLI tool")
        assert model == ModelType.LAGUNA

    def test_large_context(self):
        """Test routing for large context."""
        model = route_task("Analyze this", context_size=500000)
        assert model == ModelType.NEMOTRON

    def test_local_only(self):
        """Test routing for local-only tasks."""
        model = route_task("Run locally", is_local_only=True)
        assert model == ModelType.NORTH

    def test_budget_conscious(self):
        """Test routing for budget tasks."""
        model = route_task("Process files", is_budget_conscious=True)
        assert model == ModelType.LING

    def test_speed_critical(self):
        """Test routing for speed-critical tasks."""
        model = route_task("Quick code generation")
        assert model == ModelType.DEEPSEEK

    def test_default(self):
        """Test default routing."""
        model = route_task("Write a function")
        assert model == ModelType.BIG_PICKLE


class TestGetModelInfo:
    """Test the get_model_info function."""

    def test_all_models_have_info(self):
        """Test that all models have info."""
        for model in ModelType:
            info = get_model_info(model)
            assert "name" in info
            assert "strength" in info
            assert "context" in info
            assert "speed" in info

    def test_model_names(self):
        """Test model names are correct."""
        assert get_model_info(ModelType.MIMO)["name"] == "MiMo-V2.5 Free"
        assert get_model_info(ModelType.DEEPSEEK)["name"] == "DeepSeek V4 Flash Free"
        assert get_model_info(ModelType.LAGUNA)["name"] == "Laguna S 2.1 Free"
        assert get_model_info(ModelType.LING)["name"] == "Ling-3.0-flash Free"
        assert get_model_info(ModelType.NORTH)["name"] == "North Mini Code Free"
        assert get_model_info(ModelType.NEMOTRON)["name"] == "Nemotron 3 Ultra Free"
        assert get_model_info(ModelType.BIG_PICKLE)["name"] == "Big Pickle"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
