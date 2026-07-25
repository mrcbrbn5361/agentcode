"""
AgentCode v0.0.2 - Session Management

OpenClaw-inspired session management with context preservation,
dynamic model switching, and progress tracking.
"""

import json
import time
import uuid
from pathlib import Path
from typing import Dict, List, Optional, Any
from dataclasses import dataclass, asdict
from datetime import datetime


@dataclass
class SessionContext:
    """Session context information."""
    task_type: str
    language: str
    project_path: str
    files_modified: List[str]
    tests_passed: int
    tests_failed: int
    lines_written: int
    time_spent: float


@dataclass
class Session:
    """Represents a coding session."""
    session_id: str
    created_at: str
    updated_at: str
    model_used: str
    task_description: str
    context: SessionContext
    is_active: bool = True


class SessionManager:
    """Manages coding sessions with persistence and model switching."""
    
    def __init__(self):
        self.sessions_dir = Path.home() / ".agentcode" / "sessions"
        self.sessions_dir.mkdir(parents=True, exist_ok=True)
        self.current_session: Optional[Session] = None
    
    def create_session(self, model: str, task_description: str, language: str = "python") -> Session:
        """Create a new coding session."""
        session_id = str(uuid.uuid4())[:8]
        now = datetime.now().isoformat()
        
        context = SessionContext(
            task_type="coding",
            language=language,
            project_path=str(Path.cwd()),
            files_modified=[],
            tests_passed=0,
            tests_failed=0,
            lines_written=0,
            time_spent=0.0,
        )
        
        session = Session(
            session_id=session_id,
            created_at=now,
            updated_at=now,
            model_used=model,
            task_description=task_description,
            context=context,
        )
        
        self.current_session = session
        self._save_session(session)
        
        return session
    
    def resume_session(self, session_id: str) -> Optional[Session]:
        """Resume an existing session."""
        session_file = self.sessions_dir / f"{session_id}.json"
        if session_file.exists():
            with open(session_file, "r") as f:
                data = json.load(f)
                session = Session(**data)
                self.current_session = session
                return session
        return None
    
    def list_sessions(self, active_only: bool = True) -> List[Dict]:
        """List all sessions."""
        sessions = []
        for session_file in self.sessions_dir.glob("*.json"):
            with open(session_file, "r") as f:
                data = json.load(f)
                if active_only and not data.get("is_active", True):
                    continue
                sessions.append({
                    "session_id": data["session_id"],
                    "created_at": data["created_at"],
                    "model_used": data["model_used"],
                    "task_description": data["task_description"],
                })
        return sessions
    
    def update_session(self, **kwargs):
        """Update current session."""
        if self.current_session:
            for key, value in kwargs.items():
                if hasattr(self.current_session, key):
                    setattr(self.current_session, key, value)
            self.current_session.updated_at = datetime.now().isoformat()
            self._save_session(self.current_session)
    
    def add_modified_file(self, file_path: str):
        """Add a modified file to current session."""
        if self.current_session and self.current_session.context:
            if file_path not in self.current_session.context.files_modified:
                self.current_session.context.files_modified.append(file_path)
                self._save_session(self.current_session)
    
    def update_test_results(self, passed: int, failed: int):
        """Update test results for current session."""
        if self.current_session and self.current_session.context:
            self.current_session.context.tests_passed = passed
            self.current_session.context.tests_failed = failed
            self._save_session(self.current_session)
    
    def add_lines_written(self, lines: int):
        """Add to lines written counter."""
        if self.current_session and self.current_session.context:
            self.current_session.context.lines_written += lines
            self._save_session(self.current_session)
    
    def get_session_stats(self) -> Dict[str, Any]:
        """Get statistics for current session."""
        if not self.current_session:
            return {}
        
        context = self.current_session.context
        return {
            "session_id": self.current_session.session_id,
            "model_used": self.current_session.model_used,
            "task": self.current_session.task_description,
            "language": context.language,
            "files_modified": len(context.files_modified),
            "tests_passed": context.tests_passed,
            "tests_failed": context.tests_failed,
            "lines_written": context.lines_written,
            "time_spent": context.time_spent,
        }
    
    def _save_session(self, session: Session):
        """Save session to file."""
        session_file = self.sessions_dir / f"{session.session_id}.json"
        with open(session_file, "w") as f:
            json.dump(asdict(session), f, indent=2)
    
    def close_session(self):
        """Close current session."""
        if self.current_session:
            self.current_session.is_active = False
            self._save_session(self.current_session)
            self.current_session = None


