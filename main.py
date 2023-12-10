"""Main module for the VC to HC transformation."""

from uuid import uuid4
from rich.traceback import install
from rich.console import Console
from hamiltoniancircuit.gadget import Gadget
from hamiltoniancircuit.selector import Selector
import hamiltoniancircuit.selector_tools.tools as tools
from hamiltoniancircuit.gadget_tools.tools import create_gadgets
import hamiltoniancircuit.input_reader as input_reader

install()
console = Console()


def test() -> None:
    """a"""
    graph_data = input_reader.read_graph()
    gadgets = create_gadgets(graph_data)
    for gadget in gadgets:
        console.print(gadget)


    node_1 = uuid4()
    node_2 = uuid4()
    node_3 = uuid4()
    node_4 = uuid4()

    gadget = Gadget(node_1, node_2)
    gadget2 = Gadget(node_2, node_3)
    gadget3 = Gadget(node_3, node_4)

    gadget.join("Right", gadget2)
    gadget2.join("Left", gadget, 1)
    gadget.join("Right", gadget3)

    console.print(gadget)
    console.print(gadget2)

    # selector = Selector()
    # selector.connect_gadget(gadget)
    # selector.connect_gadget(gadget2)
    # console.print(selector)
    # # selector.connect_gadget(gadget)

    # selector2 = Selector()
    # selector2.connect_gadget(gadget)
    # # selector2.connect_gadget(selector)
    # console.print(selector2)
    gadget.join("Left", gadget2)
    gadget3.join("Left", gadget)
    # console.print(gadget)
    # console.print(gadget2)

    selector_list = tools.make_connections(2, [gadget, gadget2, gadget3])
    for selector in selector_list:
        console.print(selector)
