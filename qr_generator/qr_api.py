"""
QR Kod Olusturucu - API Client
==============================
goqr.me API kullanarak QR kod uretir.
Ucretsiz, API key gerektirmez.
"""

import requests
from pathlib import Path


API_BASE_URL = "https://api.qrserver.com/v1/create-qr-code/"


def create_qr_via_api(
    data: str,
    filename: str,
    output_dir: str = "output/qr_codes",
    size: int = 300,
    color: str = "000000",
    bgcolor: str = "ffffff",
    format: str = "png"
) -> str:
    """
    goqr.me API kullanarak QR kod olusturur.
    
    Args:
        data: QR icerigi (URL, metin, vs.)
        filename: Dosya adi (uzantisiz)
        output_dir: Cikti klasoru
        size: Piksel boyutu (max 1000)
        color: QR rengi (hex, # olmadan)
        bgcolor: Arkaplan rengi (hex)
        format: png veya svg
    
    Returns:
        Kaydedilen dosyanin yolu
    """
    # Cikti klasorunu olustur
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    
    # API parametreleri
    params = {
        "data": data,
        "size": f"{size}x{size}",
        "color": color,
        "bgcolor": bgcolor,
        "format": format,
        "qzone": 2,  # Kenar boslugu
        "charset-source": "UTF-8",
    }
    
    print(f"[API] QR olusturuluyor: {data[:50]}...")
    
    try:
        response = requests.get(API_BASE_URL, params=params, timeout=10)
        response.raise_for_status()
        
        # Dosyaya kaydet
        filepath = Path(output_dir) / f"{filename}.{format}"
        with open(filepath, "wb") as f:
            f.write(response.content)
        
        print(f"[API] Olusturuldu: {filepath}")
        return str(filepath)
        
    except requests.exceptions.RequestException as e:
        print(f"[API] Hata: {e}")
        return None


def create_social_qr_api(
    platform: str,
    username: str,
    output_dir: str = "output/qr_codes"
) -> str:
    """
    Sosyal medya QR kodu API ile olusturur.
    """
    platform = platform.lower().strip()
    
    # Platform URL'leri
    url_templates = {
        "instagram": f"https://instagram.com/{username}",
        "linkedin": f"https://linkedin.com/in/{username}",
        "twitter": f"https://twitter.com/{username}",
        "x": f"https://x.com/{username}",
        "youtube": f"https://youtube.com/@{username}",
        "tiktok": f"https://tiktok.com/@{username}",
        "github": f"https://github.com/{username}",
        "whatsapp": f"https://wa.me/{username}",
        "telegram": f"https://t.me/{username}",
        "facebook": f"https://facebook.com/{username}",
    }
    
    # Platform renkleri (hex)
    colors = {
        "instagram": "E1306C",
        "linkedin": "0077B5",
        "twitter": "1DA1F2",
        "x": "000000",
        "youtube": "FF0000",
        "tiktok": "000000",
        "github": "24292E",
        "whatsapp": "25D366",
        "telegram": "0088CC",
        "facebook": "1877F2",
    }
    
    url = url_templates.get(platform, username)
    color = colors.get(platform, "000000")
    filename = f"{platform}_{username}_api"
    
    return create_qr_via_api(
        data=url,
        filename=filename,
        output_dir=output_dir,
        color=color
    )


if __name__ == "__main__":
    # Test
    print("\n=== API QR Test ===\n")
    
    create_qr_via_api(
        data="https://google.com",
        filename="test_api_google"
    )
    
    create_social_qr_api("github", "test_user")
    
    print("\n[OK] API testleri tamamlandi!")
