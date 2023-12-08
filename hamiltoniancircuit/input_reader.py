from rich.console import Console

import yaml
import networkx as nx
import matplotlib.pyplot as plt

console = Console()

def run():
    console.print("Hamiltonian Circuit", style="bold red")

    with open('graph.yaml') as grafo_yaml:
        grafo_datos = yaml.safe_load(grafo_yaml)

    graph = nx.Graph()

    graph.add_nodes_from(grafo_datos['vertexes'])
    graph.add_edges_from(grafo_datos['edges'])

    plt.figure(figsize=(8, 6))
    nx.draw(graph, with_labels=True, node_color='skyblue', node_size=1500, edge_color='black', linewidths=1, font_size=15)
    plt.title("Graph", fontsize=20)
    plt.show()
