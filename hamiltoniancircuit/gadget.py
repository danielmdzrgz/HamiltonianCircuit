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

    def join_right(self, position: int, gadget: Gadget) -> None:
        """Join a gadget to the right."""    
        self.right_[1].append({position: gadget})

    def join_left(self, position: int, gadget: Gadget) -> None:
        """Join a gadget to the left."""
        self.left_[1].append({position: gadget})

    def join(
        self,
        side: Union[Literal["Right"], Literal["Left"]],
        position: int,
        gadget: Gadget,
    ) -> None:
        """Join a gadget to the left or right."""
        if gadget.id == self.id:
            raise ValueError("Cannot join gadget to itself.")

        if side == "Right":
            self.join_right(position, gadget)
        else:
            self.join_left(position, gadget)

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

        right_str = (
            f"R : [{right_connections}]"
            if right_connections
            else "R : []"
        )

        left_str = (
            f"L : [{left_connections}]"
            if left_connections
            else "L : []"
        )

        return f"Gadget ID: {self.id}, {right_str}, {left_str}"

    @staticmethod
    def get_number_of_gadgets() -> int:
        """Return the number of gadgets."""
        return Gadget.number_of_gadgets