class ModelSwitcher:
    """Dynamic model switching during session."""
    
    def __init__(self):
        self.available_models = {
            "mimo": "MiMo-V2.5",
            "deepseek": "DeepSeek V4 Flash",
            "laguna": "Laguna S 2.1",
            "ling": "Ling-3.0-flash",
            "north": "North Mini Code",
            "nemotron": "Nemotron 3 Ultra",
            "bigpickle": "Big Pickle",
        }
        self.current_model = "mimo"
        self.model_history = []
    
    def list_models(self) -> Dict[str, str]:
        """List available models."""
        return self.available_models.copy()
    
    def switch_model(self, model_id: str) -> bool:
        """Switch to a different model."""
        if model_id in self.available_models:
            self.model_history.append(self.current_model)
            self.current_model = model_id
            return True
        return False
    
    def get_current_model(self) -> str:
        """Get current model ID."""
        return self.current_model
    
    def get_model_name(self, model_id: str) -> str:
        """Get model name by ID."""
        return self.available_models.get(model_id, "Unknown")
    
    def revert_model(self) -> bool:
        """Revert to previous model."""
        if self.model_history:
            self.current_model = self.model_history.pop()
            return True
        return False


class ProgressTracker:
    """Track coding progress and metrics."""
    
    def __init__(self):
        self.metrics = {
            "tasks_completed": 0,
            "lines_written": 0,
            "tests_passing": 0,
            "tests_failing": 0,
            "files_modified": 0,
            "models_used": {},
            "time_start": time.time(),
        }
    
    def task_completed(self, model: str):
        """Record task completion."""
        self.metrics["tasks_completed"] += 1
        self.metrics["models_used"][model] = self.metrics["models_used"].get(model, 0) + 1
    
    def add_lines(self, count: int):
        """Add lines written."""
        self.metrics["lines_written"] += count
    
    def update_tests(self, passing: int, failing: int):
        """Update test counts."""
        self.metrics["tests_passing"] = passing
        self.metrics["tests_failing"] = failing
    
    def file_modified(self):
        """Record file modification."""
        self.metrics["files_modified"] += 1
    
    def get_stats(self) -> Dict[str, Any]:
        """Get current statistics."""
        elapsed = time.time() - self.metrics["time_start"]
        hours = int(elapsed // 3600)
        minutes = int((elapsed % 3600) // 60)
        
        return {
            "tasks_completed": self.metrics["tasks_completed"],
            "lines_written": self.metrics["lines_written"],
            "tests_passing": self.metrics["tests_passing"],
            "tests_failing": self.metrics["tests_failing"],
            "files_modified": self.metrics["files_modified"],
            "models_used": self.metrics["models_used"],
            "total_time": f"{hours}h {minutes}m",
        }
    
    def print_stats(self):
        """Print formatted statistics."""
        stats = self.get_stats()
        print("\n" + "="*50)
        print("Session Statistics")
        print("="*50)
        print(f"Tasks completed: {stats['tasks_completed']}")
        print(f"Lines written: {stats['lines_written']}")
        print(f"Tests: {stats['tests_passing']} passing, {stats['tests_failing']} failing")
        print(f"Files modified: {stats['files_modified']}")
        print(f"Total time: {stats['total_time']}")
        
        if stats["models_used"]:
            print("\nModels used:")
            for model, count in stats["models_used"].items():
                print(f"  {model}: {count} tasks")
        print("="*50 + "\n")


def get_session_manager() -> SessionManager:
    """Get session manager instance."""
    return SessionManager()


def get_model_switcher() -> ModelSwitcher:
    """Get model switcher instance."""
    return ModelSwitcher()


def get_progress_tracker() -> ProgressTracker:
    """Get progress tracker instance."""
    return ProgressTracker()