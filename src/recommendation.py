
import joblib
import re
from rapidfuzz import process, fuzz
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

similarity_matrix = joblib.load(BASE_DIR/'models'/'similarity_matrix.pkl')
embedding_similarity_matrix = joblib.load(BASE_DIR/'models'/'embedding_similarity_matrix.pkl')
data = pd.read_csv(BASE_DIR/'data'/'processed'/'classical_music_feature_engineered.csv')
data['search_text'] = (
        data['title'].fillna('') + ' ' + data['composer_name'].fillna('') + ' ' +data['form'].fillna('')
)

def normalize(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

data['search_text'] = data['search_text'].apply(normalize)

def find_best_match(query):
    query = normalize(query)

    composers = data['composer_name'].dropna().unique()
    forms = data['form'].dropna().unique()

    search_df = data

    matched_composer = None
    for composer in composers:
        if normalize(composer) in query:
            matched_composer = composer
            break

    if matched_composer:
        search_df = search_df[
            search_df['composer_name'] == matched_composer
        ]

    matched_form = None
    for form in forms:
        if normalize(form) in query:
            matched_form = form
            break

    if matched_form:
        search_df = search_df[
            search_df['form'] == matched_form
        ]

    match = process.extractOne(
        query,
        search_df['search_text'],
        scorer=fuzz.token_set_ratio
    )

    if match is None:
        return None

    matched_text, score, index = match

    return {
        'index': index,
        'title': data.loc[index, 'title'],
        'composer_name': data.loc[index, 'composer_name'],
        'score': score,
    }

def recommend_tfidf(index, n=5):
    # index = find_best_match(query)['index']

    similarity_scores = list(enumerate(similarity_matrix[index]))
    similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)
    similarity_scores = similarity_scores[1:n+1]

    recommended_indices = [i[0] for i in similarity_scores]
    return data.loc[recommended_indices, ['title', 'composer_name','epoch', 'form',
                    'extended_genre', 'instrumentation', 'mode', 'tempo_marking']]


def recommend_embedding(index, n=5):
    # index = find_best_match(query)['index']

    similarity_scores = list(enumerate(embedding_similarity_matrix[index]))
    similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)
    similarity_scores = similarity_scores[1:n+1]

    recommended_indices = [i[0] for i in similarity_scores]
    return data.loc[recommended_indices, ['title', 'composer_name','epoch', 'form',
                    'extended_genre', 'instrumentation', 'mode', 'tempo_marking']]

