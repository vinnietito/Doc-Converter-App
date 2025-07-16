FROM python:3.11-slim

# Install system packages (LibreOffice and fonts)
RUN apt-get update && \
    apt-get install -y libreoffice poppler-utils fonts-dejavu && \
    apt-get clean

# Set workdir
WORKDIR /app

# Copy files
COPY . .

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose port
EXPOSE 8000

# Start the app using gunicorn
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:8000"]
