FROM python:3.9-slim

WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Make sure NLTK resources are downloaded during build
RUN python -c "import nltk; nltk.download('stopwords'); nltk.download('punkt')"

# Command to run the application
CMD uvicorn app:app --host 0.0.0.0 --port 7860
