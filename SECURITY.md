# Security Policy

## Reporting Vulnerabilities

If you discover a security vulnerability, please report it responsibly.

### How to Report

1. **For non-critical issues**: Open a GitHub issue
2. **For critical issues**: Contact via email (if provided in repo)

**Do NOT disclose publicly until fixed.**

### What to Include

- Description of the vulnerability
- Steps to reproduce
- Potential impact
- Suggested fix (if any)

---

## Security Considerations

### Free Models

⚠️ **Important**: Free models may use your data for training.

| Model | Data Policy | Risk Level |
|-------|-------------|------------|
| MiMo-V2.5 | May use data for training | Medium |
| DeepSeek V4 Flash | May use data for training | Medium |
| Laguna S 2.1 | May use data for training | Medium |
| Ling-3.0-flash | May use data for training | Medium |
| North Mini Code | Data stays on device | Low |
| Nemotron 3 Ultra | Zero-retention policy | Low |
| Big Pickle | Stealth model, unknown | High |

### Recommendations

1. **Never use free models for confidential code**
2. **Use local models (North Mini Code) for sensitive data**
3. **Verify outputs before deployment**
4. **Review model selection before execution**

---

## Data Handling

### What We Collect

- No code or context data is stored
- No personal information is collected
- Skill configuration is local only

### Free Model Data Usage

Free models may:
- Use inputs for model training
- Store conversation data
- Process data on external servers

### Local Model Data Usage

Local models (North Mini Code):
- Process data on your device
- No data sent to external servers
- Full privacy control

---

## Best Practices

### 1. Review Model Selection

Before processing sensitive data:
- Check which model will be used
- Verify it's appropriate for your data
- Consider using local models

### 2. Verify Outputs

Always verify:
- Generated code is correct
- No sensitive data is exposed
- Security best practices are followed

### 3. Keep Updated

- Keep AgentCode updated
- Check for security advisories
- Monitor model availability

### 4. Follow Least Privilege

- Only grant necessary permissions
- Review permission settings
- Restrict access to sensitive data

---

## Model-Specific Security

### Big Pickle (Stealth Model)

⚠️ **High Risk**

- Identity undisclosed
- Data usage unknown
- **Recommendation**: Use only for low-risk tasks

### Free Tier Models

⚠️ **Medium Risk**

- Data may be used for training
- **Recommendation**: Never use for confidential code

### North Mini Code

✅ **Low Risk**

- Runs locally
- No data sent externally
- **Recommendation**: Use for sensitive projects

### Nemotron 3 Ultra

✅ **Low Risk**

- Zero-retention policy
- Enterprise-grade security
- **Recommendation**: Safe for production use

---

## Compliance

### Open Source

- MIT License
- Open source code
- Community reviewed

### Data Protection

- No data collection by AgentCode
- Model data usage varies by provider
- User responsible for data handling

---

## Updates

This security policy is updated as needed.

Last updated: 2026-07-25

---

## Contact

For security concerns:
- GitHub Issues: https://github.com/mrcbrbn5361/agentcode/issues
- Repository: https://github.com/mrcbrbn5361/agentcode

---

Thank you for helping keep AgentCode secure! 🔒
