"""
AgentCode v0.0.2 - Multi-Language Support

Language detection, templates, and linter integration for all major programming languages.
"""

import os
import re
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
from enum import Enum


class ProgrammingLanguage(str, Enum):
    """Supported programming languages."""
    PYTHON = "python"
    JAVASCRIPT = "javascript"
    TYPESCRIPT = "typescript"
    GO = "go"
    RUST = "rust"
    JAVA = "java"
    CSHARP = "csharp"
    CPP = "cpp"
    PHP = "php"
    RUBY = "ruby"
    SWIFT = "swift"
    KOTLIN = "kotlin"
    SCALA = "scala"
    SHELL = "shell"


@dataclass
class LanguageInfo:
    """Information about a programming language."""
    name: str
    extensions: List[str]
    config_files: List[str]
    expert_model: str
    linters: List[str]
    formatters: List[str]


# Language configurations
LANGUAGE_CONFIGS: Dict[ProgrammingLanguage, LanguageInfo] = {
    ProgrammingLanguage.PYTHON: LanguageInfo(
        name="Python",
        extensions=[".py"],
        config_files=["requirements.txt", "setup.py", "pyproject.toml", "Pipfile"],
        expert_model="mimo",
        linters=["flake8", "pylint", "mypy", "ruff"],
        formatters=["black", "autopep8", "yapf"],
    ),
    ProgrammingLanguage.JAVASCRIPT: LanguageInfo(
        name="JavaScript",
        extensions=[".js", ".jsx", ".mjs"],
        config_files=["package.json", ".eslintrc", ".eslintrc.js", ".babelrc"],
        expert_model="mimo",
        linters=["eslint", "jshint"],
        formatters=["prettier"],
    ),
    ProgrammingLanguage.TYPESCRIPT: LanguageInfo(
        name="TypeScript",
        extensions=[".ts", ".tsx", ".mts"],
        config_files=["tsconfig.json", "package.json", ".eslintrc"],
        expert_model="mimo",
        linters=["tsc", "eslint"],
        formatters=["prettier"],
    ),
    ProgrammingLanguage.GO: LanguageInfo(
        name="Go",
        extensions=[".go"],
        config_files=["go.mod", "go.sum", "Makefile"],
        expert_model="laguna",
        linters=["golangci-lint", "go vet"],
        formatters=["gofmt", "goimports"],
    ),
    ProgrammingLanguage.RUST: LanguageInfo(
        name="Rust",
        extensions=[".rs"],
        config_files=["Cargo.toml", "Cargo.lock"],
        expert_model="laguna",
        linters=["clippy"],
        formatters=["rustfmt"],
    ),
    ProgrammingLanguage.JAVA: LanguageInfo(
        name="Java",
        extensions=[".java"],
        config_files=["pom.xml", "build.gradle", "build.gradle.kts"],
        expert_model="nemotron",
        linters=["checkstyle", "spotbugs", "pmd"],
        formatters=["google-java-format"],
    ),
    ProgrammingLanguage.CSHARP: LanguageInfo(
        name="C#",
        extensions=[".cs", ".csx"],
        config_files=["*.csproj", "*.sln", "Directory.Build.props"],
        expert_model="nemotron",
        linters=["dotnet format"],
        formatters=["dotnet format"],
    ),
    ProgrammingLanguage.CPP: LanguageInfo(
        name="C++",
        extensions=[".cpp", ".cc", ".cxx", ".h", ".hpp"],
        config_files=["CMakeLists.txt", "Makefile", "meson.build"],
        expert_model="laguna",
        linters=["cppcheck", "clang-tidy"],
        formatters=["clang-format"],
    ),
    ProgrammingLanguage.PHP: LanguageInfo(
        name="PHP",
        extensions=[".php"],
        config_files=["composer.json", "composer.lock", "phpunit.xml"],
        expert_model="ling",
        linters=["phpcs", "phpstan", "psalm"],
        formatters=["php-cs-fixer", "phpcbf"],
    ),
    ProgrammingLanguage.RUBY: LanguageInfo(
        name="Ruby",
        extensions=[".rb", ".rake"],
        config_files=["Gemfile", "Gemfile.lock", ".rubocop.yml"],
        expert_model="ling",
        linters=["rubocop"],
        formatters=["rubocop"],
    ),
    ProgrammingLanguage.SWIFT: LanguageInfo(
        name="Swift",
        extensions=[".swift"],
        config_files=["Package.swift", "Cartfile", "Podfile"],
        expert_model="mimo",
        linters=["swiftlint"],
        formatters=["swiftformat"],
    ),
    ProgrammingLanguage.KOTLIN: LanguageInfo(
        name="Kotlin",
        extensions=[".kt", ".kts"],
        config_files=["build.gradle.kts", "pom.xml"],
        expert_model="mimo",
        linters=["ktlint", "detekt"],
        formatters=["ktlint"],
    ),
    ProgrammingLanguage.SCALA: LanguageInfo(
        name="Scala",
        extensions=[".scala", ".sc"],
        config_files=["build.sbt", "project/build.properties"],
        expert_model="nemotron",
        linters=["scalastyle", "scalafix"],
        formatters=["scalafmt"],
    ),
    ProgrammingLanguage.SHELL: LanguageInfo(
        name="Shell",
        extensions=[".sh", ".bash", ".zsh"],
        config_files=[],
        expert_model="laguna",
        linters=["shellcheck"],
        formatters=["shfmt"],
    ),
}


