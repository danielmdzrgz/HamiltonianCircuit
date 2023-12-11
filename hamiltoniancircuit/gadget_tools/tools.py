"""
This module contains some functions to work with the gadgets of the reduction.
The functions are:
  - create_gadgets: given the original graph, create the gadgets.
"""

from typing import Dict, List
from uuid import UUID
from hamiltoniancircuit.gadget import Gadget


def create_gadgets(vertexes: Dict[str, UUID], edges: List[str]) -> List[Gadget]:
    """Create the gadgets for the transformation based on the original graph."""
    gadgets: List[Gadget] = []

    for edge in edges:
        edge = edge.split("-")
        node_1 = vertexes[edge[0]]
        node_2 = vertexes[edge[1]]
        gadgets.append(Gadget(node_1, node_2))

    return gadgets
