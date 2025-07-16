from PIL import Image
import pytesseract
from docx import Document
import platform

# ✅ Only set tesseract path if running on Windows
if platform.system() == "Windows":
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
# ⛔️ Do NOT override on Linux — use system PATH

def convert_image_to_word(image_path, output_path):
    try:
        text = pytesseract.image_to_string(Image.open(image_path))
        doc = Document()
        doc.add_paragraph(text)
        doc.save(output_path)
    except Exception as e:
        print(f"[ERROR] Failed to convert image: {e}")
        raise
