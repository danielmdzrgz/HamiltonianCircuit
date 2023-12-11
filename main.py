"""Main module for the VC to HC transformation."""

from rich.traceback import install
from rich.console import Console

# temporal imports until visualization logic is moved to a separate module
import networkx as nx
import matplotlib.pyplot as plt
from typing import List

# from hamiltoniancircuit.gadget import Gadget

# from hamiltoniancircuit.selector import Selector
from hamiltoniancircuit.input_reader import read_graph
from hamiltoniancircuit.gadget_tools import tools as g_tools

install()
console = Console()

def visualize_graph(vertexes: List[str], edges: List[str]) -> None:
    """Shows a graphical representation of the VC problem instance."""
    console.print("Vertex Cover original instance", style="bold red")

    graph = nx.Graph()
    edge_representation: List[List[str]] = [edge.split("-") for edge in edges]
    graph.add_nodes_from(vertexes)
    graph.add_edges_from(edge_representation)

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


def test() -> None:
    """a"""
    vertexes, edges = read_graph()
    gadgets = g_tools.create_gadgets(vertexes, edges)

    console.print("Nodes:", style="bold blue")
    for vertex, vertex_id in vertexes.items():
        console.print(f"{vertex}: {vertex_id}")

    console.print("Gadgets:", style="bold blue")
    for gadget in gadgets:
        console.print(gadget)

    # node_1 = uuid4()
    # node_2 = uuid4()
    # node_3 = uuid4()
    # node_4 = uuid4()

    # gadget1 = Gadget(node_1, node_3)
    # gadget2 = Gadget(node_3, node_4)
    # gadget3 = Gadget(node_1, node_4)
    # gadget4 = Gadget(node_1, node_2)
    # gadget5 = Gadget(node_2, node_4)

    # gadget.join("Left", gadget2, "Left")
    # gadget2.join("Left", gadget3, "Left")
    # gadget.join("Right", gadget3, "Right")

    # gadgets = [gadget1, gadget2, gadget3, gadget4, gadget5]
    console.print("Connected gadgets:", style="bold green")
    nodes = list(vertexes.values())
    connected_gadgets = g_tools.connect_gadget_groups(gadgets, nodes)

    for gadget in connected_gadgets:
        console.print(gadget)

    visualize_graph(list(vertexes.keys()), edges)
    # selector = Selector()
    # selector.connect_gadget(gadget)
    # selector.connect_gadget(gadget2)
    # console.print(selector)
    # # selector.connect_gadget(gadget)

    # selector2 = Selector()
    # selector2.connect_gadget(gadget)
    # # selector2.connect_gadget(selector)
    # console.print(selector2)
    # gadget.join("Left", gadget2)
    # gadget3.join("Left", gadget)
    # # console.print(gadget)
    # # console.print(gadget2)

    # selector_list = tools.make_connections(2, [gadget, gadget2, gadget3])
    # for selector in selector_list:
    #     console.print(selector)


# Gadget ID: 1, R : [6: G-3], L : [6: G-2]
# Gadget ID: 2, R : [], L : [1: G-1, 6: G-3]
