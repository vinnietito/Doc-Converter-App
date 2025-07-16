from PIL import Image
import pytesseract
from docx import Document
import platform
import os

# 🧠 Set tesseract path conditionally based on OS
if platform.system() == "Windows":
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
else:
    # Linux systems (e.g., Render) just need tesseract installed in system PATH
    pytesseract.pytesseract.tesseract_cmd = "tesseract"

def convert_image_to_word(image_path, output_path):
    try:
        text = pytesseract.image_to_string(Image.open(image_path))
        doc = Document()
        doc.add_paragraph(text)
        doc.save(output_path)
    except Exception as e:
        print(f"[ERROR] Failed to convert image: {e}")
        raise
