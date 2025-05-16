import string
from collections import Counter
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
import matplotlib.pyplot as plt

# Benutzerdefinierte Funktion zur Textverarbeitung
def bereinige_text(text):
    # Kleinbuchstaben
    text = text.lower()
    # Satzzeichen entfernen
    text = text.translate(str.maketrans('', '', string.punctuation))
    # In Wörter aufteilen
    woerter = text.split()
    # Deutsche Stoppwörter laden
    deutsch_stoppwoerter = set(stopwords.words('german'))
    # Stoppwörter entfernen
    gefiltert = [wort for wort in woerter if wort not in deutsch_stoppwoerter]
    return gefiltert

# Beispieltext laden (du kannst hier auch einen Pfad verwenden)
text = """
Faust: Habe nun, ach! Philosophie, Juristerei und Medizin,
und leider auch Theologie durchaus studiert, mit heißem Bemühn.
Da steh ich nun, ich armer Tor! Und bin so klug als wie zuvor.
"""

# Text verarbeiten
woerter = bereinige_text(text)

# Wortfrequenz berechnen
haeufigkeit = Counter(woerter)

# Ergebnisse anzeigen
print("Gesamtzahl der Wörter (ohne Stoppwörter):", len(woerter))
print("Anzahl eindeutiger Wörter:", len(set(woerter)))
print("\nDie 10 häufigsten Wörter:")
for wort, anzahl in haeufigkeit.most_common(10):
    print(f"{wort}: {anzahl}")

# Optional: Balkendiagramm
def zeige_balkendiagramm(counter):
    haeufigste = counter.most_common(10)
    woerter, werte = zip(*haeufigste)
    plt.bar(woerter, werte, color='skyblue')
    plt.xticks(rotation=45)
    plt.title("Die 10 häufigsten Wörter")
    plt.xlabel("Wort")
    plt.ylabel("Anzahl")
    plt.tight_layout()
    plt.show()

zeige_balkendiagramm(haeufigkeit)
