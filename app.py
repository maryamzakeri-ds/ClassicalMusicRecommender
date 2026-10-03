import pandas as pd
import streamlit as st
import urllib.parse
from src.recommendation import find_best_match, recommend_embedding, recommend_tfidf

st.title('Classical Music Recommender')
query = st.text_input('What is your favorite classical music or composer?')
method = st.selectbox('Recommendation method', ['TF-IDF', 'Embeddings'])

if st.button('Recommend'):
    match = find_best_match(query)

    if match['score'] < 50:
        st.write('No matching work was found. Try another query.')
    else:
        st.subheader('Reference work')
        st.write(f"**{match['title']} — {match['composer_name']}**")

        if method == 'TF-IDF':
            recommendations = recommend_tfidf(match['index'])
        else:
            recommendations = recommend_embedding(match['index'])

        st.subheader('Recommended Works')

        for _, row in recommendations.iterrows():
            row = row.fillna('Unknown')
            st.markdown(f"### {row['title']}")
            st.write(f"**Composer:** {row['composer_name']}")

            col1, col2 = st.columns(2)

            with col1:
                st.write(f"**Epoch:** {row['epoch']}")
                st.write(f"**Form:** {row['form']}")
                st.write(f"**Genre:** {row['extended_genre']}")

            with col2:
                st.write(f"**Instrumentation:** {row['instrumentation']}")
                st.write(f"**Mode:** {row['mode']}")
                st.write(f"**Tempo:** {row['tempo_marking']}")

            search_query = f"{row['composer_name']} {row['title']}"
            youtube_url = (
                    "https://www.youtube.com/results?search_query="
                    + urllib.parse.quote(search_query)
            )

            st.link_button("🎧 Listen", youtube_url)

            st.divider()

