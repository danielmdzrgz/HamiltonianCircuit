"""
This module contains some functions to work with the gadgets of the reduction.
The functions are:
  - create_gadgets: given the original graph, create the gadgets.
"""

from typing import Dict, List
import uuid
from hamiltoniancircuit.gadget import Gadget


def create_gadgets(
    graph_data: Dict[str, List[str]]
) -> List[Gadget]:
    """Create the gadgets for the transformation based on the original graph."""
    gadgets: List[Gadget] = []
    vertex_uuids: Dict[str, uuid.UUID] = {}
    for node in graph_data["vertexes"]:
        vertex_uuids[node] = uuid.uuid4()

    for edge in graph_data["edges"]:
        edge = edge.split("-")
        node_1 = vertex_uuids[edge[0]]
        node_2 = vertex_uuids[edge[1]]
        gadgets.append(Gadget(node_1, node_2))

    return gadgets
