import os
from pdf2image import convert_from_path
from docx2pdf import convert

def convert_docx_to_images(docx_path, output_folder):
    pdf_path = docx_path.replace(".docx", ".pdf")
    convert(docx_path, pdf_path)

    images = convert_from_path(pdf_path)
    image_paths = []

    for i, img in enumerate(images):
        img_path = os.path.join(output_folder, f"page_{i+1}.png")
        img.save(img_path, 'PNG')
        image_paths.append(img_path)

    return image_paths
