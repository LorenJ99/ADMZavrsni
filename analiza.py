import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt

# Učitavanje podataka iz CSV datoteke
data = pd.read_csv('podaci.csv')

# Stvaranje usmjerenog grafa
G = nx.DiGraph()

# Dodavanje bridova s težinama u graf
for _, edge in data.iterrows():
    source = edge['source']
    target = edge['target']
    weight = 1  # Početna težina je 1
    if G.has_edge(source, target):
        # Ako već postoji veza, dodajte težinu
        weight += G[source][target]['weight']
    G.add_edge(source, target, weight=weight)

# Lokalna analiza - centralnost čvorova
local_centrality = nx.degree_centrality(G)

# Središnja analiza - centralnost bridova
central_edge = nx.edge_betweenness_centrality(G)

# Globalna analiza - centralnost po važnosti
global_centrality = nx.eigenvector_centrality(G)

# Vizualizacija grafova
plt.figure(figsize=(18, 6))

# Lokalna analiza - graf s označenim čvorovima prema lokalnoj centralnosti
plt.subplot(1, 3, 1)
pos = nx.circular_layout(G)  # Pozicioniranje čvorova u krug
nx.draw(G, pos, with_labels=True, node_size=[v * 1000 for v in local_centrality.values()], node_color='skyblue')
plt.title('Lokalna analiza')
labels = nx.get_edge_attributes(G, 'weight')  # Dohvaćanje težina bridova
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)  # Prikaz težina
plt.savefig('lokalni-graf.png', bbox_inches='tight', dpi=300)  # Spremi graf u lokalnu datoteku

# Središnja analiza - graf s označenim bridovima prema središnjoj centralnosti
plt.subplot(1, 3, 2)
pos = nx.circular_layout(G)  # Pozicioniranje čvorova u krug
nx.draw(G, pos, with_labels=True, width=[v * 10 for v in central_edge.values()], edge_color='skyblue')
plt.title('Središnja analiza')
labels = nx.get_edge_attributes(G, 'weight')  # Dohvaćanje težina bridova
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)  # Prikaz težina
plt.savefig('sredisnji-graf.png', bbox_inches='tight', dpi=300)  # Spremi graf u lokalnu datoteku

# Globalna analiza - graf s označenim čvorovima prema globalnoj centralnosti
plt.subplot(1, 3, 3)
pos = nx.circular_layout(G)  # Pozicioniranje čvorova u krug
nx.draw(G, pos, with_labels=True, node_size=[v * 10000 for v in global_centrality.values()], node_color='skyblue')
plt.title('Globalna analiza')
labels = nx.get_edge_attributes(G, 'weight')  # Dohvaćanje težina bridova
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)  # Prikaz težina
plt.savefig('globalni-graf.png', bbox_inches='tight', dpi=300)  # Spremi graf u lokalnu datoteku

plt.tight_layout()
plt.show()