class LanguageDetector:
    """Detects programming language of a project."""
    
    def __init__(self, project_path: str = "."):
        self.project_path = Path(project_path)
    
    def detect_language(self) -> Optional[ProgrammingLanguage]:
        """Detect primary language of project."""
        language_scores = {}
        
        for lang, info in LANGUAGE_CONFIGS.items():
            score = self._calculate_language_score(lang, info)
            if score > 0:
                language_scores[lang] = score
        
        if language_scores:
            return max(language_scores, key=language_scores.get)
        return None
    
    def detect_all_languages(self) -> List[ProgrammingLanguage]:
        """Detect all languages used in project."""
        detected = []
        
        for lang, info in LANGUAGE_CONFIGS.items():
            score = self._calculate_language_score(lang, info)
            if score > 0:
                detected.append(lang)
        
        return detected
    
    def _calculate_language_score(self, lang: ProgrammingLanguage, info: LanguageInfo) -> int:
        """Calculate score for a language based on project files."""
        score = 0
        
        # Check for config files
        for config_file in info.config_files:
            if "*" in config_file:
                # Glob pattern
                matches = list(self.project_path.glob(config_file))
                score += len(matches) * 10
            else:
                if (self.project_path / config_file).exists():
                    score += 10
        
        # Check for file extensions
        for ext in info.extensions:
            files = list(self.project_path.glob(f"*{ext}"))
            score += len(files)
        
        return score
    
    def get_language_info(self, lang: ProgrammingLanguage) -> LanguageInfo:
        """Get information about a language."""
        return LANGUAGE_CONFIGS.get(lang)


