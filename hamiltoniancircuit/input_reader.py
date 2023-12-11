"""
"""

from typing import Dict, List, Tuple
from uuid import UUID, uuid4
from rich.console import Console
import yaml
import networkx as nx
import matplotlib.pyplot as plt


def read_graph() -> Tuple[Dict[str, UUID], List[str]]:
    """Read the graph from a yaml file."""
    with open("graph.yaml", encoding="UTF-8") as yaml_graph:
        data = yaml.safe_load(yaml_graph)

    edge_data = [edge[0] + "-" + edge[1] for edge in data["edges"]]

    vertexes_uuid: Dict[str, UUID] = {}
    for node in data["vertexes"]:
        vertexes_uuid[node] = uuid4()

    return vertexes_uuid, edge_data