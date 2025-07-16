import os
import pythoncom
from docx2pdf import convert
from pdf2image import convert_from_path

def convert_docx_to_images(docx_path, output_folder):
    # Initialize COM for Word Automation
    pythoncom.CoInitialize()

    # Add Poppler bin to PATH (TEMPORARY fix)
    os.environ["PATH"] += os.pathsep + r"C:\Program Files\Poppler\poppler-24.08.0\Library\bin"  # 🔁 Edit this path

    # Convert DOCX to PDF
    base_filename = os.path.splitext(os.path.basename(docx_path))[0]
    pdf_path = os.path.join(output_folder, base_filename + '.pdf')
    convert(docx_path, pdf_path)

    # Convert PDF to PNG images
    images = convert_from_path(pdf_path)

    image_paths = []
    for i, image in enumerate(images):
        image_path = os.path.join(output_folder, f'page_{i+1}.png')
        image.save(image_path, 'PNG')
        image_paths.append(image_path)

    return image_paths
