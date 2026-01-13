"""
PDF Rapor Olusturucu
====================
Excel'den veri okuyup PDF rapor olusturur.
"""

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from pathlib import Path
from datetime import datetime


class PDFReportGenerator:
    """PDF rapor olusturucu."""
    
    def __init__(self, output_dir: str = "output/reports"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.styles = getSampleStyleSheet()
        
        self.styles.add(ParagraphStyle(
            name='TitleStyle',
            fontSize=24,
            spaceAfter=30,
            alignment=1,
            textColor=colors.HexColor('#2C3E50')
        ))
    
    def create_sales_report(self, title: str, data: list, filename: str = None, company_name: str = "Sirket") -> str:
        """Satis raporu PDF olusturur."""
        if not filename:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"rapor_{timestamp}.pdf"
        
        filepath = self.output_dir / filename
        
        doc = SimpleDocTemplate(str(filepath), pagesize=A4, rightMargin=2*cm, leftMargin=2*cm, topMargin=2*cm, bottomMargin=2*cm)
        elements = []
        
        # Baslik
        elements.append(Paragraph(company_name, self.styles['TitleStyle']))
        elements.append(Paragraph(title, self.styles['Normal']))
        elements.append(Paragraph(f"Tarih: {datetime.now().strftime('%d/%m/%Y %H:%M')}", self.styles['Normal']))
        elements.append(Spacer(1, 20))
        
        # Tablo
        table_data = [["#", "Urun Adi", "Adet", "Birim Fiyat", "Toplam"]]
        grand_total = 0
        
        for i, item in enumerate(data, 1):
            urun = item.get("urun", item.get("Urun Adi", ""))
            adet = item.get("adet", item.get("Adet", 0))
            fiyat = item.get("fiyat", item.get("Birim Fiyat (TL)", 0))
            toplam = float(adet) * float(fiyat)
            grand_total += toplam
            table_data.append([str(i), str(urun), str(adet), f"{float(fiyat):,.2f} TL", f"{toplam:,.2f} TL"])
        
        table_data.append(["", "", "", "TOPLAM:", f"{grand_total:,.2f} TL"])
        
        table = Table(table_data, colWidths=[1.5*cm, 6*cm, 2*cm, 3.5*cm, 3.5*cm])
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#3498DB')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('BACKGROUND', (0, 1), (-1, -2), colors.HexColor('#ECF0F1')),
            ('BACKGROUND', (0, -1), (-1, -1), colors.HexColor('#27AE60')),
            ('TEXTCOLOR', (0, -1), (-1, -1), colors.whitesmoke),
            ('FONTNAME', (0, -1), (-1, -1), 'Helvetica-Bold'),
            ('GRID', (0, 0), (-1, -1), 1, colors.white),
            ('ALIGN', (2, 1), (-1, -1), 'RIGHT'),
            ('TOPPADDING', (0, 0), (-1, -1), 8),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ]))
        
        elements.append(table)
        elements.append(Spacer(1, 30))
        elements.append(Paragraph("Bu rapor otomatik olusturulmustur.", self.styles['Normal']))
        
        doc.build(elements)
        print(f"[PDF] Rapor olusturuldu: {filepath}")
        return str(filepath)


if __name__ == "__main__":
    gen = PDFReportGenerator()
    test_data = [
        {"urun": "Laptop", "adet": 2, "fiyat": 25000},
        {"urun": "Mouse", "adet": 10, "fiyat": 350},
        {"urun": "Klavye", "adet": 5, "fiyat": 750},
    ]
    gen.create_sales_report("Test Raporu", test_data, company_name="Demo Sirket")
