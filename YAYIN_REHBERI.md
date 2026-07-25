# 🚀 AgentCode Yayın Rehberi

## 📋 Yayın Öncesi Kontrol Listesi

- [ ] SKILL.md dosyası doğru formatta mı?
- [ ] README.md dosyası eksiksiz mi?
- [ ] LICENSE dosyası var mı?
- [ ] package.json doğru mu?
- [ ] .gitignore oluşturuldu mu?

## 🔧 Yayın Adımları

### Adım 1: GitHub Deposu Oluştur

1. GitHub'a gidin: https://github.com/new
2. Yeni depo oluşturun:
   - **Name:** `agentcode`
   - **Description:** "7 ücretsiz modelin en iyi yeteneklerini tek çatı altında toplayan akıllı coding agent'ı"
   - **Visibility:** Public (veya tercih ettiğiniz)
   - **Initialize:** README.md ile başlatmayın (zaten var)

### Adım 2: Git Deposu Başlatın

```bash
cd /data/data/com.termux/files/home/agentcode-publish

# Git deposunu başlat
git init

# Dosyaları ekleyin
git add .

# İlk commit'i yapın
git commit -m "v0.0.1: İlk sürüm - 7 ücretsiz model entegrasyonu"

# Uzak depoyu ekleyin (GitHub URL'nizi kullanın)
git remote add origin https://github.com/YOUR_USERNAME/agentcode.git

# Ana dala push edin
git push -u origin main
```

### Adım 3: İlk Sürüm (Release) Oluşturun

```bash
# Tag oluşturun
git tag -a v0.0.1 -m "v0.0.1: İlk sürüm"
git push origin v0.0.1
```

### Adım 4: GitHub'da Release Oluşturun

1. GitHub depo sayfasına gidin
2. "Releases" bölümüne tıklayın
3. "Create a new release" butonuna tıklayın
4. Tag: `v0.0.1`
5. Title: `v0.0.1 - İlk Sürüm`
6. Description:

```markdown
## 🎉 v0.0.1 - İlk Sürüm

### ✨ Yeni Özellikler
- 7 ücretsiz model entegrasyonu
- Akıllı model yönlendirme
- Multimodal görev desteği
- Hızlı kod üretimi

### 📊 Desteklenen Modeller
- MiMo-V2.5 (Multimodal)
- DeepSeek V4 Flash (Hız)
- Laguna S 2.1 (Terminal Agent)
- Ling-3.0-flash (Verimlilik)
- North Mini Code (Local)
- Nemotron 3 Ultra (Enterprise)
- Big Pickle (Günlük)

### 🚀 Kurulum
SKILL.md dosyasını ~/.config/opencode/skills/agentcode/ dizinine kopyalayın.
```

7. "Publish release" butonuna tıklayın

## 📦 Alternatif Yayın Yöntemleri

### Yöntem 1: npm ile Yayın

```bash
# package.json'da username'i güncelleyin
# package.json'daki homepage ve repository.url güncelleyin

# npm'a giriş yapın
npm login

# Yayınlayın
npm publish
```

### Yöntem 2: OpenCode Registry

OpenCode ekosistemi henüz resmi bir registry sunmuyor, ancak gelecekte eklenebilir. Şimdilik GitHub üzerinden paylaşım en iyi yöntem.

## 🔄 Güncelleme Yapma

### Küçük Sürüm (Patch)

```bash
# package.json'da versiyonu güncelleyin
# "version": "0.0.2" yapın

git add .
git commit -m "v0.0.2: Bug fixes"
git tag -a v0.0.2 -m "v0.0.2"
git push origin main --tags
```

### Büyük Sürüm (Minor)

```bash
# package.json'da versiyonu güncelleyin
# "version": "0.1.0" yapın

git add .
git commit -m "v0.1.0: Yeni özellikler"
git tag -a v0.1.0 -m "v0.1.0"
git push origin main --tags
```

## 📢 Duyuru Yapma

### GitHub'da

1. README.md'yi güncelleyin
2. Release notlarını yazın
3. GitHub Discussions açın

### Sosyal Medyada

```
🎉 AgentCode v0.0.1 çıktı!

7 ücretsiz AI modelini tek bir coding agent'ında birleştirdik:
- MiMo-V2.5 (Multimodal)
- DeepSeek V4 Flash (Hız)
- Laguna S 2.1 (Terminal)
- Ling-3.0-flash (Verimlilik)
- North Mini Code (Local)
- Nemotron 3 Ultra (Enterprise)
- Big Pickle (Günlük)

Şimdi deneyin: https://github.com/username/agentcode

#OpenCode #AI #CodingAgent #FreeModels
```

## 🐛 Sorun Giderme

### Yayında Sorun Olursa

1. GitHub Issues'dan bildirin
2. Hızlı düzeltme için hotfix branch'i oluşturun
3. Yeni sürüm yayınlayın

### Kullanıcılar Kuramazsa

1. README'deki kurulum adımlarını kontrol edin
2. Troubleshooting bölümünü ekleyin
3. Örnek konfigürasyonları paylaşın

## 📊 Takip

- GitHub Insights
- npm download sayısı (eğer npm'deyseniz)
- Kullanıcı geri bildirimleri

## 🤝 Katkı Yönetimi

1. CONTRIBUTING.md dosyası oluşturun
2. Pull Request şablonu ekleyin
3. Issue şablonları oluşturun

---

**Başarılar! 🎉**
