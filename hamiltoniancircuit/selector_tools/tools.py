"""
This module contains the make_connections which recieves the k selector number
and a list of gadgets and create a number of k selector and then connected them
to the gadgets of the list to create the circuit of the reduction from Vertex 
Cover to Hamiltonian Circuit.
"""

from typing import List
from hamiltoniancircuit.gadget import Gadget
from hamiltoniancircuit.selector import Selector


def create_selectors(k_number: int) -> List[Selector]:
    """Create the selectors for the transformation."""
    selectors: List[Selector] = []
    for _ in range(k_number):
        selectors.append(Selector())

    return selectors


def make_connections(k_number_selectors: int, gadgets: List[Gadget]) -> List[Selector]:
    """Create the selectors and then make the connectios with the gadgets"""
    selector_list: List[Selector] = create_selectors(k_number_selectors)

    for gadget in gadgets:
        print(gadget.left_[1] + gadget.right_[1])
        if any(connection == {} for connection in gadget.left_[1] + gadget.right_[1]):
            for selector in selector_list:
                selector.connect_gadget(gadget)

    return selector_list
