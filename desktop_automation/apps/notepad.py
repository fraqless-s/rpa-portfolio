"""
Notepad Controller - Windows Notepad Otomasyonu
"""

import time
import subprocess
import pyautogui
from datetime import datetime
from pathlib import Path


class NotepadController:
    """Windows Notepad'i kontrol eder."""
    
    def __init__(self):
        self.process = None
        self.delay = 0.2
    
    def open(self):
        """Notepad'i açar."""
        print("[NOTEPAD] Notepad açılıyor...")
        self.process = subprocess.Popen("notepad.exe")
        time.sleep(1)
        print("[NOTEPAD] Notepad hazır.")
    
    def close(self, save: bool = False):
        """Notepad'i kapatır."""
        if not save:
            pyautogui.hotkey("alt", "F4")
            time.sleep(0.5)
            # Kaydetme sorusuna "Hayır" de
            pyautogui.press("tab")
            pyautogui.press("enter")
        print("[NOTEPAD] Notepad kapatıldı.")
    
    def type_text(self, text: str):
        """Metin yazar (Türkçe karakter destekli)."""
        # pyautogui.write() Türkçe karakterleri desteklemez
        # Bu yüzden clipboard kullanıyoruz
        import pyperclip
        pyperclip.copy(text)
        pyautogui.hotkey("ctrl", "v")
        time.sleep(self.delay)
    
    def new_line(self, count: int = 1):
        """Yeni satır ekler."""
        for _ in range(count):
            pyautogui.press("enter")
        time.sleep(self.delay)
    
    def write_report(self, products: list, grand_total: float):
        """Ürün raporu yazar."""
        report_lines = []
        
        # Başlık
        report_lines.append("=" * 60)
        report_lines.append("           ÜRÜN FİYAT RAPORU")
        report_lines.append("=" * 60)
        report_lines.append("")
        report_lines.append(f"Tarih: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
        report_lines.append(f"Toplam Ürün Sayısı: {len(products)}")
        report_lines.append("")
        report_lines.append("-" * 60)
        
        # Ürün listesi
        for i, p in enumerate(products, 1):
            report_lines.append(f"\n[{i}] {p['name']}")
            report_lines.append(f"    Birim Fiyat: {p['price']:,.2f} TL")
            report_lines.append(f"    Adet: {p['quantity']}")
            report_lines.append(f"    Ara Toplam: {p['subtotal']:,.2f} TL")
            report_lines.append(f"    KDV (%18): {p['kdv']:,.2f} TL")
            report_lines.append(f"    Toplam: {p['total']:,.2f} TL")
        
        # Alt çizgi ve genel toplam
        report_lines.append("")
        report_lines.append("-" * 60)
        report_lines.append("")
        report_lines.append(f">>> GENEL TOPLAM: {grand_total:,.2f} TL <<<")
        report_lines.append("")
        report_lines.append("=" * 60)
        report_lines.append("        Bu rapor RPA Bot tarafından oluşturulmuştur.")
        report_lines.append("=" * 60)
        
        # Tek seferde yaz
        full_text = "\n".join(report_lines)
        self.type_text(full_text)
        
        print(f"[NOTEPAD] Rapor yazıldı ({len(products)} ürün)")
    
    def save_as(self, file_path: str):
        """Dosyayı farklı kaydet."""
        # Farklı kaydet dialogu
        pyautogui.hotkey("ctrl", "shift", "s")
        time.sleep(1)
        
        # Dosya yolunu yaz
        import pyperclip
        pyperclip.copy(file_path)
        pyautogui.hotkey("ctrl", "v")
        time.sleep(0.3)
        
        # Kaydet
        pyautogui.press("enter")
        time.sleep(0.5)
        
        # Eğer dosya varsa "Evet" de
        pyautogui.press("left")
        pyautogui.press("enter")
        time.sleep(0.3)
        
        print(f"[NOTEPAD] Dosya kaydedildi: {file_path}")


if __name__ == "__main__":
    # Test
    notepad = NotepadController()
    notepad.open()
    
    test_products = [
        {"name": "Test Ürün", "price": 100, "quantity": 2, "subtotal": 200, "kdv": 36, "total": 236}
    ]
    
    notepad.write_report(test_products, 236)
    time.sleep(2)
    notepad.close()
