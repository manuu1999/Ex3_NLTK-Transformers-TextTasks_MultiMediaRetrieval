import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download stopwords and punkt tokenizer
nltk.download('stopwords')
nltk.download('punkt')


def detect_language(text):
    languages = ['english', 'german', 'italian']
    stopwords_count = {}

    # Tokenize the input text
    tokens = word_tokenize(text.lower())

    for language in languages:
        lang_stopwords = set(stopwords.words(language))
        stopwords_count[language] = sum(1 for word in tokens if word in lang_stopwords)

    detected_language = max(stopwords_count, key=stopwords_count.get)
    return detected_language


# Example usage
text = "Ciao, come stai? Questo è un esempio di testo in italiano."
print("Detected Language:", detect_language(text))
