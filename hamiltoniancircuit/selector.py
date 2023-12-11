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
        self.conections_: Dict[Gadget, List[GadgetSideType]] = (
            {} if not selector else selector.conections_.copy()
        )

        type(self).number_of_selectors += 1
        self.id = type(self).number_of_selectors

    def connect_gadget(self, gadget: Gadget, side: GadgetSideType) -> None:
        """Conect the selector to a gadget."""
        if side in self.conections_.get(gadget, []):
            raise ValueError("Cannot connect selector to the same gadget twice.")

        gadget_entry = self.conections_.get(gadget)
        if gadget_entry:
            gadget_entry.append(side)
            return

        self.conections_[gadget] = [side]

    def __str__(self) -> str:
        """Return a string representation of the selector."""
        connections = "; ".join(
            [
                f"G-{gadget.id}: {', '.join(sides)}"
                for gadget, sides in self.conections_.items()
            ]
        )
        return f"Selector ID: {self.id}, Connections: [{connections}]"
