"""
This module contains the Selector class, which is used to create auxiliary nodes
to connect the gadgets in the reduction from Vertex Cover to Hamiltonian Circuit.

Selectors are used to connect the gadgets based on the Vertex Cover instance's edges.
"""

from __future__ import annotations
from typing import Dict, List, Literal, Union
from hamiltoniancircuit.gadget import Gadget

from rich.table import Table
from rich.console import Console
from rich import box

GadgetSideType = Union[Literal["Left"], Literal["Right"]]


class Selector:
    """Selector class for Hamiltonian Circuit problem."""

    number_of_selectors: int = 0

    def __init__(self, selector: Union[Selector, None] = None) -> None:
        """Initialize a selector."""
        self.connections_: Dict[Gadget, Dict[GadgetSideType, List[int]]] = (
            {} if not selector else selector.connections_.copy()
        )

        type(self).number_of_selectors += 1
        self.id = type(self).number_of_selectors

    def connect_gadget(
        self, gadget: Gadget, side: GadgetSideType, position: int
    ) -> None:
        """Conect the selector to a gadget."""
        gadget_entry = self.connections_.get(gadget)
        if gadget_entry is None:
            self.connections_[gadget] = {side: [position]}
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

    def to_table_data(self):
        """Prepare data for tabular representation."""
        table_data = []
        for gadget, sides in self.connections_.items():
            for side, positions in sides.items():
                table_data.append([f"G-{gadget.id}", side, ", ".join(map(str, positions))])
        return table_data
    
    def print_table(self) -> None:
        table = Table(title=f"Selector id: {self.id}", box=box.SIMPLE, show_header=True, header_style="bold")

        table.add_column("Gadget ID")
        table.add_column("Connections", justify="center")

        max_len_left = max(len(', '.join(map(str, sides.get("Left", [])))) for _, sides in self.connections_.items())
        max_len_right = max(len(', '.join(map(str, sides.get("Right", [])))) for _, sides in self.connections_.items())

        for gadget, sides in self.connections_.items():
            left_positions = ', '.join(map(str, sides.get("Left", []))) if sides.get("Left") else " "
            right_positions = ', '.join(map(str, sides.get("Right", []))) if sides.get("Right") else " "

            left_positions_formatted = f"{left_positions: <{max_len_left}}"
            right_positions_formatted = f"{right_positions: >{max_len_right}}"

            left_connection = "[green]❚[/green]" if "Left" in sides and sides["Left"] else "[white]❚[/white]"
            right_connection = "[green]❚[/green]" if "Right" in sides and sides["Right"] else "[white]❚[/white]"

            connection_str = f"{left_positions_formatted} {left_connection} {right_connection} {right_positions_formatted}"
            table.add_row(f"G-{gadget.id}", connection_str)

        console = Console()
        console.print(table)
