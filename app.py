import pickle
import pandas as pd
import numpy as np
import uvicorn
import os
import nltk
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from sklearn.feature_extraction.text import CountVectorizer

# Download NLTK resources (required for Hugging Face)
nltk_data_dir = "./nltk_data"
nltk.download('stopwords', download_dir=nltk_data_dir)
nltk.download('punkt', download_dir=nltk_data_dir)
os.environ['NLTK_DATA'] = nltk_data_dir

# Setting up FastAPI as backend framework
app = FastAPI()

# Setting up Jinja2 templates for rendering HTML
templates = Jinja2Templates(directory="templates")

# Setting up static files for CSS and JS
app.mount("/static", StaticFiles(directory="static"), name="static")

# Opening pickle file containing the trained ML Model and vectorizer
# Choosen model is Random Forest
ml_model = pickle.load(open('models/spam_model.pkl', 'rb'))
vectorizer_model = pickle.load(open('cv/count_vectorizer.pkl', 'rb'))

# Home page route
@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Prediction route
@app.post("/predict", response_class=HTMLResponse)
async def predict_api(request: Request, message: str = Form(...)):
    # Converting text to vector 
    transformed_message=vectorizer_model.transform([message]).toarray()
    # Predicting Vectorised data using ML Model
    prediction = ml_model.predict(transformed_message)
    prediction_label="Spam" if prediction[0] else "Not Spam"
    return templates.TemplateResponse("index.html", {"request": request, "prediction_text": prediction_label})

if __name__ == "__main__":
    port = int(os.getenv("PORT", 7860))
    uvicorn.run(app, host="0.0.0.0", port=port)
