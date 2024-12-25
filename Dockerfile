# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Install necessary dependencies for Chrome
RUN apt-get update && \
    apt-get install -y wget gnupg2 \
    libnss3 \
    libxss1 \
    libasound2 \
    fonts-liberation \
    libappindicator3-1 \
    libatk-bridge2.0-0 \
    libgtk-3-0 \
    xdg-utils \
    google-chrome-stable && \
    rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /app

# Copy backend requirements and install dependencies
COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy both frontend and backend files to the container
COPY backend/ ./backend/
COPY frontend/ ./frontend/

# Command to run your application
CMD ["python", "backend/app.py"]
