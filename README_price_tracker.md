# 🕷️ E-Ticaret Fiyat Takip Botu

Turkiye'nin populer e-ticaret sitelerinden (Amazon, Trendyol, Hepsiburada) otomatik fiyat takibi yapan RPA botu.

## ✨ Ozellikler

- **Multi-site destegi** - Amazon TR, Trendyol, Hepsiburada
- **Async scraping** - Playwright ile hizli veri cekme
- **Excel raporlama** - Otomatik stillendirilmis cikti
- **Anti-bot onlemleri** - User-Agent rotation, bekleme sureleri
- **OOP mimari** - Factory pattern ile genisletilebilir yapi

## 🛠️ Teknolojiler

- Python 3.10+
- Playwright (async)
- openpyxl
- asyncio

## 📦 Kurulum

```bash
pip install playwright openpyxl
playwright install chromium
```

## 🚀 Kullanim

```bash
python price_tracker.py
```

## 📸 Ekran Goruntusu

Bot calisirken tarayici acilir ve siteleri ziyaret eder. Sonuclar `fiyat_takibi.xlsx` dosyasina kaydedilir.

## 📁 Dosya Yapisi

```
price_tracker.py    # Ana bot kodu
fiyat_takibi.xlsx   # Cikti raporu
requirements.txt    # Bagimliliklar
```

## 👤 Gelistirici

**Yigit Pirdogan**
- LinkedIn: [yigit-pirdogan](https://linkedin.com/in/yigit-pirdogan-36b495266)
- GitHub: [ypirdoqan](https://github.com/ypirdoqan)
