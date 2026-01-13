"""
Gemini API Client
=================
Google Gemini API ile iletisim kurar.
"""

import os
import google.generativeai as genai
from typing import Optional


class GeminiClient:
    """Gemini API istemcisi."""
    
    def __init__(self, api_key: str = None, model: str = "gemini-2.0-flash"):
        """
        Args:
            api_key: Gemini API anahtari (veya GEMINI_API_KEY env)
            model: Kullanilacak model
        """
        self.api_key = api_key or os.getenv("GEMINI_API_KEY")
        
        if not self.api_key:
            raise ValueError("GEMINI_API_KEY gerekli! Ortam degiskeni olarak ayarlayin veya parametre olarak verin.")
        
        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel(model)
        self.chat = None
        self.history = []
    
    def start_chat(self, system_prompt: str = None):
        """Yeni sohbet baslat."""
        if system_prompt:
            self.chat = self.model.start_chat(history=[
                {"role": "user", "parts": [system_prompt]},
                {"role": "model", "parts": ["Anlasildı. Size yardimci olmaya hazirim."]}
            ])
        else:
            self.chat = self.model.start_chat()
        
        self.history = []
        print("[CHAT] Yeni sohbet baslatildi.")
    
    def send_message(self, message: str) -> str:
        """Mesaj gonder ve cevap al."""
        if not self.chat:
            self.start_chat()
        
        try:
            response = self.chat.send_message(message)
            reply = response.text
            
            # Gecmise ekle
            self.history.append({"role": "user", "content": message})
            self.history.append({"role": "assistant", "content": reply})
            
            return reply
        
        except Exception as e:
            return f"Hata: {str(e)}"
    
    def simple_query(self, prompt: str) -> str:
        """Tek seferlik sorgu (sohbet gecmisi olmadan)."""
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"Hata: {str(e)}"
    
    def get_history(self) -> list:
        """Sohbet gecmisini dondur."""
        return self.history


if __name__ == "__main__":
    # Test - API key gerektirir
    print("Gemini Client testi icin GEMINI_API_KEY ortam degiskeni gerekli.")
    print("Ornek: set GEMINI_API_KEY=your-api-key")
