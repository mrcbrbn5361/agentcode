# AgentCode

> 7 ücretsiz AI modelinin gücünü tek bir çatı altında toplayan akıllı coding agent'ı

[![OpenAgentSkill](https://www.openagentskill.com/api/badge/agentcode)](https://www.openagentskill.com/skills/agentcode)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenCode Skills](https://img.shields.io/badge/OpenCode-Skills-blue.svg)](https://opencode.ai/docs/skills/)
[![Version](https://img.shields.io/badge/version-0.0.1-green.svg)](https://github.com/mrcbrbn5361/agentcode/releases/tag/v0.0.1)

## 🎯 Nedir?

AgentCode, OpenCode için geliştirilmiş bir agent skill'idir. 7 ücretsiz modelin güçlü yönlerini tek bir ajan da birleştirir ve görev türüne göre **en uygun modeli otomatik seçer**.

## 📊 Desteklenen Modeller

| Model | OpenCode ID | En İyi Alan | Context |
|-------|-------------|-------------|---------|
| MiMo-V2.5 | `opencode/mimo-v2.5-free` | Multimodal | 1M |
| DeepSeek V4 Flash | `opencode/deepseek-v4-flash-free` | Hız | 1M |
| Laguna S 2.1 | `opencode/laguna-s-2.1-free` | Terminal Agent | 1M |
| Ling-3.0-flash | `opencode/ling-3.0-flash-free` | Verimlilik | 256K |
| North Mini Code | `opencode/north-mini-code-free` | Local | 256K |
| Nemotron 3 Ultra | `opencode/nemotron-3-ultra-free` | Enterprise | 1M |
| Big Pickle | `opencode/big-pickle` | Günlük | 200K |

## 🚀 Hızlı Başlangıç

### 1. Kurulum

```bash
# Global skill dizinine kopyalayın
mkdir -p ~/.config/opencode/skills/agentcode
cp SKILL.md ~/.config/opencode/skills/agentcode/
```

### 2. Konfigürasyon

`~/.config/opencode/opencode.json` dosyasına ekleyin:

```json
{
  "$schema": "https://opencode.ai/config.json",
  "skills": {
    "paths": ["~/.config/opencode/skills"]
  }
}
```

### 3. Opencode'u Yeniden Başlatın

```bash
opencode
```

## 📝 Kullanım Örnekleri

### Hızlı Kod Üretimi
```
Kullanıcı: "FastAPI endpoint'ini yaz"
→ DeepSeek V4 Flash kullanılır (126 token/s)
```

### Görüntü Analizi
```
Kullanıcı: "Bu ekran görüntüsündeki UI hatasını düzelt"
→ MiMo-V2.5 kullanılır (multimodal destek)
```

### Terminal Görevleri
```
Kullanıcı: "Docker compose dosyasını oluştur"
→ Laguna S 2.1 kullanılır (terminal uzmanı)
```

### Büyük Projeler
```
Kullanıcı: "Bu 10K satırlık kod tabanını analiz et"
→ Nemotron 3 Ultra kullanılır (1M context)
```

## 🔀 Akıllı Yönlendirme

AgentCode otomatik olarak şu faktörlere göre model seçer:

- **Görev türü** (kod yazma, analiz, planlama)
- **Gerekli context boyutu**
- **Hız gereksinimi**
- **Bütçe kısıtlaması**
- **Multimodal ihtiyaç**

## ⚙️ Gelişmiş Konfigürasyon

### Özel Model Tercihleri

```json
{
  "agent": {
    "agentcode": {
      "model": "opencode/deepseek-v4-flash-free"
    }
  }
}
```

### İzin Ayarları

```json
{
  "permission": {
    "skill": {
      "agentcode": "allow"
    }
  }
}
```

## 📋 Görev Akışı

```
┌─────────────────────────────────────────────────┐
│  Kullanıcı Görevi Söyler                         │
└─────────────────┬───────────────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────────────────┐
│  AgentCode Görevi Analiz Eder                   │
│  - Görev türü: kod yazma / analiz / planlama     │
│  - Context ihtiyacı: küçük / büyük               │
│  - Hız önceliği: yüksek / düşük                  │
└─────────────────┬───────────────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────────────────┐
│  En Uygun Model Seçilir                         │
│  - DeepSeek V4 Flash → Hızlı kod üretimi        │
│  - Laguna S 2.1 → Kaliteli coding               │
│  - MiMo-V2.5 → Multimodal görevler              │
│  - ...                                          │
└─────────────────┬───────────────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────────────────┐
│  Görev Gerçekleştirilir ve Sonuç Sunulur        │
└─────────────────────────────────────────────────┘
```

## 🤫 Gizlilik ve Güvenlik

| Model | Gizlilik Notu |
|-------|---------------|
| Big Pickle | Stealth model - gizli projelerde dikkatli kullanın |
| Tüm ücretsiz modeller | Verileriniz eğitim için kullanılabilir |
| North Mini Code | Sovereign AI - yerinde deployment için ideal |

## 🐛 Sorun Bildirme

Sorun bulursanız lütfen [GitHub Issues](https://github.com/username/agentcode/issues) adresinden bildirin.

## 🤝 Katkıda Bulunma

Katkılarınız hoş geldi!

1. Fork yapın
2. Branch oluşturun (`git checkout -b feature/amazing-feature`)
3. Commit edin (`git commit -m 'Add amazing feature'`)
4. Push edin (`git push origin feature/amazing-feature`)
5. Pull Request oluşturun

## 📄 Lisans

Bu proje [MIT Lisansı](LICENSE) altında lisanslanmıştır.

## 🔗 Bağlantılar

- [OpenCode Docs](https://opencode.ai/docs)
- [OpenCode Skills](https://opencode.ai/docs/skills/)
- [OpenCode GitHub](https://github.com/anomalyco/opencode)

---

**v0.0.1** - İlk sürüm 🎉
