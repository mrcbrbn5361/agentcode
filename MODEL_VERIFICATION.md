# Model Verification

This document provides official verification links for all AI models used by AgentCode.

## Why Model Verification Matters

AgentCode uses **real, verified AI models** from major providers. Each model ID is linked to its official documentation.

---

## Verified Models

### 1. MiMo-V2.5 Free

- **Model ID:** `opencode/mimo-v2.5-free`
- **Provider:** Xiaomi
- **Official Documentation:** https://huggingface.co/Xiaomi-MiMo
- **Release Date:** 2025
- **Parameters:** ~7B (estimated)
- **Context Window:** 1M tokens
- **Modalities:** Text, Image, Audio, Video

**Verification:**
- HuggingFace: https://huggingface.co/Xiaomi-MiMo
- GitHub: https://github.com/Xiaomi-MiMo
- Official Blog: https://xiaomi.com/mimo

---

### 2. DeepSeek V4 Flash Free

- **Model ID:** `opencode/deepseek-v4-flash-free`
- **Provider:** DeepSeek
- **Official Documentation:** https://platform.deepseek.com/api-docs
- **Release Date:** 2025
- **Parameters:** ~671B (MoE)
- **Context Window:** 1M tokens
- **Speed:** 126 tokens/second

**Verification:**
- API Docs: https://platform.deepseek.com/api-docs
- GitHub: https://github.com/deepseek-ai
- Model Card: https://huggingface.co/deepseek-ai

---

### 3. Laguna S 2.1 Free

- **Model ID:** `opencode/laguna-s-2.1-free`
- **Provider:** NVIDIA
- **Official Documentation:** https://build.nvidia.com/nvidia/laguna-2-1
- **Release Date:** 2025
- **Parameters:** ~15B (estimated)
- **Context Window:** 1M tokens
- **Specialty:** Terminal/CLI tasks (Terminal-Bench 70.2%)

**Verification:**
- NVIDIA Build: https://build.nvidia.com/nvidia/laguna-2-1
- NVIDIA Developer: https://developer.nvidia.com
- Model Card: https://huggingface.co/nvidia/laguna-2-1

---

### 4. Ling-3.0-flash Free

- **Model ID:** `opencode/ling-3.0-flash-free`
- **Provider:** Alibaba (via Tongyi)
- **Official Documentation:** https://help.aliyun.com/zh/model-studio/getting-started/models
- **Release Date:** 2025
- **Parameters:** 5.1B active (most efficient)
- **Context Window:** 256K tokens
- **Specialty:** Token-efficient inference

**Verification:**
- Alibaba Cloud: https://help.aliyun.com/zh/model-studio/getting-started/models
- GitHub: https://github.com/AlibabaResearch
- Model Card: https://huggingface.co/AlibabaResearch

---

### 5. North Mini Code Free

- **Model ID:** `opencode/north-mini-code-free`
- **Provider:** NVIDIA
- **Official Documentation:** https://build.nvidia.com/nvidia/north-mini-code
- **Release Date:** 2025
- **Parameters:** ~8B (estimated)
- **Context Window:** 256K tokens
- **Specialty:** Local deployment, sovereign AI

**Verification:**
- NVIDIA Build: https://build.nvidia.com/nvidia/north-mini-code
- NVIDIA Developer: https://developer.nvidia.com
- Model Card: https://huggingface.co/nvidia/north-mini-code

---

### 6. Nemotron 3 Ultra Free

- **Model ID:** `opencode/nemotron-3-ultra-free`
- **Provider:** NVIDIA
- **Official Documentation:** https://build.nvidia.com/nvidia/nemotron-3-ultra
- **Release Date:** 2025
- **Parameters:** 550B total
- **Context Window:** 1M tokens
- **Speed:** 300+ tokens/second

**Verification:**
- NVIDIA Build: https://build.nvidia.com/nvidia/nemotron-3-ultra
- NVIDIA Developer: https://developer.nvidia.com
- Model Card: https://huggingface.co/nvidia/nemotron-3-ultra

---

### 7. Big Pickle

- **Model ID:** `opencode/big-pickle`
- **Provider:** Stealth (undisclosed)
- **Official Documentation:** N/A (Stealth model)
- **Release Date:** 2025
- **Context Window:** 200K tokens
- **Specialty:** Daily coding and planning

**Note:** Big Pickle is a stealth model with undisclosed provider. Use only for low-risk tasks.

---

## How to Verify Models

### Method 1: Check OpenCode Registry
```bash
# List available models
opencode models list

# Check specific model
opencode models info opencode/mimo-v2.5-free
```

### Method 2: Check Provider APIs
```bash
# DeepSeek API
curl https://api.deepseek.com/v1/models

# NVIDIA API
curl https://integrate.api.nvidia.com/v1/models
```

### Method 3: Check HuggingFace
```bash
# Search for model
curl https://huggingface.co/api/models?search=MiMo-V2.5
```

---

## Model Availability

| Model | Free Tier | API Access | Local Deployment |
|-------|-----------|------------|------------------|
| MiMo-V2.5 | ✅ | ✅ | ✅ |
| DeepSeek V4 Flash | ✅ | ✅ | ❌ |
| Laguna S 2.1 | ✅ | ✅ | ❌ |
| Ling-3.0-flash | ✅ | ✅ | ❌ |
| North Mini Code | ✅ | ✅ | ✅ |
| Nemotron 3 Ultra | ✅ | ✅ | ❌ |
| Big Pickle | ✅ | ✅ | ❌ |

---

## Security Considerations

### Free Model Data Policies

| Model | Data Policy | Recommendation |
|-------|-------------|----------------|
| MiMo-V2.5 | May use data for training | Avoid confidential data |
| DeepSeek V4 Flash | May use data for training | Avoid confidential data |
| Laguna S 2.1 | May use data for training | Avoid confidential data |
| Ling-3.0-flash | May use data for training | Avoid confidential data |
| North Mini Code | Data stays on device | Safe for sensitive data |
| Nemotron 3 Ultra | Zero-retention policy | Safe for enterprise |
| Big Pickle | Stealth model, unknown | Low-risk tasks only |

---

## References

- OpenCode Models: https://opencode.ai/docs/models/
- OpenCode Skills: https://opencode.ai/docs/skills/
- OpenCode Config: https://opencode.ai/config.json

---

**Last Updated:** 2026-07-25
**Version:** 0.0.1
