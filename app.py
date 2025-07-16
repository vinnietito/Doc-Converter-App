from flask import Flask, render_template, request, send_file, redirect, url_for, flash
import os
import zipfile
import io
from utils.image_to_word import convert_image_to_word
from utils.word_to_image import convert_docx_to_images

app = Flask(__name__)
app.secret_key = 'secret-key'
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['STATIC_IMAGE_FOLDER'] = os.path.join('static', 'converted_images')

# Ensure required folders exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['STATIC_IMAGE_FOLDER'], exist_ok=True)

def clear_folder(folder_path):
    """Delete all files in a given folder."""
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            os.remove(file_path)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert-image', methods=['POST'])
def image_to_word():
    file = request.files.get('image')
    if file:
        clear_folder(app.config['UPLOAD_FOLDER'])  # Clean up before saving
        filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filename)
        output_path = filename + ".docx"
        convert_image_to_word(filename, output_path)
        return send_file(output_path, as_attachment=True)
    flash("Please upload an image.")
    return redirect(url_for('index'))

@app.route('/convert-word', methods=['POST'])
def word_to_image():
    file = request.files.get('docx')
    if file:
        clear_folder(app.config['UPLOAD_FOLDER'])          # Clean uploads
        clear_folder(app.config['STATIC_IMAGE_FOLDER'])    # Clean images

        filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filename)

        output_folder = app.config['STATIC_IMAGE_FOLDER']
        os.makedirs(output_folder, exist_ok=True)

        image_paths = convert_docx_to_images(filename, output_folder)

        # Safely generate URLs for static images
        image_urls = [
            url_for('static', filename=os.path.relpath(path, 'static').replace('\\', '/'))
            for path in image_paths if os.path.exists(path)
        ]

        return render_template('index.html', image_paths=image_urls)

    flash("Please upload a DOCX file.")
    return redirect(url_for('index'))

# ✅ NEW: Route to download all images as ZIP
@app.route('/download-zip')
def download_zip():
    zip_stream = io.BytesIO()
    with zipfile.ZipFile(zip_stream, 'w') as zipf:
        image_dir = app.config['STATIC_IMAGE_FOLDER']
        for filename in os.listdir(image_dir):
            if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
                full_path = os.path.join(image_dir, filename)
                zipf.write(full_path, arcname=filename)
    zip_stream.seek(0)
    return send_file(
        zip_stream,
        as_attachment=True,
        download_name='converted_images.zip',
        mimetype='application/zip'
    )

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=10000)
