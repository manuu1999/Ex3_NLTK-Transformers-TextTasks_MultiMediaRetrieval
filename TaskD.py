from collections import defaultdict
from unidecode import unidecode

def generate_ngrams(text, n=3):
    text = unidecode(text.lower())
    text = f"<{text}>"
    return [text[i:i+n] for i in range(len(text) - n + 1)]

def train_naive_bayes(language_texts, n=3, top_n=1000):
    likelihoods = {}
    for lang, texts in language_texts.items():
        ngram_counts = Counter()
        for text in texts:
            ngram_counts.update(generate_ngrams(text, n))
        top_ngrams = dict(ngram_counts.most_common(top_n))
        likelihoods[lang] = top_ngrams
    return likelihoods

def predict_language(text, likelihoods, n=3):
    ngrams = generate_ngrams(text, n)
    scores = {lang: 0 for lang in likelihoods}
    for lang, ngram_likelihoods in likelihoods.items():
        for ngram in ngrams:
            if ngram in ngram_likelihoods:
                scores[lang] += ngram_likelihoods[ngram]
    return max(scores, key=scores.get)

# Example usage
language_texts = {
    'english': ["Hello world", "This is an English text."],
    'german': ["Hallo Welt", "Das ist ein deutscher Text."],
    'italian': ["Ciao mondo", "Questo è un testo italiano."]
}
likelihoods = train_naive_bayes(language_texts)
text = "Ciao, come va?"
print("Predicted Language:", predict_language(text, likelihoods))
