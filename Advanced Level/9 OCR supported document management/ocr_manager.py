import pytesseract
from PIL import Image
import os

# Tesseract yolu (Windows kullanıcıları için)
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def ocr_from_image(image_path):
    try:
        img = Image.open(image_path)
        text = pytesseract.image_to_string(img, lang='tur')
        return text
    except Exception as e:
        return f"Hata: {e}"

def process_documents(folder_path):
    results = {}
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp')):
            path = os.path.join(folder_path, filename)
            print(f"{filename} işleniyor...")
            text = ocr_from_image(path)
            results[filename] = text
    return results

def main():
    folder = input("Dokümanların bulunduğu klasör yolunu girin: ")
    if not os.path.isdir(folder):
        print("Geçerli bir klasör yolu girin.")
        return

    texts = process_documents(folder)
    for file, content in texts.items():
        print(f"\n----- {file} -----\n")
        print(content)
        print("\n-------------------\n")

if __name__ == "__main__":
    main()
