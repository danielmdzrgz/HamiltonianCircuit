"""
"""

from typing import Dict, List, Tuple
from uuid import UUID, uuid4
from rich.console import Console
import yaml
import networkx as nx
import matplotlib.pyplot as plt

console = Console()


def read_graph() -> Tuple[Dict[str, UUID], List[str]]:
    """Read the graph from a yaml file."""
    with open("graph.yaml", encoding="UTF-8") as yaml_graph:
        data = yaml.safe_load(yaml_graph)

    edge_data = [edge[0] + "-" + edge[1] for edge in data["edges"]]

    vertexes_uuid: Dict[str, UUID] = {}
    for node in data["vertexes"]:
        vertexes_uuid[node] = uuid4()

    return vertexes_uuid, edge_data


def run():
    console.print("Hamiltonian Circuit", style="bold red")

    with open("graph.yaml", encoding="UTF-8") as grafo_yaml:
        grafo_datos = yaml.safe_load(grafo_yaml)

    console.print("Grafo de entrada", style="bold blue")
    console.print(grafo_datos)

    graph = nx.Graph()

    graph.add_nodes_from(grafo_datos["vertexes"])
    graph.add_edges_from(grafo_datos["edges"])

    plt.figure(figsize=(8, 6))
    nx.draw(
        graph,
        with_labels=True,
        node_color="skyblue",
        node_size=1500,
        edge_color="black",
        linewidths=1,
        font_size=15,
    )
    plt.title("Graph", fontsize=20)
    plt.show()
