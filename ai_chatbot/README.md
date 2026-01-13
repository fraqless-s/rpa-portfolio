# 🤖 AI Chatbot (Gemini)

Google Gemini API ile calisan, web sitelerine entegre edilebilen chatbot.

## ✨ Ozellikler

- **Gemini API** - Google'in en yeni AI modeli
- **REST API** - FastAPI ile HTTP endpoint
- **Web Widget** - Hazir HTML/JS sohbet arayuzu
- **CLI modu** - Terminal uzerinden test
- **Turkce destek** - Turkce konusabilen asistan

## 🛠️ Teknolojiler

- Python 3.10+
- google-generativeai
- FastAPI
- uvicorn

## 📦 Kurulum

```bash
cd ai_chatbot
pip install -r requirements.txt
```

## 🔑 API Key

```bash
# Windows
set GEMINI_API_KEY=your-api-key

# Veya PowerShell
$env:GEMINI_API_KEY="your-api-key"
```

API Key al: https://aistudio.google.com/app/apikey

## 🚀 Kullanim

### Terminal Chatbot
```bash
python main.py
```

### Web API
```bash
python chat_api.py
# http://localhost:8000/docs
```

### Web Widget
`chat_widget.html` dosyasini tarayicida ac.

## 📁 Dosya Yapisi

```
ai_chatbot/
├── main.py           # CLI chatbot
├── chat_api.py       # REST API
├── gemini_client.py  # Gemini wrapper
├── chat_widget.html  # Web arayuzu
└── requirements.txt
```

## 👤 Gelistirici

**Yigit Pirdogan**
- LinkedIn: [yigit-pirdogan](https://linkedin.com/in/yigit-pirdogan-36b495266)
