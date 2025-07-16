# Use official Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install system dependencies (incl. tesseract-ocr)
RUN apt-get update && \
    apt-get install -y tesseract-ocr libglib2.0-0 libsm6 libxext6 libxrender-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Copy project files
COPY . /app

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose a generic port (Render injects the real one)
EXPOSE 8080

# ✅ Fix: Start Flask app using Render's assigned port
CMD ["sh", "-c", "waitress-serve --host=0.0.0.0 --port=${PORT} app:app"]
