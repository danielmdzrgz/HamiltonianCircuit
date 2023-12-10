from __future__ import annotations
from typing import Dict, List, Literal, Union, Tuple
from typing import Dict, List, Literal, Union, Tuple
from uuid import UUID
from hamiltoniancircuit.gadget import Gadget
from rich.console import Console

def gadget_algorithm(gadgets: List[Gadget], nodes: List[UUID]):
  console = Console()
  current_gadget: Gadget
  previus_gadget: Gadget
  for node in nodes:
    console.print(node)
    for gadget in gadgets:
      if gadget.contains(node):
        side: str = ""
        if gadget.left_[0] == node:
          side = "Left"
        else:
          side = "Right"
        console.print(gadget)
        console.print(side)

    console.print("\n")
        
        

