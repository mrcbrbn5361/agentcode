---
name: agentcode
description: "7 ücretsiz modelin en iyi yeteneklerini tek çatı altında toplayan akıllı coding agent'ı. Görev türüne göre en uygun modeli otomatik seçer. Trigger: kod yaz, refactor, debug, analiz, plan, dosya düzenle, test yaz, proje oluştur."
license: MIT
compatibility: opencode
metadata:
  version: "0.0.1"
  author: "AgentCode Contributors"
  models: "7"
  category: "coding-agent"
---

# AgentCode - Akıllı Multi-Model Coding Agent 🚀

[![OpenAgentSkill](https://www.openagentskill.com/api/badge/agentcode)](https://www.openagentskill.com/skills/agentcode)

> 7 ücretsiz AI modelinin gücünü tek bir ajan da birleştiren akıllı coding agent'ı

## 🎯 Ne Yapar?

AgentCode, kullanıcının coding görevini analiz eder ve **en uygun ücretsiz modeli otomatik seçer**. Her modelin güçlü olduğu alanları kullanarak en iyi sonucu verir.

## 📊 7 Ücretsiz Model

| Model | En İyi Alan | Context |
|-------|-------------|---------|
| **MiMo-V2.5** | Multimodal (Görüntü+Ses+Video) | 1M |
| **DeepSeek V4 Flash** | Hız & Yüksek Hacim | 1M |
| **Laguna S 2.1** | Terminal Coding Agent | 1M |
| **Ling-3.0-flash** | Token Verimliliği | 256K |
| **North Mini Code** | Yerinde (Local) Deployment | 256K |
| **Nemotron 3 Ultra** | Enterprise Long-Horizon Agent | 1M |
| **Big Pickle** | Günlük Ücretsiz Coding | 200K |

## 🔀 Akıllı Yönlendirme

| Görev Türü | Önerilen Model | Neden |
|------------|----------------|-------|
| Hızlı Kod Üretimi | DeepSeek V4 Flash | 126 token/s ile en hızlı |
| Kaliteli Coding | Laguna S 2.1 | Terminal-Bench %70.2 |
| Görüntü/Ses Analizi | MiMo-V2.5 | Multimodal destek |
| Hızlı Planlama | Big Pickle | Ücretsiz ve hızlı |
| Uzun Proje | Nemotron 3 Ultra | 1M context + enterprise |
| Yerinde Deployment | North Mini Code | Sovereign AI |
| Bütçe Dostu | Ling-3.0-flash | En ucuz inference |

## 🚀 Kurulum

### Opsiyon 1: Manuel Kurulum

```bash
# Skill dizinini oluştur
mkdir -p ~/.config/opencode/skills/agentcode

# SKILL.md dosyasını indir
curl -fsSL https://raw.githubusercontent.com/username/agentcode/main/SKILL.md \
  -o ~/.config/opencode/skills/agentcode/SKILL.md
```

### Opsiyon 2: Git ile Kurulum

```bash
cd ~/.config/opencode/skills
git clone https://github.com/username/agentcode.git
```

### Opsiyon 3: OpenCode Config

`opencode.json` dosyasına ekle:

```json
{
  "skills": {
    "paths": ["~/.config/opencode/skills"]
  }
}
```

## 📝 Kullanım

### Örnek 1: Hızlı Kod Üretimi

```
Kullanıcı: "React component'ini yaz"
AgentCode: DeepSeek V4 Flash kullanır (hızlı kod üretimi)
```

### Örnek 2: Görüntü Analizi

```
Kullanıcı: "Bu ekran görüntüsündeki hatayı düzelt"
AgentCode: MiMo-V2.5 kullanır (multimodal analiz)
```

### Örnek 3: Planlama

```
Kullanıcı: "Bu proje için plan oluştur"
AgentCode: Big Pickle kullanır (ücretsiz planlama)
```

## ⚙️ Konfigürasyon

### Varsayılan Agent Olarak Ayarlama

`opencode.json`:

```json
{
  "$schema": "https://opencode.ai/config.json",
  "default_agent": "agentcode"
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

## 🤫 Gizlilik Notları

- **Big Pickle** stealth modeldir, gizli projelerde dikkatli kullanın
- Ücretsiz modeller **sınırlı süreliğine** ücretsizdir
- Tüm ücretsiz modeller verilerinizi **eğitim için kullanabilir**

## 📋 Görev Akışı

```
1. Kullanıcı görevini söyler
2. AgentCode görevi analiz eder
3. En uygun modeli seçer (sebebiyle açıklar)
4. Görevi gerçekleştirir
5. Sonucu sunar
```

## 🔧 Sorun Giderme

### Skill Görünmüyor?

1. `SKILL.md` dosyasının big harflerle yazıldığından emin olun
2. Frontmatter'da `name` ve `description` olduğundan emin olun
3. Skill adının benzersiz olduğundan emin olun
4. İzinleri kontrol edin

### Model Seçilmiyor?

- Görev türünün doğru analiz edildiğinden emin olun
- Model ID'lerinin doğru formatta olduğundan emin olun (`opencode/model-id`)

## 🤝 Katkıda Bulunma

1. Fork yapın
2. Feature branch oluşturun
3. Değişikliklerinizi commit edin
4. Pull request oluşturun

## 📄 Lisans

MIT Lisansı - Detaylı bilgi için [LICENSE](LICENSE) dosyasına bakın

## 🔗 Bağlantılar

- [OpenCode Docs](https://opencode.ai/docs)
- [OpenCode GitHub](https://github.com/anomalyco/opencode)
- [Sorun Bildir](https://github.com/username/agentcode/issues)

---

**v0.0.1** - İlk sürüm 🎉
