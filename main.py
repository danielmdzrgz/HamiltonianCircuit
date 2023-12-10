"""Main module for the VC to HC transformation."""

from platform import node
import uuid
from uuid import UUID
from typing import List
from rich.traceback import install
from rich.console import Console
from hamiltoniancircuit.gadget import Gadget
from hamiltoniancircuit.gadget_algorithm import gadget_algorithm

install()
console = Console()

def test() -> None:
    """a"""

    node_1 = uuid.uuid4()
    node_2 = uuid.uuid4()
    node_3 = uuid.uuid4()
    node_4 = uuid.uuid4()

    console.print(node_1)
    console.print(node_2)
    console.print(node_3)
    console.print(node_4)
    console.print("\n")

    list_node: List[UUID] = [node_1, node_2, node_3, node_4]

    gadget1 = Gadget(node_3, node_1)
    gadget2 = Gadget(node_4, node_1)
    gadget3 = Gadget(node_2, node_1)
    gadget4 = Gadget(node_4, node_2)

    """gadget1.join("Left", gadget2, 1)
    gadget2.join("Left", gadget1, 6)
    gadget2.join("Left", gadget3, 1)
    gadget3.join("Left", gadget2, 6)"""
    gadget_algorithm([gadget1, gadget2, gadget3, gadget4], list_node)

    console.print(gadget1)
    console.print(gadget2)
    console.print(gadget3)
    console.print(gadget4)
