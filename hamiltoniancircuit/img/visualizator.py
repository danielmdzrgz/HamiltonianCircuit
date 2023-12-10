import matplotlib
matplotlib.use('Agg')

import networkx as nx
import matplotlib.pyplot as plt

def test():
    G = nx.Graph()

    # Agregar nodos
    G.add_nodes_from([1, 2, 3, 4])

    # Agregar aristas (conexiones entre nodos)
    G.add_edges_from([(1, 2), (1, 3), (1, 4), (3, 4)])

    # Definir posiciones de los nodos (imitando un cuadrado)
    pos = {1: (0, 1), 2: (0, 0), 3: (1, 1), 4: (1, 0)}

    # Dibujar el grafo
    nx.draw_networkx(G, pos, with_labels=True, font_weight='bold')

    # Guardar el gráfico en un archivo en lugar de mostrarlo
    plt.savefig("grafo.png")

