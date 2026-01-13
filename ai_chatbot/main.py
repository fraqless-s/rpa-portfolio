"""
CLI Chatbot
===========
Terminal uzerinden chatbot ile sohbet.
Test ve demo icin kullanilir.
"""

import os
import sys
from pathlib import Path
from datetime import datetime

sys.path.insert(0, str(Path(__file__).parent))


def print_banner():
    print("\n" + "=" * 50)
    print(">>> AI CHATBOT (Gemini) <<<")
    print("=" * 50)
    print("Komutlar:")
    print("  /cikis  - Programdan cik")
    print("  /sifirla - Sohbeti sifirla")
    print("  /gecmis - Sohbet gecmisini goster")
    print("=" * 50 + "\n")


def main():
    print_banner()
    
    # API key kontrolu
    api_key = os.getenv("GEMINI_API_KEY")
    
    if not api_key:
        print("[HATA] GEMINI_API_KEY ortam degiskeni bulunamadi!")
        print("\nCozum:")
        print("  Windows: set GEMINI_API_KEY=your-api-key")
        print("  Linux:   export GEMINI_API_KEY=your-api-key")
        print("\nAPI key icin: https://makersuite.google.com/app/apikey")
        return
    
    # Gemini client'i baslat
    from gemini_client import GeminiClient
    
    try:
        client = GeminiClient(api_key=api_key)
        client.start_chat(
            system_prompt="Sen yardimci bir Turkce asistan sin. Kisa ve anlasilir cevaplar ver."
        )
        print("[OK] Chatbot hazir! Yazmaya basla...\n")
    except Exception as e:
        print(f"[HATA] Gemini baglantisi kurulamadi: {e}")
        return
    
    # Sohbet dongusu
    while True:
        try:
            user_input = input("Sen: ").strip()
            
            if not user_input:
                continue
            
            # Komutlar
            if user_input.lower() == "/cikis":
                print("\nGorusuruz! 👋\n")
                break
            
            elif user_input.lower() == "/sifirla":
                client.start_chat(
                    system_prompt="Sen yardimci bir Turkce asistan sin. Kisa ve anlasilir cevaplar ver."
                )
                print("[OK] Sohbet sifirlandi.\n")
                continue
            
            elif user_input.lower() == "/gecmis":
                history = client.get_history()
                if history:
                    print("\n--- Sohbet Gecmisi ---")
                    for msg in history:
                        role = "Sen" if msg["role"] == "user" else "Bot"
                        print(f"{role}: {msg['content'][:100]}...")
                    print("--- Son ---\n")
                else:
                    print("[INFO] Henuz sohbet gecmisi yok.\n")
                continue
            
            # Normal mesaj
            response = client.send_message(user_input)
            print(f"\nBot: {response}\n")
        
        except KeyboardInterrupt:
            print("\n\nGorusuruz! 👋\n")
            break
        except Exception as e:
            print(f"\n[HATA] {e}\n")


if __name__ == "__main__":
    main()
