from collections import defaultdict, Counter

# Dataset fittizio
letters = [
    {"sender": "Voltaire", "recipient": "Frederick the Great", "year": 1740, "place_sent": "Cirey", "place_received": "Potsdam"},
    {"sender": "Voltaire", "recipient": "Frederick the Great", "year": 1741, "place_sent": "Cirey", "place_received": "Potsdam"},
    {"sender": "Voltaire", "recipient": "Jean-Jacques Rousseau", "year": 1760, "place_sent": "Ferney", "place_received": "Geneva"},
    {"sender": "Diderot", "recipient": "Catherine the Great", "year": 1773, "place_sent": "Paris", "place_received": "St. Petersburg"},
    {"sender": "Jean-Jacques Rousseau", "recipient": "Diderot", "year": 1755, "place_sent": "Geneva", "place_received": "Paris"},
    {"sender": "Montesquieu", "recipient": "Voltaire", "year": 1748, "place_sent": "Bordeaux", "place_received": "Cirey"},
    {"sender": "Voltaire", "recipient": "Montesquieu", "year": 1749, "place_sent": "Cirey", "place_received": "Bordeaux"},
    {"sender": "Catherine the Great", "recipient": "Diderot", "year": 1774, "place_sent": "St. Petersburg", "place_received": "Paris"},
    {"sender": "Diderot", "recipient": "Voltaire", "year": 1765, "place_sent": "Paris", "place_received": "Ferney"},
    {"sender": "Frederick the Great", "recipient": "Voltaire", "year": 1742, "place_sent": "Potsdam", "place_received": "Cirey"}
]

# Task 1: Letters per decade
def letters_per_decade(data):
    result = defaultdict(int)
    for letter in data:
        decade = (letter['year'] // 10) * 10
        result[f"{decade}s"] += 1
    return dict(result)

# Task 2: Top correspondents (senders + recipients)
def top_correspondents(data, n=5):
    counter = Counter()
    for letter in data:
        counter[letter["sender"]] += 1
        counter[letter["recipient"]] += 1
    return counter.most_common(n)

# Task 3: Communication map (place_sent → set of place_received)
def communication_map(data):
    routes = defaultdict(set)
    for letter in data:
        routes[letter["place_sent"]].add(letter["place_received"])
    return dict(routes)

# Task 4: Pair frequency (undirected, sorted alphabetically)
def pair_frequency(data):
    pairs = defaultdict(int)
    for letter in data:
        pair = tuple(sorted([letter["sender"], letter["recipient"]]))
        pairs[pair] += 1
    return dict(pairs)

# Task 5: City activity (number of letters sent from or received in each city)
def city_activity(data):
    city_counts = defaultdict(int)
    for letter in data:
        city_counts[letter["place_sent"]] += 1
        city_counts[letter["place_received"]] += 1
    return dict(city_counts)

# Task 6 (bonus): Directed graph of correspondents
def correspondence_graph(data):
    graph = defaultdict(lambda: defaultdict(int))
    for letter in data:
        sender = letter["sender"]
        recipient = letter["recipient"]
        graph[sender][recipient] += 1
    return {k: dict(v) for k, v in graph.items()}

# --- Demo ---
if __name__ == "__main__":
    print("Letters per Decade:")
    print(letters_per_decade(letters))

    print("\nTop Correspondents:")
    print(top_correspondents(letters))

    print("\nCommunication Map:")
    print(communication_map(letters))

    print("\nPair Frequency:")
    print(pair_frequency(letters))

    print("\nCity Activity:")
    print(city_activity(letters))

    print("\nDirected Correspondence Graph:")
    print(correspondence_graph(letters))
