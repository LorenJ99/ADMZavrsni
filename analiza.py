import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('podaci.csv')

G = nx.DiGraph()

for _, edge in data.iterrows():
    source = edge['source']
    target = edge['target']
    weight = 1
    if G.has_edge(source, target):
        weight += G[source][target]['weight']
    G.add_edge(source, target, weight=weight)

# Lokalna analiza
local_centrality = nx.degree_centrality(G)

# Središnja analiza
central_edge = nx.edge_betweenness_centrality(G)

# Globalna analiza
global_centrality = nx.eigenvector_centrality(G)

# Vizualizacija grafova
plt.figure(figsize=(18, 6))

# Lokalna analiza
plt.subplot(1, 3, 1)
pos = nx.circular_layout(G) 
nx.draw(G, pos, with_labels=True, node_size=[v * 1000 for v in local_centrality.values()], node_color='skyblue')
plt.title('Lokalna analiza')
labels = nx.get_edge_attributes(G, 'weight') 
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.savefig('lokalni-graf.png', bbox_inches='tight', dpi=300) 

# Središnja analiza
plt.subplot(1, 3, 2)
pos = nx.circular_layout(G)
nx.draw(G, pos, with_labels=True, width=[v * 10 for v in central_edge.values()], edge_color='skyblue')
plt.title('Središnja analiza')
labels = nx.get_edge_attributes(G, 'weight')  
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)  
plt.savefig('sredisnji-graf.png', bbox_inches='tight', dpi=300)  

# Globalna analiza
plt.subplot(1, 3, 3)
pos = nx.circular_layout(G)  
nx.draw(G, pos, with_labels=True, node_size=[v * 10000 for v in global_centrality.values()], node_color='skyblue')
plt.title('Globalna analiza')
labels = nx.get_edge_attributes(G, 'weight') 
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels) 
plt.savefig('globalni-graf.png', bbox_inches='tight', dpi=300)  

plt.tight_layout()
plt.show()
