"""
This module contains functionalities to extract the input data from a yaml file.
The yaml file must have the following structure:

vertexes:
  - A
  - B
  - C
  - D

edges:
  - [A, B]
  - [A, C]
  - [A, D]
  - [B, D]

An example yaml file is provided in the root of the project with the name graph.yaml.
"""

from typing import List, Tuple
import yaml


def read_graph() -> Tuple[List[str], List[str]]:
    """Read the graph from a yaml file."""
    with open("graph.yaml", encoding="UTF-8") as yaml_graph:
        data = yaml.safe_load(yaml_graph)

    edge_data: List[str] = [edge[0] + "-" + edge[1] for edge in data["edges"]]

    return data["vertexes"], edge_data
