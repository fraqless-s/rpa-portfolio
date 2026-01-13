# 📄 PDF Rapor Olusturucu

Excel'den veri okuyup profesyonel PDF raporlar ureten otomasyon.

## ✨ Ozellikler

- **Satis raporu** - Urun listesi, toplam hesaplama
- **Profesyonel tasarim** - Renkli tablolar, basliklar
- **Otomatik tarihlendirme** - Timestamp ekleme
- **Toplu uretim** - Birden fazla rapor

## 🛠️ Teknolojiler

- Python 3.10+
- reportlab
- openpyxl

## 📦 Kurulum

```bash
cd email_automation
pip install -r requirements.txt
```

## 🚀 Kullanim

```bash
# Demo modu
python main.py demo

# Excel'den rapor
python main.py
```

## 📸 Ornek Cikti

Bot, stillendirilmis PDF raporlar olusturur:
- Mavi baslik satiri
- Yesil toplam satiri
- Otomatik KDV hesaplama

## 📁 Dosya Yapisi

```
email_automation/
├── main.py           # Ana bot
├── pdf_generator.py  # PDF olusturucu
├── data/
│   └── urunler.xlsx
└── output/reports/
```

## 👤 Gelistirici

**Yigit Pirdogan**
- LinkedIn: [yigit-pirdogan](https://linkedin.com/in/yigit-pirdogan-36b495266)
