from PIL import Image
import pytesseract
import os

# Tesseract exe yolunu belirtmeniz gerekebilir (Windows için)
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def read_invoice(image_path):
    if not os.path.exists(image_path):
        print(f"Hata: '{image_path}' dosyası bulunamadı.")
        return

    try:
        image = Image.open(image_path)
        text = pytesseract.image_to_string(image, lang='tur')  # Türkçe dil seçeneği
        print("---- Fatura Metni ----")
        print(text)
    except Exception as e:
        print(f"Fatura okunurken hata oluştu: {e}")

def main():
    print("OCR Destekli Fatura Okuma Sistemi")
    invoice_path = input("Fatura dosyasının yolunu giriniz (örnek: invoices/example_invoice.png): ")
    read_invoice(invoice_path)

if __name__ == "__main__":
    main()
