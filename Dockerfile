# Use a lightweight Python base image
FROM python:3.10-slim

# Install system dependencies: tesseract and libreoffice
RUN apt-get update && \
    apt-get install -y \
    tesseract-ocr \
    libreoffice \
    poppler-utils \
    && apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Copy all project files into the container
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port
EXPOSE 10000

# Run the app with Gunicorn
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:10000"]
