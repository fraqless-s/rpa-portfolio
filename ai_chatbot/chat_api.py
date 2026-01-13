"""
FastAPI Chat API
================
REST API olarak chatbot servisi sunar.
Herhangi bir web sitesine entegre edilebilir.
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from gemini_client import GeminiClient


# FastAPI uygulamasi
app = FastAPI(
    title="AI Chatbot API",
    description="Gemini tabanli chatbot REST API",
    version="1.0.0"
)

# CORS - Tum originlere izin ver (site entegrasyonu icin)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Global client (basit implementasyon)
chat_client: Optional[GeminiClient] = None


# Request/Response modelleri
class ChatRequest(BaseModel):
    message: str
    system_prompt: Optional[str] = None


class ChatResponse(BaseModel):
    reply: str
    success: bool


class HealthResponse(BaseModel):
    status: str
    message: str


@app.on_event("startup")
async def startup():
    """Uygulama baslarken Gemini client'i baslat."""
    global chat_client
    api_key = os.getenv("GEMINI_API_KEY")
    
    if api_key:
        try:
            chat_client = GeminiClient(api_key=api_key)
            chat_client.start_chat(
                system_prompt="Sen yardimci bir asistansin. Turkce konusuyorsun. Kisa ve net cevaplar ver."
            )
            print("[API] Gemini client baslatildi.")
        except Exception as e:
            print(f"[API] Gemini client hatasi: {e}")
    else:
        print("[API] UYARI: GEMINI_API_KEY bulunamadi!")


@app.get("/", response_model=HealthResponse)
async def root():
    """API durum kontrolu."""
    return HealthResponse(
        status="ok",
        message="AI Chatbot API calisiyor!"
    )


@app.get("/health", response_model=HealthResponse)
async def health():
    """Saglik kontrolu."""
    if chat_client:
        return HealthResponse(status="ok", message="Gemini bagli")
    else:
        return HealthResponse(status="warning", message="Gemini bagli degil - API key eksik")


@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    """
    Chatbot ile mesajlasma.
    
    Ornek:
        POST /chat
        {"message": "Merhaba, nasilsin?"}
    """
    if not chat_client:
        raise HTTPException(
            status_code=503,
            detail="Chatbot hazir degil. GEMINI_API_KEY ortam degiskenini ayarlayin."
        )
    
    try:
        reply = chat_client.send_message(request.message)
        return ChatResponse(reply=reply, success=True)
    except Exception as e:
        return ChatResponse(reply=f"Hata: {str(e)}", success=False)


@app.post("/reset")
async def reset_chat():
    """Sohbeti sifirla."""
    if chat_client:
        chat_client.start_chat(
            system_prompt="Sen yardimci bir asistansin. Turkce konusuyorsun. Kisa ve net cevaplar ver."
        )
        return {"message": "Sohbet sifirlandi."}
    else:
        raise HTTPException(status_code=503, detail="Chatbot hazir degil.")


if __name__ == "__main__":
    import uvicorn
    print("\n" + "=" * 50)
    print("AI CHATBOT API BASLATILIYOR")
    print("=" * 50)
    print("Adres: http://localhost:8000")
    print("Docs:  http://localhost:8000/docs")
    print("=" * 50 + "\n")
    
    uvicorn.run(app, host="0.0.0.0", port=8000)
