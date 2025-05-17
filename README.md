---
title: Spam Detector
emoji: 🛡️
colorFrom: blue
colorTo: green
sdk: docker
sdk_version: "0.104.1"
app_file: app.py
pinned: false
---

# Spam Message Detector

A Natural Language Processing (NLP) and machine learning web application built with FastAPI that detects whether a message is spam or not with 98% accuracy.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Machine Learning Model](#machine-learning-model)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Model Performance](#model-performance)
- [Technologies Used](#technologies-used)
- [Future Improvements](#future-improvements)

## Overview

This web application leverages Natural Language Processing (NLP) techniques and a trained Random Forest classifier to determine whether a given text message is spam or legitimate. The model uses Bag of Words (BOW) with n-grams and custom stopword removal to achieve high accuracy.

## Features

- Clean, simple web interface for message submission
- Real-time spam detection with high accuracy
- FastAPI backend for speedy processing
- Pre-trained model with 98% accuracy rate
- Custom stopword handling for enhanced performance

## Machine Learning Model

The spam detection model was built using the following approach:

1. **Text Preprocessing**:
   - Custom stopwords removal (keeping negation words)
   - Text normalization and stemming using Porter Stemmer
   - Regular expression to filter out non-alphanumeric characters

2. **Feature Engineering**:
   - Bag of Words (BOW) representation
   - N-grams (1-2) to capture phrase context
   - Maximum of 2500 features to optimize performance

3. **Model Selection**:
   - Random Forest Classifier was selected due to its exceptional performance
   - 98% accuracy on test data
   - Excellent precision and recall metrics

## Project Structure

```
spam-detector/
│
├── models/
│   └── spam_model.pkl           # Trained Random Forest model
│
├── cv/
│   └── count_vectorizer.pkl     # Fitted CountVectorizer for text transformation
│
├── templates/
│   └── index.html               # Frontend HTML template
│
├── static/
│   ├── css/                     # CSS styling files
│   └── js/                      # JavaScript files (if any)
│
├── app.py                       # FastAPI application
└── README.md                    # This file
```

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/spam-detection-app.git
   cd spam-detection-app
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Download NLTK resources:
   ```python
   import nltk
   nltk.download('stopwords')
   nltk.download('punkt')
   ```

## Usage

1. Start the FastAPI server using uvicorn:
   ```
   uvicorn app:app --reload --port 8000
   ```

2. Open your browser and navigate to:
   ```
   http://127.0.0.1:8000/
   ```

3. Enter a message in the input field and click "Submit" to see the prediction.

## API Endpoints

- `GET /` - Displays the home page with the message input form
- `POST /predict` - Accepts a message and returns the prediction (Spam/Not Spam)

## Model Performance

The Random Forest model achieved:
- **Accuracy**: 98.5%
- **Confusion Matrix**:
  ```
  [[955   0]
   [ 17 143]]
  ```
- **Classification Report**:
  ```
             precision    recall  f1-score   support
          0       0.98      1.00      0.99       955
          1       1.00      0.89      0.94       160
  ```

This indicates that:
- The model correctly identified all legitimate messages (955/955)
- The model correctly identified 89% of spam messages (143/160)
- 17 spam messages were incorrectly classified as legitimate (false negatives)
- No legitimate messages were incorrectly classified as spam (false positives)

## Technologies Used

- **Backend**: FastAPI
- **Frontend**: HTML, Jinja2 templates
- **Machine Learning**: scikit-learn, NLTK
- **Natural Language Processing (NLP)**: Text preprocessing, tokenization, stemming, stopword removal
- **Data Processing**: Pandas, NumPy
- **Model Serialization**: Pickle

## Future Improvements

- Add more styling to enhance the UI
- Create a dashboard with visualization of results
- Add batch processing capabilities
- Deploy the application to a cloud platform
- Implement confidence scores for predictions
- Add model retraining functionality with new data