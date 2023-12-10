from typing import List, Literal, Union
from uuid import UUID
from rich.console import Console
from hamiltoniancircuit.gadget import Gadget

console = Console()

def gadget_algorithm(gadgets: List[Gadget], nodes: List[UUID]) -> List[Gadget]:
    """This function connects the gadgets that belong to the same node."""
    for node in nodes:
        console.print(f"Node: {node}")
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

            console.print(previous_gadget)
            console.print(previous_side)
            console.print(current_gadget)
            console.print(current_side)
            previous_gadget.join(previous_side, current_gadget, current_side)
            previous_gadget = current_gadget
            previous_side = current_side

    return gadgets
