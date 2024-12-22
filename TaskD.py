from collections import Counter
from unidecode import unidecode


# Function to generate n-grams
def generate_ngrams(text, n=3):
    text = unidecode(text.lower())
    text = f"<{text}>"  # Add start and end markers
    return [text[i:i + n] for i in range(len(text) - n + 1)]


# Function to train Naive Bayes likelihoods for multiple languages
def train_naive_bayes(language_texts, n=3, top_n=1000):
    likelihoods = {}
    for lang, texts in language_texts.items():
        ngram_counts = Counter()
        for text in texts:
            ngram_counts.update(generate_ngrams(text, n))
        # Select top-n n-grams for the language
        top_ngrams = dict(ngram_counts.most_common(top_n))
        likelihoods[lang] = top_ngrams
    return likelihoods


# Function to predict language based on learned likelihoods
def predict_language(text, likelihoods, n=3):
    ngrams = generate_ngrams(text, n)
    scores = {lang: 0 for lang in likelihoods}

    for lang, ngram_likelihoods in likelihoods.items():
        for ngram in ngrams:
            if ngram in ngram_likelihoods:
                scores[lang] += ngram_likelihoods[ngram]

    return max(scores, key=scores.get)


# Example usage
if __name__ == "__main__":
    # Example texts for training
    language_texts = {
        'english': ["Hello world", "This is an example of English text."],
        'german': ["Hallo Welt", "Das ist ein Beispieltext in Deutsch."],
        'italian': ["Ciao mondo", "Questo è un esempio di testo in italiano."]
    }

    # Train Naive Bayes likelihoods
    likelihoods = train_naive_bayes(language_texts, n=3, top_n=100)

    # Input text for prediction
    text = "buongiorno."
    text2 = "hello"
    text3 = "Hallo"

    predicted_language = predict_language(text, likelihoods)
    predicted_language2 = predict_language(text2, likelihoods)
    predicted_language3 = predict_language(text3, likelihoods)

    print("Predicted Language:", predicted_language)
    print("Predicted Language:", predicted_language2)
    print("Predicted Language:", predicted_language3)

