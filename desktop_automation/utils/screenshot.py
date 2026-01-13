"""
Screenshot Utility - Ekran görüntüsü alma ve karşılaştırma
"""

import pyautogui
from pathlib import Path
from datetime import datetime


def take_screenshot(name: str = None, output_dir: str = "output/screenshots") -> str:
    """Ekran görüntüsü alır ve kaydeder."""
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{name}_{timestamp}.png" if name else f"screenshot_{timestamp}.png"
    filepath = Path(output_dir) / filename
    
    screenshot = pyautogui.screenshot()
    screenshot.save(filepath)
    
    print(f"[SCREENSHOT] Kaydedildi: {filepath}")
    return str(filepath)


def take_region_screenshot(x: int, y: int, width: int, height: int, 
                           name: str = None, output_dir: str = "output/screenshots") -> str:
    """Belirli bir bölgenin ekran görüntüsünü alır."""
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{name}_{timestamp}.png" if name else f"region_{timestamp}.png"
    filepath = Path(output_dir) / filename
    
    screenshot = pyautogui.screenshot(region=(x, y, width, height))
    screenshot.save(filepath)
    
    print(f"[SCREENSHOT] Bölge kaydedildi: {filepath}")
    return str(filepath)


if __name__ == "__main__":
    # Test
    path = take_screenshot("test")
    print(f"Screenshot saved: {path}")
