"""
This module contains the Gadget class, which is used to create the gadgets
used in the reduction from Vertex Cover to Hamiltonian Circuit.

Gadgets are used to connect the new graph based on the Vertex Cover instance'e edges.
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import Dict, List, Literal, Union
from uuid import UUID


class Gadget:
    """Gadget class for Hamiltonian Circuit problem."""

    number_of_gadgets: int = 0
    id: int = 0

    @dataclass
    class GadgetSide:
        """Gadget side class."""

        node_id: UUID
        gadget_nodes: List[Dict[int, Gadget]]

    def __init__(self, right_id: UUID, left_id: UUID) -> None:
        """Initialize a gadget."""
        self.right_: Gadget.GadgetSide = Gadget.GadgetSide(right_id, [])
        self.left_: Gadget.GadgetSide = Gadget.GadgetSide(left_id, [])

        type(self).number_of_gadgets += 1
        self.id = type(self).number_of_gadgets

    def contains_node(self, node: UUID) -> bool:
        """Return True if the gadget contains the node."""
        return node in (self.right_.node_id, self.left_.node_id)

    def contains_gadget(self, gadget: Gadget) -> bool:
        """Return True if the gadget contains the gadget."""
        return any(
            gadget in dct.values()
            for dct in self.right_.gadget_nodes + self.left_.gadget_nodes
        )

    def join_right(self, gadget: Gadget, position) -> None:
        """Join a gadget to the right."""
        if any(position in dct for dct in self.right_.gadget_nodes):
            raise ValueError("Position already taken in right side.")

        self.right_.gadget_nodes.append({position: gadget})

    def join_left(self, gadget: Gadget, position) -> None:
        """Join a gadget to the left."""
        if any(position in dct for dct in self.left_.gadget_nodes):
            raise ValueError("Position already taken in left side.")

        self.left_.gadget_nodes.append({position: gadget})

    def join(
        self,
        side: Union[Literal["Right"], Literal["Left"]],
        o_gadget: Gadget,
        o_gadget_side: Union[Literal["Right"], Literal["Left"]],
        position: int = 6,
    ) -> None:
        """Join a gadget to the left or right."""
        if o_gadget.id == self.id:
            raise ValueError("Cannot join gadget to itself.")

        if self.contains_gadget(o_gadget) or o_gadget.contains_gadget(self):
            raise ValueError("Detected a cycle.")

        if side == "Right":
            self.join_right(o_gadget, position)
        else:
            self.join_left(o_gadget, position)

        if o_gadget_side == "Right":
            o_gadget.join_right(self, 1)
        else:
            o_gadget.join_left(self, 1)

    def __str__(self) -> str:
        """Return a string representation of the gadget."""
        right_connections = ", ".join(
            [
                f"{key}: G-{gadget.id}"
                for dct in self.right_.gadget_nodes
                for key, gadget in dct.items()
            ]
        )

        left_connections = ", ".join(
            [
                f"{key}: G-{gadget.id}"
                for dct in self.left_.gadget_nodes
                for key, gadget in dct.items()
            ]
        )

        right_str = (
            f"R[{self.right_.node_id}] :[{right_connections}]"
            if right_connections
            else f"R[{self.right_.node_id}] :[]"
        )

        left_str = (
            f"L[{self.left_.node_id}] :[{left_connections}]"
            if left_connections
            else f"L[{self.left_.node_id}] :[]"
        )

        return f"Gadget ID: {self.id}, {right_str}, {left_str}"

    @staticmethod
    def get_number_of_gadgets() -> int:
        """Return the number of gadgets."""
        return Gadget.number_of_gadgets
