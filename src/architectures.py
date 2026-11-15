import networkx as nx


def heavy_hex_graph(rows: int = 3, cols: int = 3):
    """
    Construct a simplified heavy-hex-inspired
    connectivity graph.

    This is a synthetic graph, not an exact IBM
    processor topology.
    """
    graph = nx.hexagonal_lattice_graph(rows, cols)

    # Remove alternating edges to produce
    # a sparser connectivity structure.
    edges = list(graph.edges())

    for i, edge in enumerate(edges):
        if i % 3 == 0:
            graph.remove_edge(*edge)

    return nx.convert_node_labels_to_integers(graph)


def square_grid_graph(rows: int = 4, cols: int = 4):
    """Construct a square-grid connectivity graph."""
    graph = nx.grid_2d_graph(rows, cols)
    return nx.convert_node_labels_to_integers(graph)


if __name__ == "__main__":
    heavy_hex = heavy_hex_graph()
    grid = square_grid_graph()

    for name, graph in [
        ("Heavy-hex-inspired", heavy_hex),
        ("Square grid", grid)
    ]:
        print(f"\n{name}")
        print(f"Qubits: {graph.number_of_nodes()}")
        print(f"Connections: {graph.number_of_edges()}")
        print(f"Average degree: {sum(dict(graph.degree()).values()) / graph.number_of_nodes():.2f}")