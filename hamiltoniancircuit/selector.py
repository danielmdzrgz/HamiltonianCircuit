"""
This module contains the Selector class, which is used to create auxiliary nodes
to connect the gadgets in the reduction from Vertex Cover to Hamiltonian Circuit.

Selectors are used to connect the gadgets based on the Vertex Cover instance's edges.
"""

from typing import List
from hamiltoniancircuit.gadget import Gadget


class Selector:
    """Selector class for Hamiltonian Circuit problem."""

    number_of_selectors: int = 0

    def __init__(self) -> None:
        """Initialize a selector."""
        self.conections_: List[Gadget] = []

        type(self).number_of_selectors += 1
        self.id = type(self).number_of_selectors

    def connect_gadget(self, gadget: Gadget) -> None:
        """Conect the selector to a gadget."""
        if gadget in self.conections_:
            raise ValueError("Cannot connect selector to the same gadget twice.")

        self.conections_.append(gadget)

    def __str__(self) -> str:
        """Return a string representation of the selector."""
        connections = ", ".join([f"G-{gadget.id}" for gadget in self.conections_])
        return f"Selector ID: {self.id}, Connections: [{connections}]"
