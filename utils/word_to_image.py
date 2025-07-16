import os
import pythoncom
from docx2pdf import convert
from pdf2image import convert_from_path

def convert_docx_to_images(docx_path, output_folder):
    # Ensure COM is initialized
    pythoncom.CoInitialize()

    # Step 1: Convert DOCX to PDF
    base_filename = os.path.splitext(os.path.basename(docx_path))[0]
    pdf_path = os.path.join(output_folder, base_filename + '.pdf')
    convert(docx_path, pdf_path)

    # Step 2: Convert PDF to images
    images = convert_from_path(pdf_path)

    image_paths = []
    for i, image in enumerate(images):
        image_path = os.path.join(output_folder, f'page_{i+1}.png')
        image.save(image_path, 'PNG')
        image_paths.append(image_path)

    return image_paths
