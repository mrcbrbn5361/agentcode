"""
AgentCode v0.0.2 - User Preference Selection System

Interactive wizard for selecting AI models based on detected system capabilities
and user preferences with intelligent recommendations.
"""

import json
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
from enum import Enum

from detector import DetectedModel, ModelCategory, detect_system_models


class UserPriority(str, Enum):
    """User priority for model selection."""
    SPEED = "speed"
    ACCURACY = "accuracy"
    PRIVACY = "privacy"
    COST = "cost"
    CODING = "coding"


@dataclass
class UserPreferences:
    """User's model preferences."""
    primary_model: str
    fallback_models: List[str]
    terminal_model: str
    multimodal_model: str
    local_model: str
    priority: UserPriority
    privacy_mode: bool
    auto_fallback: bool


class SelectionWizard:
    """Interactive model selection wizard."""
    
    def __init__(self):
        self.detected_models: List[DetectedModel] = []
        self.user_preferences: Optional[UserPreferences] = None
        self.config_path = Path.home() / ".agentcode" / "config.json"
    
    def run_wizard(self) -> UserPreferences:
        """Run the interactive selection wizard."""
        print("\n" + "="*60)
        print("AgentCode Model Selection Wizard")
        print("="*60 + "\n")
        
        # Step 1: Detect system models
        print("Step 1: Scanning your system for AI models...")
        self.detected_models = detect_system_models()
        self._print_detection_summary()
        
        # Step 2: Select priority
        print("\nStep 2: What's your priority?")
        priority = self._select_priority()
        
        # Step 3: Select models
        print("\nStep 3: Select models for AgentCode to use:")
        selected_models = self._select_models()
        
        # Step 4: Configure preferences
        print("\nStep 4: Configure preferences:")
        preferences = self._configure_preferences(priority, selected_models)
        
        # Step 5: Save configuration
        print("\nStep 5: Saving configuration...")
        self._save_config(preferences)
        
        print("\n✓ Configuration saved successfully!")
        print(f"  Config file: {self.config_path}")
        
        return preferences
    
    def _print_detection_summary(self):
        """Print summary of detected models."""
        detector_summary = {}
        for model in self.detected_models:
            category = model.category.value
            if category not in detector_summary:
                detector_summary[category] = []
            detector_summary[category].append(model.name)
        
        print(f"\nFound {len(self.detected_models)} AI models on your system:\n")
        
        for category, models in detector_summary.items():
            if models:
                print(f"\n{category.upper()} ({len(models)} found):")
                for model in models:
                    print(f"  ✓ {model}")
    
    def _select_priority(self) -> UserPriority:
        """Select user priority."""
        priorities = [
            ("1", "Speed", "Fastest response times"),
            ("2", "Accuracy", "Best code quality"),
            ("3", "Privacy", "Local processing only"),
            ("4", "Cost", "Free models only"),
            ("5", "Coding", "Best for programming tasks"),
        ]
        
        print("\nAvailable priorities:")
        for num, name, desc in priorities:
            print(f"  [{num}] {name} - {desc}")
        
        while True:
            choice = input("\nEnter your choice (1-5): ").strip()
            if choice in ["1", "2", "3", "4", "5"]:
                priority_map = {
                    "1": UserPriority.SPEED,
                    "2": UserPriority.ACCURACY,
                    "3": UserPriority.PRIVACY,
                    "4": UserPriority.COST,
                    "5": UserPriority.CODING,
                }
                return priority_map[choice]
            print("Invalid choice. Please enter 1-5.")
    
    def _select_models(self) -> Dict[str, str]:
        """Select models for different purposes."""
        # Prepare model options based on detection
        model_options = self._prepare_model_options()
        
        selected = {}
        
        # Select primary model
        print("\nAvailable primary models:")
        for i, (model_id, model_info) in enumerate(model_options["primary"].items(), 1):
            print(f"  [{i}] {model_info['name']} - {model_info['description']}")
        
        while True:
            choice = input("\nSelect primary model (number): ").strip()
            try:
                idx = int(choice) - 1
                model_ids = list(model_options["primary"].keys())
                if 0 <= idx < len(model_ids):
                    selected["primary"] = model_ids[idx]
                    break
            except ValueError:
                pass
            print("Invalid choice. Please enter a number.")
        
        # Select fallback models
        print("\nAvailable fallback models:")
        for i, (model_id, model_info) in enumerate(model_options["fallback"].items(), 1):
            print(f"  [{i}] {model_info['name']} - {model_info['description']}")
        
        while True:
            choices = input("\nSelect fallback models (comma-separated numbers): ").strip()
            try:
                indices = [int(x.strip()) - 1 for x in choices.split(",")]
                model_ids = list(model_options["fallback"].keys())
                selected_fallback = []
                for idx in indices:
                    if 0 <= idx < len(model_ids):
                        selected_fallback.append(model_ids[idx])
                if selected_fallback:
                    selected["fallback"] = selected_fallback
                    break
            except ValueError:
                pass
            print("Invalid choices. Please enter comma-separated numbers.")
        
        # Select terminal model
        print("\nAvailable terminal models:")
        for i, (model_id, model_info) in enumerate(model_options["terminal"].items(), 1):
            print(f"  [{i}] {model_info['name']} - {model_info['description']}")
        
        while True:
            choice = input("\nSelect terminal model (number): ").strip()
            try:
                idx = int(choice) - 1
                model_ids = list(model_options["terminal"].keys())
                if 0 <= idx < len(model_ids):
                    selected["terminal"] = model_ids[idx]
                    break
            except ValueError:
                pass
            print("Invalid choice. Please enter a number.")
        
        # Select multimodal model
        print("\nAvailable multimodal models:")
        for i, (model_id, model_info) in enumerate(model_options["multimodal"].items(), 1):
            print(f"  [{i}] {model_info['name']} - {model_info['description']}")
        
        while True:
            choice = input("\nSelect multimodal model (number): ").strip()
            try:
                idx = int(choice) - 1
                model_ids = list(model_options["multimodal"].keys())
                if 0 <= idx < len(model_ids):
                    selected["multimodal"] = model_ids[idx]
                    break
            except ValueError:
                pass
            print("Invalid choice. Please enter a number.")
        
        # Select local model (optional)
        if model_options["local"]:
            print("\nAvailable local models:")
            for i, (model_id, model_info) in enumerate(model_options["local"].items(), 1):
                print(f"  [{i}] {model_info['name']} - {model_info['description']}")
            
            choice = input("\nSelect local model (number, or press Enter to skip): ").strip()
            if choice:
                try:
                    idx = int(choice) - 1
                    model_ids = list(model_options["local"].keys())
                    if 0 <= idx < len(model_ids):
                        selected["local"] = model_ids[idx]
                except ValueError:
                    pass
        
        return selected
    
    def _prepare_model_options(self) -> Dict[str, Dict]:
        """Prepare model options for selection."""
        # AgentCode's 7 free models
        agentcode_models = {
            "mimo": {
                "name": "MiMo-V2.5",
                "description": "Best Overall (10/10) - Multimodal, 1M context",
                "category": "primary",
            },
            "deepseek": {
                "name": "DeepSeek V4 Flash",
                "description": "Fastest (126 tok/s) - Speed critical tasks",
                "category": "fallback",
            },
            "laguna": {
                "name": "Laguna S 2.1",
                "description": "Terminal Expert (70.2% TerminalBench)",
                "category": "terminal",
            },
            "ling": {
                "name": "Ling-3.0-flash",
                "description": "Token Efficient - Cost optimization",
                "category": "fallback",
            },
            "north": {
                "name": "North Mini Code",
                "description": "Local/Private - Sovereign AI",
                "category": "local",
            },
            "nemotron": {
                "name": "Nemotron 3 Ultra",
                "description": "Enterprise (550B) - Maximum accuracy",
                "category": "primary",
            },
            "bigpickle": {
                "name": "Big Pickle",
                "description": "Stealth Daily - Privacy focused",
                "category": "local",
            },
        }
        
        # Add detected system models as options
        detected_options = {}
        for model in self.detected_models:
            detected_options[model.source] = {
                "name": model.name,
                "description": f"Detected {model.category.value} model",
                "category": model.category.value,
            }
        
        # Combine and categorize
        options = {
            "primary": {},
            "fallback": {},
            "terminal": {},
            "multimodal": {},
            "local": {},
        }
        
        for model_id, model_info in agentcode_models.items():
            category = model_info["category"]
            if category in options:
                options[category][model_id] = model_info
        
        # Add detected models
        for model_id, model_info in detected_options.items():
            if "cli" in model_id.lower():
                options["fallback"][model_id] = model_info
            elif "ide" in model_id.lower():
                options["fallback"][model_id] = model_info
            elif "cloud" in model_id.lower():
                options["primary"][model_id] = model_info
            elif "local" in model_id.lower():
                options["local"][model_id] = model_info
        
        return options
    
    def _configure_preferences(self, priority: UserPriority, selected_models: Dict[str, str]) -> UserPreferences:
        """Configure additional preferences."""
        # Privacy mode
        privacy_choice = input("\nEnable privacy mode? (y/n, default: n): ").strip().lower()
        privacy_mode = privacy_choice in ["y", "yes"]
        
        # Auto fallback
        fallback_choice = input("Enable automatic model fallback? (y/n, default: y): ").strip().lower()
        auto_fallback = fallback_choice not in ["n", "no"]
        
        return UserPreferences(
            primary_model=selected_models.get("primary", "mimo"),
            fallback_models=selected_models.get("fallback", ["deepseek", "laguna"]),
            terminal_model=selected_models.get("terminal", "laguna"),
            multimodal_model=selected_models.get("multimodal", "mimo"),
            local_model=selected_models.get("local", ""),
            priority=priority,
            privacy_mode=privacy_mode,
            auto_fallback=auto_fallback,
        )
    
    def _save_config(self, preferences: UserPreferences):
        """Save configuration to file."""
        config = {
            "version": "0.0.2",
            "selected_models": {
                "primary": preferences.primary_model,
                "fallback": preferences.fallback_models,
                "terminal": preferences.terminal_model,
                "multimodal": preferences.multimodal_model,
                "local": preferences.local_model,
            },
            "detected_systems": {
                "cli": [m.source for m in self.detected_models if m.category == ModelCategory.CLI],
                "ide": [m.source for m in self.detected_models if m.category == ModelCategory.IDE],
                "cloud": [m.source for m in self.detected_models if m.category == ModelCategory.CLOUD],
                "local": [m.source for m in self.detected_models if m.category == ModelCategory.LOCAL],
            },
            "user_preferences": {
                "priority": preferences.priority.value,
                "privacy_mode": preferences.privacy_mode,
                "auto_fallback": preferences.auto_fallback,
            },
        }
        
        # Create config directory if it doesn't exist
        self.config_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Save config
        with open(self.config_path, "w") as f:
            json.dump(config, f, indent=2)


def load_config() -> Optional[Dict]:
    """Load configuration from file."""
    config_path = Path.home() / ".agentcode" / "config.json"
    if config_path.exists():
        with open(config_path, "r") as f:
            return json.load(f)
    return None


def get_selected_models() -> Dict[str, str]:
    """Get currently selected models from config."""
    config = load_config()
    if config and "selected_models" in config:
        return config["selected_models"]
    return {}


def run_setup_wizard() -> UserPreferences:
    """Run the setup wizard."""
    wizard = SelectionWizard()
    return wizard.run_wizard()


if __name__ == "__main__":
    run_setup_wizard()