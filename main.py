"""Main module for the VC to HC transformation."""

import uuid
from typing import List
from rich.traceback import install
from rich.console import Console
from hamiltoniancircuit.gadget import Gadget
from hamiltoniancircuit.selector import Selector

install()
console = Console()


def create_selectors(k_number: int) -> List[Selector]:
    """Create the selectors for the transformation."""
    selectors = []
    for _ in range(k_number):
        selectors.append(Selector())

    return selectors


def test() -> None:
    """a"""

    node_1 = uuid.uuid4()
    node_2 = uuid.uuid4()
    node_3 = uuid.uuid4()
    node_4 = uuid.uuid4()

    gadget = Gadget(node_1, node_2)
    gadget2 = Gadget(node_2, node_3)
    gadget3 = Gadget(node_3, node_4)

    gadget.join("Right", gadget2)
    gadget.join("Right", gadget3)

    console.print(gadget)
    console.print(gadget2)

    selector = Selector()
    selector.connect_gadget(gadget)
    selector.connect_gadget(gadget2)
    console.print(selector)
    # selector.connect_gadget(gadget)

    selector2 = Selector()
    selector2.connect_gadget(gadget)
    # selector2.connect_gadget(selector)
    console.print(selector2)

    k_number: int = 2
    selectors = create_selectors(k_number)
    for selector in selectors:
        console.print(selector)
