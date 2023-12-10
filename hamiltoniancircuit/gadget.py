"""
This module contains the Gadget class, which is used to create the gadgets
used in the reduction from Vertex Cover to Hamiltonian Circuit.

Gadgets are used to connect the new graph based on the Vertex Cover instance'e edges.
"""

from __future__ import annotations
from typing import Dict, List, Literal, Union, Tuple
from uuid import UUID


class Gadget:
    """Gadget class for Hamiltonian Circuit problem."""

    number_of_gadgets: int = 0
    id: int = 0

    def __init__(self, right_id: UUID, left_id: UUID) -> None:
        """Initialize a gadget."""
        self.right_: Tuple[UUID, List[Dict[int, Gadget]]] = (right_id, [{}])
        self.left_: Tuple[UUID, List[Dict[int, Gadget]]] = (left_id, [{}])

        type(self).number_of_gadgets += 1
        self.id = type(self).number_of_gadgets

    def contains(self, node: UUID) -> bool:
        """Return True if the gadget contains the node."""
        return node in (self.right_[0], self.left_[0])

    def join_right(self, gadget: Gadget, position: int = 6) -> None:
        """Join a gadget to the right."""
        if gadget:
            self.right_[1].append({position: gadget})

    def join_left(self, gadget: Gadget, position: int = 6) -> None:
        """Join a gadget to the left."""
        if gadget:
            self.left_[1].append({position: gadget})

    def join(
        self,
        side: Union[Literal["Right"], Literal["Left"]],
        gadget: Gadget,
        position: int = 6,
    ) -> None:
        """Join a gadget to the left or right."""
        if gadget.id == self.id:
            raise ValueError("Cannot join gadget to itself.")

        if side == "Right" and all(gadget not in dct.values() for dct in self.right_[1]):
            self.join_right(gadget, position)
        else:
            self.join_left(gadget, position)

    def __str__(self) -> str:
        """Return a string representation of the gadget."""
        right_connections = ", ".join(
            [
                f"{key}: G-{gadget.id}"
                for dct in self.right_[1]
                for key, gadget in dct.items()
            ]
        )

        left_connections = ", ".join(
            [
                f"{key}: G-{gadget.id}"
                for dct in self.left_[1]
                for key, gadget in dct.items()
            ]
        )

        right_str = f"R : [{right_connections}]" if right_connections else "R : []"

        left_str = f"L : [{left_connections}]" if left_connections else "L : []"

        return f"Gadget ID: {self.id}, {right_str}, {left_str}"

    @staticmethod
    def get_number_of_gadgets() -> int:
        """Return the number of gadgets."""
        return Gadget.number_of_gadgets
