from flask import Flask, render_template, request, send_file, redirect, url_for, flash
import os
from utils.image_to_word import convert_image_to_word
from utils.word_to_image import convert_docx_to_images

app = Flask(__name__)
app.secret_key = 'secret-key'
app.config['UPLOAD_FOLDER'] = 'uploads'

# Ensure upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert-image', methods=['POST'])
def image_to_word():
    file = request.files.get('image')
    if file:
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
        filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filename)
        output_folder = os.path.join(app.config['UPLOAD_FOLDER'], 'images')
        os.makedirs(output_folder, exist_ok=True)
        image_paths = convert_docx_to_images(filename, output_folder)
        return render_template('index.html', image_paths=[url_for('static', filename=path.split('static/')[1]) for path in image_paths])
    flash("Please upload a DOCX file.")
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
