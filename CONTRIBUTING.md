# Contributing to AgentCode

Thank you for your interest in contributing to AgentCode! This document provides guidelines and information about contributing.

## How to Contribute

### 1. Fork the Repository

```bash
# Fork via GitHub CLI
gh repo fork mrcbrbn5361/agentcode

# Or fork via web interface
# https://github.com/mrcbrbn5361/agentcode/fork
```

### 2. Clone Your Fork

```bash
git clone https://github.com/YOUR_USERNAME/agentcode.git
cd agentcode
```

### 3. Create Feature Branch

```bash
git checkout -b feature/amazing-feature
```

### 4. Make Changes

- Follow existing code style
- Add comments if needed
- Update documentation
- Add tests if applicable

### 5. Test Changes

```bash
# Test locally with OpenCode
opencode

# Try the skill with various tasks
# Verify model selection works correctly
```

### 6. Commit Changes

```bash
git add .
git commit -m "Add amazing feature"
```

### 7. Push to Branch

```bash
git push origin feature/amazing-feature
```

### 8. Open Pull Request

```bash
# Via GitHub CLI
gh pr create --repo mrcbrbn5361/agentcode

# Or via web interface
# https://github.com/mrcbrbn5361/agentcode/compare/main...your-branch
```

---

## Development Guidelines

### Code Style

- Use clear, descriptive variable names
- Keep functions small and focused
- Add comments for complex logic
- Follow markdown best practices for documentation

### Documentation

- Update README.md if adding features
- Add examples for new functionality
- Keep SKILL.md up to date
- Update CHANGELOG.md with changes

### Commit Messages

Use clear, descriptive commit messages:

```
Add: New feature description
Fix: Bug fix description
Update: Improvement description
Remove: Removed feature description
```

### Testing

Before submitting a PR:

1. Test locally with OpenCode
2. Verify model selection works
3. Check for errors or warnings
4. Ensure documentation is accurate

---

## Types of Contributions

### Bug Reports

If you find a bug:

1. Check existing issues first
2. Open a new issue with:
   - Clear description
   - Steps to reproduce
   - Expected vs actual behavior
   - Screenshots if applicable

### Feature Requests

For new features:

1. Open an issue first
2. Describe the feature
3. Explain use cases
4. Wait for approval before implementing

### Documentation

Help improve documentation:

1. Fix typos
2. Add examples
3. Improve clarity
4. Translate to other languages

### Code Contributions

1. Follow the development guidelines
2. Add tests if applicable
3. Update documentation
4. Submit a PR

---

## Style Guide

### Markdown

- Use proper heading hierarchy
- Add code blocks with language syntax
- Include examples
- Keep line lengths reasonable

### Code

- Use consistent indentation
- Follow language conventions
- Add comments where needed
- Keep functions focused

---

## Questions?

If you have questions:

1. Check the documentation
2. Open a GitHub issue
3. Join the community discussions

---

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

Thank you for contributing to AgentCode! 🎉
