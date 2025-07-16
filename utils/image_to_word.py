from PIL import Image
import pytesseract
from docx import Document

def convert_image_to_word(image_path, output_path):
    text = pytesseract.image_to_string(Image.open(image_path))
    doc = Document()
    doc.add_paragraph(text)
    doc.save(output_path)
