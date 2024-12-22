from sentence_transformers import SentenceTransformer, util

# Load the model
model = SentenceTransformer('all-MiniLM-L6-v2')

def encode_titles(titles):
    return {title: model.encode(title) for title in titles}

def semantic_search(query, encoded_titles):
    query_embedding = model.encode(query)
    results = {}
    for title, embedding in encoded_titles.items():
        similarity = float(util.cos_sim(query_embedding, embedding))
        results[title] = similarity
    return sorted(results.items(), key=lambda x: x[1], reverse=True)

# Example usage
titles = ["The Shawshank Redemption", "The Godfather", "The Dark Knight"]
encoded_titles = encode_titles(titles)
query = "Redemption"
print("Semantic Search Results:", semantic_search(query, encoded_titles))
