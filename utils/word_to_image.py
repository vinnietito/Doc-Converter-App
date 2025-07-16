from docx import Document
from PIL import Image, ImageDraw, ImageFont
import os
import textwrap

def convert_docx_to_images(docx_path, output_folder):
    doc = Document(docx_path)
    full_text = "\n".join([para.text for para in doc.paragraphs])

    # Create an image (white background)
    img = Image.new('RGB', (800, 1000), color='white')
    draw = ImageDraw.Draw(img)
    font = ImageFont.load_default()

    # Wrap text so it doesn't overflow
    lines = textwrap.wrap(full_text, width=90)
    y = 20
    for line in lines:
        draw.text((20, y), line, fill='black', font=font)
        y += 20

    os.makedirs(output_folder, exist_ok=True)
    image_path = os.path.join(output_folder, 'page_1.png')
    img.save(image_path)

    return [image_path]
