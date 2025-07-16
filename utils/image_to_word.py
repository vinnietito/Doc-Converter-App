from PIL import Image
import pytesseract
from docx import Document

# 👉 Set path to your actual tesseract.exe
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def convert_image_to_word(image_path, output_path):
    text = pytesseract.image_to_string(Image.open(image_path))
    doc = Document()
    doc.add_paragraph(text)
    doc.save(output_path)
