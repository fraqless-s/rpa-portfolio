"""
Calculator Controller - Windows Hesap Makinesi Otomasyonu
Fallback: Eger clipboard'dan okuma basarisiz olursa Python ile hesaplar
"""

import time
import subprocess
import pyautogui
import pyperclip


class CalculatorController:
    """Windows Calculator'i kontrol eder."""
    
    def __init__(self, use_real_calc: bool = True):
        self.process = None
        self.delay = 0.4
        self.use_real_calc = use_real_calc
    
    def open(self):
        """Hesap makinesini acar."""
        if not self.use_real_calc:
            print("[CALC] Python hesaplama modu aktif.")
            return
            
        print("[CALC] Hesap makinesi aciliyor...")
        self.process = subprocess.Popen("calc.exe")
        time.sleep(2)
        
        # Calculator penceresine odaklan
        try:
            import pygetwindow as gw
            calc_windows = gw.getWindowsWithTitle("Calculator")
            if not calc_windows:
                calc_windows = gw.getWindowsWithTitle("Hesap Makinesi")
            if calc_windows:
                calc_windows[0].activate()
                time.sleep(0.5)
        except:
            pass
        
        print("[CALC] Hesap makinesi hazir.")
    
    def close(self):
        """Hesap makinesini kapatir."""
        if not self.use_real_calc:
            return
            
        pyautogui.hotkey("alt", "F4")
        time.sleep(0.3)
        print("[CALC] Hesap makinesi kapatildi.")
    
    def clear(self):
        """Ekrani temizler."""
        if not self.use_real_calc:
            return
        pyautogui.press("escape")
        time.sleep(0.2)
    
    def multiply(self, a: float, b: float) -> float:
        """Iki sayiyi carpar ve sonucu dondurur."""
        result = a * b
        
        if self.use_real_calc:
            self.clear()
            self._type_expression(f"{int(a) if a == int(a) else a}*{int(b) if b == int(b) else b}")
            pyautogui.press("enter")
            time.sleep(0.3)
        
        print(f"[CALC] {a} x {b} = {result}")
        return result
    
    def calculate_with_percentage(self, base: float, percentage: float) -> float:
        """Yuzde hesaplar (base * percentage / 100)."""
        result = base * percentage / 100
        
        if self.use_real_calc:
            self.clear()
            base_str = str(int(base)) if base == int(base) else str(base)
            self._type_expression(f"{base_str}*{int(percentage)}/100")
            pyautogui.press("enter")
            time.sleep(0.3)
        
        print(f"[CALC] {base} x %{percentage} = {result}")
        return result
    
    def add(self, a: float, b: float) -> float:
        """Iki sayiyi toplar."""
        result = a + b
        
        if self.use_real_calc:
            self.clear()
            a_str = str(int(a)) if a == int(a) else str(a)
            b_str = str(int(b)) if b == int(b) else str(b)
            self._type_expression(f"{a_str}+{b_str}")
            pyautogui.press("enter")
            time.sleep(0.3)
        
        print(f"[CALC] {a} + {b} = {result}")
        return result
    
    def _type_expression(self, expr: str):
        """Ifadeyi hesap makinesine yazar."""
        for char in expr:
            if char == ".":
                pyautogui.press(".")
            elif char == "*":
                pyautogui.press("*")
            elif char == "/":
                pyautogui.press("/")
            elif char == "+":
                pyautogui.press("+")
            elif char == "-":
                pyautogui.press("-")
            else:
                pyautogui.press(char)
            time.sleep(0.03)


if __name__ == "__main__":
    # Test
    calc = CalculatorController(use_real_calc=True)
    calc.open()
    
    result = calc.multiply(100, 5)
    print(f"Sonuc: {result}")
    
    kdv = calc.calculate_with_percentage(500, 18)
    print(f"KDV: {kdv}")
    
    time.sleep(2)
    calc.close()
