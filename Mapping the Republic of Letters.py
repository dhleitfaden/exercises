import os
import json
import csv

# Directory structure
base_path = "republic_of_letters"
directories = [
    os.path.join(base_path, "data"),
    os.path.join(base_path, "src"),
    os.path.join(base_path, "notebooks"),
]

files = {
    "src/data_loader.py": '''\
import pandas as pd

def load_data(filepath):
    df = pd.read_csv(filepath)
    df.dropna(inplace=True)
    return df
''',

    "src/timeline_analysis.py": '''\
import pandas as pd
import matplotlib.pyplot as plt

def letters_per_decade(df):
    df['decade'] = (df['year'] // 10) * 10
    return df.groupby('decade').size()

def plot_letters_per_decade(df):
    counts = letters_per_decade(df)
    counts.plot(kind='bar', title='Letters per Decade')
    plt.xlabel('Decade')
    plt.ylabel('Number of Letters')
    plt.tight_layout()
    plt.show()
''',

    "src/network_builder.py": '''\
import networkx as nx

def build_network(df):
    G = nx.DiGraph()
    for _, row in df.iterrows():
        sender = row['sender']
        recipient = row['recipient']
        if G.has_edge(sender, recipient):
            G[sender][recipient]['weight'] += 1
        else:
            G.add_edge(sender, recipient, weight=1)
    return G
''',

    "src/map_visualizer.py": '''\
import folium

def create_map(df):
    m = folium.Map(location=[48.8566, 2.3522], zoom_start=4)
    for _, row in df.iterrows():
        folium.Marker(location=[row['lat_sent'], row['lon_sent']],
                      popup=f"From: {row['place_sent']}").add_to(m)
        folium.Marker(location=[row['lat_received'], row['lon_received']],
                      popup=f"To: {row['place_received']}").add_to(m)
    return m
''',

    "src/utils.py": '''\
def normalize_names(df, alias_dict):
    df['sender'] = df['sender'].apply(lambda x: alias_dict.get(x, x))
    df['recipient'] = df['recipient'].apply(lambda x: alias_dict.get(x, x))
    return df
''',

    "main.py": '''\
from src.data_loader import load_data
from src.timeline_analysis import plot_letters_per_decade
from src.network_builder import build_network
import networkx as nx

def main():
    df = load_data("data/letters.csv")
    plot_letters_per_decade(df)
    G = build_network(df)
    print("Number of nodes:", G.number_of_nodes())
    print("Number of edges:", G.number_of_edges())

if __name__ == "__main__":
    main()
'''
}

# Create directories
for d in directories:
    os.makedirs(d, exist_ok=True)

# Write files
for path, content in files.items():
    full_path = os.path.join(base_path, path)
    with open(full_path, "w") as f:
        f.write(content)

# Generate a sample dataset
sample_data = [
    ["sender", "recipient", "year", "place_sent", "place_received", "lat_sent", "lon_sent", "lat_received", "lon_received"],
    ["Gottfried Wilhelm Leibniz", "Antoine Arnauld", 1672, "Paris", "Paris", 48.8566, 2.3522, 48.8566, 2.3522],
    ["Isaac Newton", "Edmond Halley", 1687, "Cambridge", "London", 52.2053, 0.1218, 51.5074, -0.1278],
    ["Diderot", "Catherine the Great", 1773, "Paris", "St. Petersburg", 48.8566, 2.3522, 59.9311, 30.3609],
    ["Spinoza", "Henry Oldenburg", 1665, "Amsterdam", "London", 52.3676, 4.9041, 51.5074, -0.1278],
]

# Save CSV
with open(os.path.join(base_path, "data", "letters.csv"), "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(sample_data)

# Create example notebook
notebook_content = {
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": ["# Republic of Letters – Analysis Demo\nThis notebook demonstrates basic analysis on early modern correspondence metadata."]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\nfrom src.timeline_analysis import plot_letters_per_decade\nfrom src.network_builder import build_network\n\n# Load dataset\ndf = pd.read_csv('../data/letters.csv')\ndf.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Plot timeline\nplot_letters_per_decade(df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Build and inspect network\nG = build_network(df)\nprint(\"Nodes:\", G.nodes())\nprint(\"Edges:\", G.edges(data=True))"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "name": "python",
   "version": "3.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}

with open(os.path.join(base_path, "notebooks", "analysis_demo.ipynb"), "w", encoding="utf-8") as f:
    json.dump(notebook_content, f, indent=2)
