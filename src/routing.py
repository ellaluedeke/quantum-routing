import time

from qiskit import QuantumCircuit, transpile
from qiskit.transpiler import CouplingMap


def graph_to_coupling_map(graph):
    """Convert a NetworkX graph to a Qiskit coupling map."""
    edges = [
        (u, v)
        for u, v in graph.edges()
    ]

    return CouplingMap(couplinglist=edges)


def route_circuit(
    circuit: QuantumCircuit,
    graph,
    seed: int = 42
):
    """Compile a circuit using Qiskit's SABRE routing."""

    coupling_map = graph_to_coupling_map(graph)

    start = time.perf_counter()

    compiled = transpile(
        circuit,
        basis_gates=["rz", "sx", "x", "cx"],
        coupling_map=coupling_map,
        optimization_level=1,
        routing_method="sabre",
        seed_transpiler=seed,
    )

    elapsed = time.perf_counter() - start

    return {
        "circuit": compiled,
        "depth": compiled.depth(),
        "cx_count": compiled.count_ops().get("cx", 0),
        "swap_count": compiled.count_ops().get("swap", 0),
        "compile_time": elapsed,
    }