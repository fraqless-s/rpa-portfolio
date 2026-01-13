"""
Keyboard Utility - Klavye yardımcı fonksiyonları
"""

import time
import pyautogui
import pyperclip


def safe_type(text: str, interval: float = 0.05):
    """Türkçe karakter destekli yazma."""
    pyperclip.copy(text)
    pyautogui.hotkey("ctrl", "v")
    time.sleep(0.1)


def press_key(key: str, times: int = 1, delay: float = 0.1):
    """Tuşa belirli sayıda basar."""
    for _ in range(times):
        pyautogui.press(key)
        time.sleep(delay)


def hotkey(*keys, delay: float = 0.1):
    """Kısayol tuşu kombinasyonu."""
    pyautogui.hotkey(*keys)
    time.sleep(delay)


def wait_and_click(seconds: float = 0.5):
    """Bekler ve mevcut konuma tıklar."""
    time.sleep(seconds)
    pyautogui.click()
