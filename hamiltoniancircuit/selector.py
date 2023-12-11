"""
This module contains the Selector class, which is used to create auxiliary nodes
to connect the gadgets in the reduction from Vertex Cover to Hamiltonian Circuit.

Selectors are used to connect the gadgets based on the Vertex Cover instance's edges.
"""

from __future__ import annotations
from typing import Dict, List, Literal, Union
from hamiltoniancircuit.gadget import Gadget

GadgetSideType = Union[Literal["Left"], Literal["Right"]]


class Selector:
    """Selector class for Hamiltonian Circuit problem."""

    number_of_selectors: int = 0

    def __init__(self, selector: Union[Selector, None] = None) -> None:
        """Initialize a selector."""
        self.conections_: Dict[Gadget, Dict[GadgetSideType, List[int]]] = (
            {} if not selector else selector.conections_.copy()
        )

        type(self).number_of_selectors += 1
        self.id = type(self).number_of_selectors

    def connect_gadget(
        self, gadget: Gadget, side: GadgetSideType, position: int
    ) -> None:
        """Conect the selector to a gadget."""
        gadget_entry = self.conections_.get(gadget)
        if gadget_entry is None:
            self.conections_[gadget] = {side: [position]}
            return

        if position in gadget_entry.get(side, []):
            raise ValueError(
                "Cannot connect selector to the same position of a gadget twice."
            )

        side_entry = gadget_entry.get(side)
        if side_entry:
            side_entry.append(position)
            return

        gadget_entry[side] = [position]

    def __str__(self) -> str:
        """Return a string representation of the selector."""
        sides_str: List[str] = []
        for sides in self.conections_.values():
            side_str = ", ".join(
                f"{side}: [{', '.join([str(pos) for pos in positions])}]"
                for side, positions in sides.items()
            )
            sides_str.append(side_str)

        connections = "; ".join(
            [
                f"G-{gadget.id}: {side_str}"
                for gadget, side_str in zip(self.conections_.keys(), sides_str)
            ]
        )
        return f"Selector ID: {self.id}, Connections: [{connections}]"