class CodeTemplateGenerator:
    """Generates code templates for different languages."""
    
    def __init__(self):
        self.templates = self._load_templates()
    
    def _load_templates(self) -> Dict[ProgrammingLanguage, Dict[str, str]]:
        """Load code templates for all languages."""
        return {
            ProgrammingLanguage.PYTHON: {
                "function": 'def {name}({params}):\n    """{docstring}"""\n    pass',
                "class": 'class {name}:\n    def __init__(self{params}):\n        pass',
                "test": 'import pytest\n\ndef test_{name}():\n    assert {name}() == expected',
                "async_function": 'async def {name}({params}):\n    """{docstring}"""\n    pass',
            },
            ProgrammingLanguage.JAVASCRIPT: {
                "function": 'function {name}({params}) {{\n  // {docstring}\n}}',
                "class": 'class {name} {{\n  constructor({params}) {{\n  }}\n}}',
                "test": 'describe("{name}", () => {{\n  it("should work", () => {{\n    expect({name}()).toBe(expected);\n  }});\n}});',
                "arrow_function": 'const {name} = ({params}) => {{\n  // {docstring}\n}};',
            },
            ProgrammingLanguage.TYPESCRIPT: {
                "function": 'function {name}({params}): {return_type} {\n  // {docstring}\n}',
                "interface": 'interface {name} {\n  {fields}\n}',
                "test": 'describe("{name}", () => {\n  it("should work", () => {\n    expect({name}()).toBe(expected);\n  });\n});',
                "type": 'type {name} = {\n  {fields}\n};',
            },
            ProgrammingLanguage.GO: {
                "function": 'func {name}({params}) {return_type} {\n\t// {docstring}\n}',
                "struct": 'type {name} struct {\n\t{fields}\n}',
                "test": 'func Test{name}(t *testing.T) {\n\t// {docstring}\n}',
                "interface": 'type {name} interface {\n\t{methods}\n}',
            },
            ProgrammingLanguage.RUST: {
                "function": 'fn {name}({params}) -> {return_type} {\n    // {docstring}\n}',
                "struct": 'struct {name} {\n    {fields}\n}',
                "test": '#[cfg(test)]\nmod tests {\n    use super::*;\n\n    #[test]\n    fn test_{name}() {\n        // {docstring}\n    }\n}',
                "impl": 'impl {name} {\n    {methods}\n}',
            },
            ProgrammingLanguage.JAVA: {
                "function": 'public {return_type} {name}({params}) {\n    // {docstring}\n}',
                "class": 'public class {name} {\n    public {name}({params}) {\n    }\n}',
                "test": '@Test\npublic void test_{name}() {\n    // {docstring}\n}',
                "interface": 'public interface {name} {\n    {methods}\n}',
            },
            ProgrammingLanguage.CSHARP: {
                "function": 'public {return_type} {name}({params}) {\n    // {docstring}\n}',
                "class": 'public class {name} {\n    public {name}({params}) {\n    }\n}',
                "test": '[Test]\npublic void Test_{name}() {\n    // {docstring}\n}',
                "interface": 'public interface {name} {\n    {methods}\n}',
            },
            ProgrammingLanguage.CPP: {
                "function": '{return_type} {name}({params}) {\n    // {docstring}\n}',
                "class": 'class {name} {\npublic:\n    {name}({params});\n};',
                "test": 'TEST({name}, should_work) {\n    // {docstring}\n}',
                "header": '#pragma once\n\n#include <string>\n\nclass {name} {\npublic:\n    {name}({params});\n};',
            },
            ProgrammingLanguage.PHP: {
                "function": '<?php\n\nfunction {name}({params}) {\n    // {docstring}\n}',
                "class": '<?php\n\nclass {name} {\n    public function __construct({params}) {\n    }\n}',
                "test": '<?php\n\nuse PHPUnit\\Framework\\TestCase;\n\nclass {name}Test extends TestCase {\n    public function test_{name}() {\n        // {docstring}\n    }\n}',
            },
            ProgrammingLanguage.RUBY: {
                "function": 'def {name}({params})\n  # {docstring}\nend',
                "class": 'class {name}\n  def initialize({params})\n  end\nend',
                "test": "require 'test_helper'\n\nclass {name}Test < Minitest::Test\n  def test_{name}\n    # {docstring}\n  end\nend",
                "module": 'module {name}\n  # {docstring}\nend',
            },
            ProgrammingLanguage.SWIFT: {
                "function": 'func {name}({params}) -> {return_type} {\n    // {docstring}\n}',
                "class": 'class {name} {\n    init({params}) {\n    }\n}',
                "test": 'import XCTest\n\nclass {name}Tests: XCTestCase {\n    func test_{name}() {\n        // {docstring}\n    }\n}',
                "struct": 'struct {name} {\n    {fields}\n}',
            },
            ProgrammingLanguage.KOTLIN: {
                "function": 'fun {name}({params}): {return_type} {\n    // {docstring}\n}',
                "class": 'class {name}({params}) {\n}',
                "test": 'import org.junit.Test\n\nclass {name}Test {\n    @Test\n    fun test_{name}() {\n        // {docstring}\n    }\n}',
                "interface": 'interface {name} {\n    {methods}\n}',
            },
            ProgrammingLanguage.SCALA: {
                "function": 'def {name}({params}): {return_type} = {\n    // {docstring}\n}',
                "class": 'class {name}({params}) {\n}',
                "test": 'import org.scalatest.funsuite.AnyFunSuite\n\nclass {name}Test extends AnyFunSuite {\n  test("{name}") {\n    // {docstring}\n  }\n}',
                "trait": 'trait {name} {\n  {methods}\n}',
            },
            ProgrammingLanguage.SHELL: {
                "function": '{name}() {\n    # {docstring}\n}',
                "script": '#!/bin/bash\n\n# {docstring}\n',
                "test": '#!/bin/bash\n\n# Test {name}\nassert() {\n    if [ "$1" != "$2" ]; then\n        echo "FAIL: $1 != $2"\n        exit 1\n    fi\n}',
            },
        }
    
    def generate_template(self, lang: ProgrammingLanguage, template_type: str, **kwargs) -> str:
        """Generate a code template."""
        if lang in self.templates and template_type in self.templates[lang]:
            template = self.templates[lang][template_type]
            return template.format(**kwargs)
        return ""


