"""Main module for the VC to HC transformation."""

import uuid
from rich.traceback import install
from rich.console import Console
from hamiltoniancircuit.gadget import Gadget

install()
console = Console()

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
