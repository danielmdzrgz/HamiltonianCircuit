"""
This module contains the make_connections which recieves the k selector number
and a list of gadgets and create a number of k selector and then connected them
to the gadgets of the list to create the circuit of the reduction from Vertex 
Cover to Hamiltonian Circuit.
"""

from typing import List
from hamiltoniancircuit.gadget import Gadget
from hamiltoniancircuit.selector import Selector


def create_selectors(k_number: int, selector: Selector) -> List[Selector]:
    """Create the selectors for the transformation."""
    selector_list: List[Selector] = [selector]
    selector_list.extend([Selector(selector) for _ in range(k_number - 1)])
    return selector_list


def make_connections(k_number_selectors: int, gadgets: List[Gadget]) -> List[Selector]:
    """Create the selectors and then make the connectios with the gadgets"""
    selector: Selector = Selector()
    for gadget in gadgets:
        gadget_left = gadget.left_.gadget_nodes
        gadget_right = gadget.right_.gadget_nodes

        #TODO indicar de que posicion se conecta el gadget y poder conectarse el 1 y 6 de
        #TODO un gadget en caso de ser necesario (probablemente haya que cambiar la estructura 
        #TODO de selector para poder hacer este cambio, metodo connect_gadget)
        if not gadget_left.get(1):
            selector.connect_gadget(gadget, "Left", 1)

        if not gadget_left.get(6):
            selector.connect_gadget(gadget, "Left", 6)

        if not gadget_right.get(1):
            selector.connect_gadget(gadget, "Right", 1)
        
        if not gadget_right.get(6):
            selector.connect_gadget(gadget, "Right", 6)

    return create_selectors(k_number_selectors, selector)
