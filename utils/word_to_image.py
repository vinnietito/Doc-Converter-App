import os
import subprocess
from pdf2image import convert_from_path

def convert_docx_to_images(docx_path, output_folder):
    # Ensure output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # Convert DOCX to PDF using LibreOffice
    base_filename = os.path.splitext(os.path.basename(docx_path))[0]
    pdf_path = os.path.join(output_folder, base_filename + '.pdf')

    try:
        subprocess.run([
            "libreoffice",
            "--headless",
            "--convert-to", "pdf",
            "--outdir", output_folder,
            docx_path
        ], check=True)
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"LibreOffice conversion failed: {e}")

    # Convert the PDF to PNG images
    images = convert_from_path(pdf_path)
    image_paths = []

    for i, image in enumerate(images):
        image_path = os.path.join(output_folder, f'page_{i+1}.png')
        image.save(image_path, 'PNG')
        image_paths.append(image_path)

    return image_paths
