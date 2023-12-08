"""Main module for the VC to HC transformation."""

from rich.traceback import install
from rich.console import Console
from hamiltoniancircuit.gadget import Gadget

install()
console = Console()

def test() -> None:
    """a"""
    gadget = Gadget()
    gadget2 = Gadget()
    gadget3 = Gadget()

    gadget.join("Right", 1, gadget2)
    gadget.join("Right", 2, gadget3)

    console.print(gadget)
    console.print(gadget2)
