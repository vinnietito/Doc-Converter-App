import os
import subprocess
from pdf2image import convert_from_path

def convert_docx_to_images(docx_path, output_folder):
    # Generate PDF path
    base_filename = os.path.splitext(os.path.basename(docx_path))[0]
    pdf_path = os.path.join(output_folder, f"{base_filename}.pdf")

    # Convert DOCX to PDF using LibreOffice (works on Linux)
    subprocess.run([
        "libreoffice",
        "--headless",
        "--convert-to", "pdf",
        "--outdir", output_folder,
        docx_path
    ], check=True)

    # Convert PDF to images
    images = convert_from_path(pdf_path)

    image_paths = []
    for i, image in enumerate(images):
        image_path = os.path.join(output_folder, f"page_{i+1}.png")
        image.save(image_path, "PNG")
        image_paths.append(image_path)

    return image_paths
