import os
from docx2pdf import convert
from pdf2image import convert_from_path

def convert_docx_to_images(docx_path, output_folder):
    # Convert DOCX to PDF
    pdf_path = os.path.join(output_folder, "temp.pdf")
    convert(docx_path, pdf_path)

    # Convert PDF to images
    images = convert_from_path(pdf_path, poppler_path=r"C:\Program Files\Poppler\poppler-24.08.0\Library\bin")

    image_paths = []
    for i, img in enumerate(images):
        image_path = os.path.join(output_folder, f"page_{i + 1}.png")
        img.save(image_path, "PNG")
        image_paths.append(image_path)

    return image_paths
