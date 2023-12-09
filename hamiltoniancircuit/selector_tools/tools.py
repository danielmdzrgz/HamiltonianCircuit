"""
This module contains the make_connections which recieves the k selector number
and a list of gadgets and create a number of k selector and then connected them
to the gadgets of the list to create the circuit of the reduction from Vertex 
Cover to Hamiltonian Circuit.
"""
from hamiltoniancircuit.gadget import Gadget
from selector import Selector
from typing import List

def make_connections(k_number_selectors: int, gadgets: List[Gadget]) -> List[Selector]:
    """Create the selectors and then make the connectios with the gadgets"""
    selector_list: List[Selector] = []
    for i in range(k_number_selectors):
        aux_selector: Selector = Selector()
        selector_list.append(aux_selector)

    for i in range(len(gadgets)):
        if gadgets[i].left_[1] == [{}] or gadgets[i].right_[1] == [{}]:
            for j in range(len(selector_list)):
                selector_list[j].connect_gadget(gadgets[i])

    return selector_list