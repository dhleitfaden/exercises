def digital_humanities_quiz():
    print("Willkommen zum Digital Humanities Quiz!")
    print("Beantworte die Fragen, indem du die Zahl der richtigen Antwort eingibst.\n")

    questions = [
        {
            "question": "1. Was ist eines der Hauptziele der Digital Humanities?",
            "options": [
                "1) Alte Texte digitalisieren",
                "2) Kulturelle Daten mit digitalen Werkzeugen analysieren",
                "3) Software für Videospiele schreiben",
                "4) Inhalte für soziale Medien erstellen"
            ],
            "answer": 2
        },
        {
            "question": "2. Welches dieser Werkzeuge wird häufig in den Digital Humanities verwendet?",
            "options": [
                "1) GIS (Geographisches Informationssystem)",
                "2) Photoshop",
                "3) Excel für Finanzen",
                "4) Blender"
            ],
            "answer": 1
        },
        {
            "question": "3. Wie tragen die Digital Humanities zum Studium von Texten bei?",
            "options": [
                "1) Indem sie Texte in Videos umwandeln",
                "2) Indem sie große Mengen von Texten mit computergestützten Techniken analysieren",
                "3) Indem sie Texte durch Bilder ersetzen",
                "4) Indem sie Romane veröffentlichen"
            ],
            "answer": 2
        },
        {
            "question": "4. Welche Disziplin ist eng mit den Digital Humanities verbunden?",
            "options": [
                "1) Biologie",
                "2) Computerlinguistik",
                "3) Maschinenbau",
                "4) Medizin"
            ],
            "answer": 2
        }
    ]

    score = 0

    for q in questions:
        print(q["question"])
        for option in q["options"]:
            print(option)
        while True:
            try:
                answer = int(input("Deine Antwort: "))
                if answer in [1, 2, 3, 4]:
                    break
                else:
                    print("Bitte gib eine Zahl von 1 bis 4 ein.")
            except ValueError:
                print("Bitte gib eine gültige Zahl ein.")

        if answer == q["answer"]:
            print("Richtige Antwort!\n")
            score += 1
        else:
            print("Falsche Antwort.\n")

    print(f"Quiz beendet! Du hast {score} von {len(questions)} Punkten erreicht.")
    if score == len(questions):
        print("Großartige Arbeit! Du bist ein Experte in Digital Humanities!")
    elif score >= len(questions) / 2:
        print("Gute Arbeit! Du hast ein gutes Wissen über Digital Humanities.")
    else:
        print("Ich empfehle dir, dich mehr mit Digital Humanities zu beschäftigen!")

if __name__ == "__main__":
    digital_humanities_quiz()
