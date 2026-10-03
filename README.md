# Classical Music Recommendation System 🎼

A content-based recommendation system that suggests classical music pieces based on user preferences using metadata features and semantic embeddings.

## Overview

This project recommends similar classical music works by analyzing musical characteristics such as composer, era, form, genre, instrumentation, and other available metadata.

The system supports:
- Searching for a piece or composer
- Finding the closest matching work from user input
- Recommending similar compositions using different approaches
- Providing a simple interactive interface with Streamlit
- Added listening links for recommended pieces

## Features

- Data collection and preprocessing from Open Opus API
- Musical metadata feature engineering
- Exploratory Data Analysis (EDA)
- Content-based recommendation pipeline
- TF-IDF similarity baseline
- Handling Incomplete User Input improvement
- Sentence Transformer embeddings improvement
- Interactive Streamlit web application

## Recommendation Approaches

### 1. TF-IDF Baseline

Musical metadata is transformed into numerical representations using TF-IDF, and similarity between works is calculated using cosine similarity.

### 2. Embedding-based Recommendation

Sentence Transformer embeddings are used to capture semantic similarity between musical descriptions and metadata.

## Project Structure

ClassicalMusicRecommender/
│   
├── app.py # Streamlit application  
├── main.py # Command-line interface    
├── src/ # Recommendation functions  
├── notebooks/ # Data processing and experiments    
├── data/ # Raw and Processed dataset   
├── models/ # Precomputed similarity matrices   
├── requirements.txt    
└── README.md   

## Demo

A Streamlit application allows users to enter a composer or musical piece and receive similar recommendations.

![Classical Music Recommender Demo]
(image/demo.png)

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd ClassicalMusicRecommender
```

Install dependencies:
```bash
pip install -r requirements.txt
```

Run the application:
```bash
streamlit run app.py
```

Future Improvements:    
- Improve recommendations using richer audio features
- Build hybrid recommendation models combining metadata and embeddings
- Add user feedback to personalize recommendations

Author:  
Maryam Zakeri