# 📱 QR Kod Olusturucu

Excel'den veri okuyup toplu QR kod ureten API entegrasyonu projesi.

## ✨ Ozellikler

- **Sosyal medya QR** - Instagram, LinkedIn, Twitter, YouTube
- **vCard QR** - Kartvizit bilgisi
- **WiFi QR** - Ag baglanti bilgisi
- **Toplu uretim** - Excel'den coklu QR
- **Ozel renkler** - Platform bazli renklendirme

## 🛠️ Teknolojiler

- Python 3.10+
- qrcode + Pillow
- requests (goqr.me API)
- openpyxl

## 📦 Kurulum

```bash
cd qr_generator
pip install -r requirements.txt
```

## 🚀 Kullanim

```bash
# Demo modu
python main.py demo

# Excel'den toplu uretim
python main.py
```

## 📸 Ornek QR Kodlar

Bot, renklendirmis QR kodlar uretir:
- Instagram: Pembe
- LinkedIn: Mavi
- GitHub: Siyah

## 📁 Dosya Yapisi

```
qr_generator/
├── main.py          # Ana bot
├── qr_local.py      # Yerel QR uretici
├── qr_api.py        # API client
├── data/
│   └── social_links.xlsx
└── output/qr_codes/
```

## 👤 Gelistirici

**Yigit Pirdogan**
- LinkedIn: [yigit-pirdogan](https://linkedin.com/in/yigit-pirdogan-36b495266)
