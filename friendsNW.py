import networkx as nx
import matplotlib.pyplot as plt
import streamlit

G = nx.Graph()
G.add_edges_from([('Alice', 'Bob'), ('Alice', 'Charlie'), ('Bob', 'David'), ('Charlie', 'Eve')])

plt.figure(figsize=(6, 4))
nx.draw(G, with_labels=True, node_color='lightblue', edge_color='gray', node_size=2000, font_size=14)
plt.show()
