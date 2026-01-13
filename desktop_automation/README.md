# 🖥️ Desktop Otomasyon Botu

Windows masaustu uygulamalarini (Excel, Calculator) otomatiklestiren RPA botu.

## ✨ Ozellikler

- **Excel entegrasyonu** - Veri okuma/yazma
- **Calculator kontrolu** - pyautogui ile hesaplama
- **KDV hesaplama** - Otomatik %18 KDV ekleme
- **Toplu islem** - Birden fazla urun icin otomatik hesaplama

## 🛠️ Teknolojiler

- Python 3.10+
- pyautogui
- pywinauto
- openpyxl
- pyperclip

## 📦 Kurulum

```bash
cd desktop_automation
pip install -r requirements.txt
```

## 🚀 Kullanim

```bash
python main.py
```

Bot:
1. Excel'den urun listesi okur
2. Windows Calculator'i acar
3. Her urun icin toplam + KDV hesaplar
4. Sonuclari Excel'e yazar

## 📁 Dosya Yapisi

```
desktop_automation/
├── main.py              # Ana orkestrator
├── apps/
│   ├── calculator.py    # Calculator kontrolu
│   └── excel_handler.py # Excel islemleri
├── data/
│   └── input.xlsx       # Giris verisi
└── requirements.txt
```

## 👤 Gelistirici

**Yigit Pirdogan**
- LinkedIn: [yigit-pirdogan](https://linkedin.com/in/yigit-pirdogan-36b495266)
