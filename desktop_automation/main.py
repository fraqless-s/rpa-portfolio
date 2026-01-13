"""
Desktop Otomasyon - Excel -> Calculator
==========================================
Bu bot:
1. Excel'den urun listesi ve fiyatlari okur
2. Windows Calculator'da KDV hesaplar
3. Sonuclari Excel'e geri yazar

Senaryo A: Kolay seviye
Kullanim:
    python main.py
"""

import time
import sys
from pathlib import Path
from datetime import datetime

# Modul yolunu ayarla
sys.path.insert(0, str(Path(__file__).parent))

from apps.excel_handler import ExcelHandler
from apps.calculator import CalculatorController


# ============================================================
# AYARLAR
# ============================================================
KDV_RATE = 18  # %18 KDV
INPUT_FILE = "data/input.xlsx"


def print_banner():
    """Baslangic banner'i."""
    print("\n" + "=" * 50)
    print(">>> DESKTOP OTOMASYON BOTU <<<")
    print("    Senaryo A: Excel -> Calculator")
    print("=" * 50)
    print(f"    Baslangic: {datetime.now().strftime('%H:%M:%S')}")
    print(f"    KDV Orani: %{KDV_RATE}")
    print("=" * 50 + "\n")


def main():
    print_banner()
    
    # 1. EXCEL - Veri Yukleme
    print("[ADIM 1/3] Excel'den veri yukleniyor...")
    print("-" * 40)
    
    excel = ExcelHandler()
    input_path = Path(__file__).parent / INPUT_FILE
    
    # Eger dosya yoksa ornek veri olustur
    if not input_path.exists() or input_path.stat().st_size == 0:
        print("[INFO] Ornek veri dosyasi olusturuluyor...")
        excel.create_sample_data(str(input_path))
    
    products = excel.load(str(input_path))
    print(f"[OK] {len(products)} urun yuklendi\n")
    
    # 2. CALCULATOR - KDV Hesaplama
    print("[ADIM 2/3] Calculator'da hesaplama yapiliyor...")
    print("-" * 40)
    
    calc = CalculatorController()
    calc.open()
    
    grand_total = 0
    
    for i, product in enumerate(products, 1):
        name = product.get("Urun Adi", "Bilinmeyen")
        price_val = product.get("Birim Fiyat (TL)")
        quantity_val = product.get("Adet")
        
        # Bos veya gecersiz satirlari atla
        if price_val is None or quantity_val is None:
            continue
            
        price = float(price_val)
        quantity = int(quantity_val)
        
        print(f"\n[{i}/{len(products)}] {name}")
        print(f"    Fiyat: {price:,.0f} TL x {quantity} adet")
        
        # Ara toplam (fiyat x adet)
        subtotal = calc.multiply(price, quantity)
        time.sleep(0.2)
        
        # KDV hesapla
        kdv = calc.calculate_with_percentage(subtotal, KDV_RATE)
        time.sleep(0.2)
        
        # Genel toplam
        total = calc.add(subtotal, kdv)
        time.sleep(0.2)
        
        print(f"    Ara Toplam: {subtotal:,.2f} TL")
        print(f"    KDV (%{KDV_RATE}): {kdv:,.2f} TL")
        print(f"    Toplam: {total:,.2f} TL")
        
        # Excel'i guncelle
        excel.update_row(i + 1, subtotal, kdv, total)
        grand_total += total
    
    # Calculator'i kapat
    print("\n")
    calc.close()
    
    # 3. EXCEL - Kaydet
    print("\n[ADIM 3/3] Excel'e kaydediliyor...")
    print("-" * 40)
    
    excel.add_summary(grand_total)
    excel.save()
    
    # OZET
    print("\n" + "=" * 50)
    print(">>> ISLEM TAMAMLANDI! <<<")
    print("=" * 50)
    print(f"    Islenen Urun: {len(products)}")
    print(f"    Genel Toplam: {grand_total:,.2f} TL")
    print(f"    Kayit: {input_path}")
    print("=" * 50 + "\n")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[IPTAL] Kullanici tarafindan durduruldu.")
    except Exception as e:
        print(f"\n[HATA] {e}")
        raise
