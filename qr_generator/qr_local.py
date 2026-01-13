"""
QR Kod Olusturucu - Yerel Kutuphane
===================================
qrcode + Pillow kullanarak QR kod uretir.
API gerektirmez, offline calisir.
"""

import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer
from qrcode.image.styles.colormasks import SolidFillColorMask
from PIL import Image
from pathlib import Path


# Platform renkleri (RGB)
PLATFORM_COLORS = {
    "instagram": (225, 48, 108),
    "linkedin": (0, 119, 181),
    "twitter": (29, 161, 242),
    "x": (0, 0, 0),
    "youtube": (255, 0, 0),
    "tiktok": (0, 0, 0),
    "github": (36, 41, 46),
    "whatsapp": (37, 211, 102),
    "telegram": (0, 136, 204),
    "facebook": (24, 119, 242),
    "default": (0, 0, 0),
}


def create_qr_code(
    data: str,
    filename: str,
    output_dir: str = "output/qr_codes",
    size: int = 10,
    border: int = 2,
    fill_color: tuple = (0, 0, 0),
    back_color: tuple = (255, 255, 255),
    rounded: bool = True
) -> str:
    """QR kod olusturur ve kaydeder."""
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=size,
        border=border,
    )
    qr.add_data(data)
    qr.make(fit=True)
    
    if rounded:
        img = qr.make_image(
            image_factory=StyledPilImage,
            module_drawer=RoundedModuleDrawer(),
            color_mask=SolidFillColorMask(
                back_color=back_color,
                front_color=fill_color
            )
        )
    else:
        img = qr.make_image(fill_color=fill_color, back_color=back_color)
    
    filepath = Path(output_dir) / f"{filename}.png"
    img.save(filepath)
    
    print(f"[QR] Olusturuldu: {filepath}")
    return str(filepath)


def create_social_media_qr(
    platform: str,
    username: str,
    output_dir: str = "output/qr_codes"
) -> str:
    """Sosyal medya profili icin QR kod olusturur."""
    platform = platform.lower().strip()
    
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
    
    url = url_templates.get(platform, username)
    color = PLATFORM_COLORS.get(platform, PLATFORM_COLORS["default"])
    filename = f"{platform}_{username}"
    
    return create_qr_code(
        data=url,
        filename=filename,
        output_dir=output_dir,
        fill_color=color,
        rounded=True
    )


def create_vcard_qr(
    name: str,
    phone: str = "",
    email: str = "",
    company: str = "",
    title: str = "",
    website: str = "",
    output_dir: str = "output/qr_codes"
) -> str:
    """vCard (kartvizit) QR kodu olusturur."""
    vcard = f"""BEGIN:VCARD
VERSION:3.0
FN:{name}
TEL:{phone}
EMAIL:{email}
ORG:{company}
TITLE:{title}
URL:{website}
END:VCARD"""
    
    filename = f"vcard_{name.replace(' ', '_').lower()}"
    
    return create_qr_code(
        data=vcard.strip(),
        filename=filename,
        output_dir=output_dir,
        fill_color=(0, 0, 0),
        rounded=True
    )


def create_wifi_qr(
    ssid: str,
    password: str,
    security: str = "WPA",
    output_dir: str = "output/qr_codes"
) -> str:
    """WiFi baglanti QR kodu olusturur."""
    wifi_data = f"WIFI:T:{security};S:{ssid};P:{password};;"
    filename = f"wifi_{ssid.replace(' ', '_').lower()}"
    
    return create_qr_code(
        data=wifi_data,
        filename=filename,
        output_dir=output_dir,
        fill_color=(37, 211, 102),
        rounded=True
    )


if __name__ == "__main__":
    print("\n=== QR Kod Test ===\n")
    create_qr_code("https://google.com", "test_google")
    create_social_media_qr("instagram", "test_user")
    print("\n[OK] Testler tamamlandi!")
