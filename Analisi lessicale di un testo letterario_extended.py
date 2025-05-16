import string
import re
import spacy
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords

# Carica Spacy italiano
nlp = spacy.load("it_core_news_sm")

# Funzione per elaborare il testo
def process_text(text, language='italian'):
    text = text.lower()
    text = re.sub(r'\d+', '', text)
    text = text.translate(str.maketrans('', '', string.punctuation))
    doc = nlp(text)
    lemmas = [token.lemma_ for token in doc if token.is_alpha and token.lemma_ not in stopwords.words(language)]
    return lemmas

# Carica i testi
with open("inferno_dante.txt", "r", encoding="utf-8") as f:
    dante_text = f.read()

with open("promessi_sposi.txt", "r", encoding="utf-8") as f:
    manzoni_text = f.read()

# Processa e lemmatizza
dante_lemmas = process_text(dante_text)
manzoni_lemmas = process_text(manzoni_text)

# Conta le parole
dante_counter = Counter(dante_lemmas)
manzoni_counter = Counter(manzoni_lemmas)

# Word Cloud
def generate_wordcloud(counter, title):
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(counter)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.title(title)
    plt.show()

generate_wordcloud(dante_counter, "Word Cloud - Dante")
generate_wordcloud(manzoni_counter, "Word Cloud - Manzoni")
