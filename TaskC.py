from sentence_transformers import SentenceTransformer, util
import csv

# Load the Sentence Transformer model
# Choose a lightweight model if you have limited hardware resources
model = SentenceTransformer('all-MiniLM-L6-v2')

# Create a function to encode movie titles
def encode_movie_titles(csv_file_path):
    titles = []
    embeddings = []

    # Read movie titles from CSV
    with open(csv_file_path, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            title = row["Series_Title"]  # Ensure this matches the CSV column
            titles.append(title)
            embeddings.append(model.encode(title))  # Encode each title

    return titles, embeddings

# Perform semantic search
def semantic_search(query, titles, embeddings, top_k=10):
    query_embedding = model.encode(query)  # Encode the query
    scores = util.dot_score(query_embedding, embeddings).cpu().numpy()[0]  # Compute similarity scores

    # Pair titles with scores and sort them by score in descending order
    results = sorted(zip(titles, scores), key=lambda x: x[1], reverse=True)

    return results[:top_k]  # Return top-k results

# Example usage
csv_file_path = "data/imdb_top_1000.csv"  # Path to the CSV file
titles, embeddings = encode_movie_titles(csv_file_path)  # Encode all movie titles

query = "dream sharing technology"  # Example query
results = semantic_search(query, titles, embeddings)

# Print top results
print("Search Results:")
for title, score in results:
    print(f"{title}: {score:.2f}")
