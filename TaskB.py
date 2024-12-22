import csv
from unidecode import unidecode
from collections import Counter

# Tokenize text into n-grams
def tokenize_to_ngrams(text, n=3):
    text = unidecode(text.lower())  # Normalize text
    text = f"<{text}>"  # Add start and end markers
    return [text[i:i + n] for i in range(len(text) - n + 1)]

# Create an index of movie titles
def create_title_index(csv_file_path, n=3):
    index = {}
    with open(csv_file_path, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            title = row["Series_Title"]  # Use the correct column name
            ngrams = set(tokenize_to_ngrams(title, n))
            index[title] = ngrams
    return index

# Search for titles using n-grams
def search_titles(query, index, n=3):
    query_ngrams = set(tokenize_to_ngrams(query, n))
    results = {}
    for title, ngrams in index.items():
        # Calculate Jaccard similarity
        similarity = len(query_ngrams & ngrams) / len(query_ngrams | ngrams)
        results[title] = similarity
    # Sort by similarity
    return sorted(results.items(), key=lambda x: x[1], reverse=True)

# Example usage
csv_file_path = "data/imdb_top_1000.csv"  # Path to the CSV file
index = create_title_index(csv_file_path, n=3)  # Build the index
query = "Shwshank"  # Query with typo
results = search_titles(query, index)

# Print top 10 results
print("Search Results:")
for title, similarity in results[:10]:  # Display top 10 results
    print(f"{title}: {similarity:.2f}")
