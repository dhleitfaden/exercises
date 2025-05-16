Assicurati di avere installato queste librerie (puoi usare pip install matplotlib nltk wordcloud spacy e scaricare il modello italiano spacy con python -m spacy download it_core_news_sm).

➕ (Facoltativo) Analisi del Sentiment
Puoi creare un dizionario di parole con “valori emotivi” e confrontarlo con le parole usate dagli autori.

# Esempio semplice di dizionario emotivo
sentiment_words = {
    "amore": 1, "odio": -1, "pace": 1, "guerra": -1, "felice": 1, "triste": -1
}

def sentiment_analysis(lemmas):
    score = 0
    for lemma in lemmas:
        score += sentiment_words.get(lemma, 0)
    return score

print("💖 Sentiment Dante:", sentiment_analysis(dante_lemmas))
print("💖 Sentiment Manzoni:", sentiment_analysis(manzoni_lemmas))
Puoi naturalmente espandere il dizionario con parole tratte da dizionari emotivi come SentiWordNet, FEEL-IT, o costruirne uno tuo.
