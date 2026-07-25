"""
AgentCode v0.0.2 Test Suite

Comprehensive tests for system detection, wizard, sessions, and languages.
"""

import pytest
import json
import tempfile
from pathlib import Path
from unittest.mock import patch, MagicMock

from agentcode import route_task, get_model_info, ModelType
from detector import SystemDetector, DetectedModel, ModelCategory, detect_system_models
from wizard import SelectionWizard, UserPreferences, UserPriority, load_config
from sessions import SessionManager, ModelSwitcher, ProgressTracker
from languages import (
    LanguageDetector,
    CodeTemplateGenerator,
    LinterIntegrator,
    ProgrammingLanguage,
    detect_project_language,
    get_language_template,
    get_supported_languages,
)


# AgentCode Core Tests

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


# System Detection Tests

def test_system_detector_initialization():
    """Test system detector initialization."""
    detector = SystemDetector()
    assert detector.detected_models == []
    assert "platform" in detector.system_info


def test_detect_all():
    """Test detect_all method."""
    detector = SystemDetector()
    models = detector.detect_all()
    assert isinstance(models, list)


def test_get_models_by_category():
    """Test get_models_by_category method."""
    detector = SystemDetector()
    detector.detect_all()
    
    cli_models = detector.get_models_by_category(ModelCategory.CLI)
    assert isinstance(cli_models, list)
    
    ide_models = detector.get_models_by_category(ModelCategory.IDE)
    assert isinstance(ide_models, list)


def test_get_summary():
    """Test get_summary method."""
    detector = SystemDetector()
    detector.detect_all()
    summary = detector.get_summary()
    
    assert "total" in summary
    assert "by_category" in summary
    assert isinstance(summary["total"], int)


def test_detect_system_models():
    """Test detect_system_models convenience function."""
    models = detect_system_models()
    assert isinstance(models, list)


def test_detected_model_creation():
    """Test DetectedModel creation."""
    model = DetectedModel(
        name="Test Model",
        category=ModelCategory.CLI,
        source="test",
        version="1.0.0",
        capabilities=["test"],
    )
    
    assert model.name == "Test Model"
    assert model.category == ModelCategory.CLI
    assert model.source == "test"
    assert model.version == "1.0.0"
    assert model.capabilities == ["test"]
    assert model.is_available is True


# Wizard Tests

def test_user_preferences_creation():
    """Test UserPreferences creation."""
    prefs = UserPreferences(
        primary_model="mimo",
        fallback_models=["deepseek", "laguna"],
        terminal_model="laguna",
        multimodal_model="mimo",
        local_model="north",
        priority=UserPriority.SPEED,
        privacy_mode=False,
        auto_fallback=True,
    )
    
    assert prefs.primary_model == "mimo"
    assert prefs.fallback_models == ["deepseek", "laguna"]
    assert prefs.terminal_model == "laguna"
    assert prefs.multimodal_model == "mimo"
    assert prefs.local_model == "north"
    assert prefs.priority == UserPriority.SPEED
    assert prefs.privacy_mode is False
    assert prefs.auto_fallback is True


def test_selection_wizard_initialization():
    """Test SelectionWizard initialization."""
    wizard = SelectionWizard()
    assert wizard.detected_models == []
    assert wizard.user_preferences is None


def test_prepare_model_options():
    """Test _prepare_model_options method."""
    wizard = SelectionWizard()
    wizard.detected_models = [
        DetectedModel(
            name="Test CLI",
            category=ModelCategory.CLI,
            source="test-cli",
        )
    ]
    
    options = wizard._prepare_model_options()
    assert "primary" in options
    assert "fallback" in options
    assert "terminal" in options
    assert "multimodal" in options
    assert "local" in options


def test_load_config():
    """Test load_config function."""
    # Test with non-existent config
    with patch("wizard.Path.home") as mock_home:
        mock_home.return_value = Path("/tmp/nonexistent")
        config = load_config()
        assert config is None


# Session Tests