class LinterIntegrator:
    """Integrates with project linters and formatters."""
    
    def __init__(self, project_path: str = "."):
        self.project_path = Path(project_path)
    
    def detect_linters(self, lang: ProgrammingLanguage) -> Dict[str, bool]:
        """Detect available linters for a language."""
        lang_info = LANGUAGE_CONFIGS.get(lang)
        if not lang_info:
            return {}
        
        detected = {}
        for linter in lang_info.linters:
            detected[linter] = self._is_linter_available(linter)
        
        return detected
    
    def detect_formatters(self, lang: ProgrammingLanguage) -> Dict[str, bool]:
        """Detect available formatters for a language."""
        lang_info = LANGUAGE_CONFIGS.get(lang)
        if not lang_info:
            return {}
        
        detected = {}
        for formatter in lang_info.formatters:
            detected[formatter] = self._is_linter_available(formatter)
        
        return detected
    
    def _is_linter_available(self, tool: str) -> bool:
        """Check if a linter/formatter is available."""
        import shutil
        return shutil.which(tool) is not None
    
    def get_linter_config(self, lang: ProgrammingLanguage) -> Optional[Dict]:
        """Get linter configuration for a language."""
        lang_info = LANGUAGE_CONFIGS.get(lang)
        if not lang_info:
            return None
        
        # Check for common config files
        config_files = {
            "python": ["pyproject.toml", "setup.cfg", ".flake8", "mypy.ini"],
            "javascript": [".eslintrc", ".eslintrc.js", ".eslintrc.json"],
            "typescript": ["tsconfig.json", ".eslintrc"],
            "go": [".golangci.yml"],
            "rust": ["rustfmt.toml", ".rustfmt.toml"],
            "java": ["checkstyle.xml", "pom.xml"],
            "cpp": [".clang-format", "CMakeLists.txt"],
        }
        
        if lang.value in config_files:
            for config_file in config_files[lang.value]:
                config_path = self.project_path / config_file
                if config_path.exists():
                    return {"config_file": str(config_path)}
        
        return None


def detect_project_language(project_path: str = ".") -> Optional[ProgrammingLanguage]:
    """Detect primary language of project."""
    detector = LanguageDetector(project_path)
    return detector.detect_language()


def get_language_template(lang: ProgrammingLanguage, template_type: str, **kwargs) -> str:
    """Generate a code template for a language."""
    generator = CodeTemplateGenerator()
    return generator.generate_template(lang, template_type, **kwargs)


def get_supported_languages() -> List[Dict[str, str]]:
    """Get list of supported languages."""
    return [
        {
            "id": lang.value,
            "name": info.name,
            "expert_model": info.expert_model,
        }
        for lang, info in LANGUAGE_CONFIGS.items()
    ]