from src.recommendation import recommend_embedding, recommend_tfidf, find_best_match

query = input('Enter your favorite musical work: ')

tfidf_result = recommend_tfidf(find_best_match(query)['index'])
print('We think you would also enjoy: (TFIDF Method)')
print(tfidf_result[['title', 'composer_name']].to_string(index=False))

print()

embedding_result = recommend_embedding(find_best_match(query)['index'])
print('We think you would also enjoy: (Embedding Method)')
print(embedding_result[['title', 'composer_name']].to_string(index=False))