def test_session_manager_initialization():
    """Test SessionManager initialization."""
    with tempfile.TemporaryDirectory() as tmpdir:
        manager = SessionManager()
        manager.sessions_dir = Path(tmpdir)
        assert manager.sessions_dir == Path(tmpdir)
        assert manager.current_session is None


def test_model_switcher():
    """Test ModelSwitcher functionality."""
    switcher = ModelSwitcher()
    
    # Test initial model
    assert switcher.get_current_model() == "mimo"
    
    # Test model switching
    assert switcher.switch_model("deepseek") is True
    assert switcher.get_current_model() == "deepseek"
    
    # Test model listing
    models = switcher.list_models()
    assert "mimo" in models
    assert "deepseek" in models
    
    # Test revert
    assert switcher.revert_model() is True
    assert switcher.get_current_model() == "mimo"


def test_progress_tracker():
    """Test ProgressTracker functionality."""
    tracker = ProgressTracker()
    
    # Test initial stats
    stats = tracker.get_stats()
    assert stats["tasks_completed"] == 0
    assert stats["lines_written"] == 0
    
    # Test updates
    tracker.task_completed("mimo")
    tracker.add_lines(100)
    tracker.update_tests(10, 1)
    
    stats = tracker.get_stats()
    assert stats["tasks_completed"] == 1
    assert stats["lines_written"] == 100
    assert stats["tests_passing"] == 10
    assert stats["tests_failing"] == 1


# Language Tests

def test_language_detector_initialization():
    """Test LanguageDetector initialization."""
    detector = LanguageDetector()
    assert detector.project_path == Path(".")


def test_detect_language():
    """Test detect_language method."""
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create a Python project
        (Path(tmpdir) / "requirements.txt").touch()
        (Path(tmpdir) / "main.py").touch()
        
        detector = LanguageDetector(tmpdir)
        lang = detector.detect_language()
        
        # Should detect Python
        assert lang == ProgrammingLanguage.PYTHON


def test_detect_all_languages():
    """Test detect_all_languages method."""
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create a mixed project
        (Path(tmpdir) / "requirements.txt").touch()
        (Path(tmpdir) / "main.py").touch()
        (Path(tmpdir) / "app.js").touch()
        (Path(tmpdir) / "package.json").touch()
        
        detector = LanguageDetector(tmpdir)
        languages = detector.detect_all_languages()
        
        assert ProgrammingLanguage.PYTHON in languages
        assert ProgrammingLanguage.JAVASCRIPT in languages


def test_code_template_generator():
    """Test CodeTemplateGenerator functionality."""
    generator = CodeTemplateGenerator()
    
    # Test Python template
    template = generator.generate_template(
        ProgrammingLanguage.PYTHON,
        "function",
        name="test_func",
        params="x, y",
        docstring="Test function",
    )
    
    assert "def test_func(x, y):" in template
    assert "Test function" in template


def test_get_language_template():
    """Test get_language_template convenience function."""
    template = get_language_template(
        ProgrammingLanguage.JAVASCRIPT,
        "function",
        name="myFunc",
        params="a, b",
        docstring="My function",
    )
    
    assert "function myFunc(a, b)" in template


def test_linter_integrator():
    """Test LinterIntegrator functionality."""
    with tempfile.TemporaryDirectory() as tmpdir:
        integrator = LinterIntegrator(tmpdir)
        
        # Test Python linters
        linters = integrator.detect_linters(ProgrammingLanguage.PYTHON)
        assert isinstance(linters, dict)
        
        # Test formatters
        formatters = integrator.detect_formatters(ProgrammingLanguage.PYTHON)
        assert isinstance(formatters, dict)


def test_get_supported_languages():
    """Test get_supported_languages function."""
    languages = get_supported_languages()
    assert isinstance(languages, list)
    assert len(languages) > 0
    
    # Check structure
    for lang in languages:
        assert "id" in lang
        assert "name" in lang
        assert "expert_model" in lang


def test_programming_language_enum():
    """Test ProgrammingLanguage enum."""
    assert ProgrammingLanguage.PYTHON.value == "python"
    assert ProgrammingLanguage.JAVASCRIPT.value == "javascript"
    assert ProgrammingLanguage.GO.value == "go"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])