import string
import re
from collections import Counter
import matplotlib.pyplot as plt
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords

# Funzione per elaborare il testo
def process_text(text, language='italian'):
    text = text.lower()
    text = re.sub(r'\d+', '', text)  # Rimuove i numeri
    text = text.translate(str.maketrans('', '', string.punctuation))  # Rimuove la punteggiatura
    words = text.split()
    stop_words = set(stopwords.words(language))
    filtered_words = [word for word in words if word not in stop_words]
    return filtered_words

# Carica i testi
with open("inferno_dante.txt", "r", encoding="utf-8") as f:
    dante_text = f.read()

with open("promessi_sposi.txt", "r", encoding="utf-8") as f:
    manzoni_text = f.read()

# Processa i testi
dante_words = process_text(dante_text)
manzoni_words = process_text(manzoni_text)

# Conta le parole
dante_counter = Counter(dante_words)
manzoni_counter = Counter(manzoni_words)

# Mostra le 10 parole più comuni
print("🔹 Dante - parole più comuni:")
print(dante_counter.most_common(10))

print("\n🔸 Manzoni - parole più comuni:")
print(manzoni_counter.most_common(10))

# Visualizza il confronto
def plot_frequencies(counter, title, color):
    words, counts = zip(*counter.most_common(10))
    plt.bar(words, counts, color=color)
    plt.xticks(rotation=45)
    plt.title(title)
    plt.xlabel("Parole")
    plt.ylabel("Frequenza")
    plt.tight_layout()

plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plot_frequencies(dante_counter, "Dante - Inferno", "skyblue")

plt.subplot(1, 2, 2)
plot_frequencies(manzoni_counter, "Manzoni - I Promessi Sposi", "lightcoral")

plt.show()
