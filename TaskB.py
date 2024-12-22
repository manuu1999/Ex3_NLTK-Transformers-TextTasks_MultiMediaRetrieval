from unidecode import unidecode
from collections import Counter

def tokenize_to_ngrams(text, n=3):
    text = unidecode(text.lower())
    text = f"<{text}>"
    return [text[i:i+n] for i in range(len(text) - n + 1)]

def create_title_index(movie_titles, n=3):
    index = {}
    for title in movie_titles:
        ngrams = set(tokenize_to_ngrams(title, n))
        index[title] = ngrams
    return index

def search_titles(query, index, n=3):
    query_ngrams = set(tokenize_to_ngrams(query, n))
    results = {}
    for title, ngrams in index.items():
        similarity = len(query_ngrams & ngrams) / len(query_ngrams | ngrams)
        results[title] = similarity
    return sorted(results.items(), key=lambda x: x[1], reverse=True)

# Example usage
titles = ["The Shawshank Redemption", "The Godfather", "The Dark Knight"]
index = create_title_index(titles, n=3)
query = "Shwshank"
print("Search Results:", search_titles(query, index))
