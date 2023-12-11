"""
This module contains some functions to work with the gadgets of the reduction.
The functions are:
  - create_gadgets: given the original graph, create the gadgets.
  - connect_gadget_groups: given the gadgets and the nodes, connect the gadgets
    that belong to the same node.
"""

from typing import List, Literal, Union
from hamiltoniancircuit.gadget import Gadget


def create_gadgets(vertexes: List[str], edges: List[str]) -> List[Gadget]:
    """Create the gadgets for the transformation based on the original graph."""
    gadgets: List[Gadget] = []

    for edge in edges:
        edge = edge.split("-")
        node_1 = edge[0]
        node_2 = edge[1]

        if node_1 not in vertexes or node_2 not in vertexes:
            raise ValueError("Invalid edge.")

        gadgets.append(Gadget(node_2, node_1))

    return gadgets


def connect_gadget_groups(gadgets: List[Gadget], nodes: List[str]) -> List[Gadget]:
    """Connects the gadgets that belong to the same node."""
    for node in nodes:
        current_gadget: Union[Gadget, None] = None
        previous_gadget: Union[Gadget, None] = None
        previous_side: Union[Literal["Right"], Literal["Left"]] = "Left"

        for gadget in gadgets:
            if not gadget.contains_node(node):
                continue

            current_side = "Right" if gadget.right_.node_id == node else "Left"
            current_gadget = gadget

            if not previous_gadget:
                previous_gadget = current_gadget
                previous_side = current_side
                continue

            previous_gadget.join(previous_side, current_gadget, current_side)
            previous_gadget = current_gadget
            previous_side = current_side

    return gadgets
