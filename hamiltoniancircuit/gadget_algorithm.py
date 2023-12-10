from __future__ import annotations
from typing import Dict, List, Literal, Union, Tuple
from typing import Dict, List, Literal, Union, Tuple
from uuid import UUID
from hamiltoniancircuit.gadget import Gadget
from rich.console import Console

def gadget_algorithm(gadgets: List[Gadget], nodes: List[UUID]) -> List[Gadget]:
  for node in nodes:
    current_gadget: int = -1
    previous_gadget: int = -1
    previous_side: Union[Literal["Right"], Literal["Left"]] = "Left"
    for i in range(len(gadgets)):
      if gadgets[i].contains_node(node):
        current_side: Union[Literal["Right"], Literal["Left"]]
        if gadgets[i].left_.node_id == node:
          current_side = "Left"
        else:
          current_side = "Right"
        current_gadget = i
        if previous_gadget != -1:
          gadgets[previous_gadget].join(previous_side, gadgets[current_gadget], current_side, 6)
        previous_gadget = current_gadget
        previous_side = current_side
    
  return gadgets