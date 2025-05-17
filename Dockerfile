# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set working directory inside the container
WORKDIR /app

# Copy requirements file first (if you have one)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app code
COPY . .

# Expose port 8000 for FastAPI
EXPOSE 8000

# Run the FastAPI app with uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
