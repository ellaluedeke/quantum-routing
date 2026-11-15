import sys
sys.path.append("src")

from architectures import (
    heavy_hex_graph,
    square_grid_graph
)

from routing import route_circuit

from qiskit import QuantumCircuit


# Simple test circuit
qc = QuantumCircuit(5)

qc.h(0)
qc.cx(0, 1)
qc.cx(1, 2)
qc.cx(2, 3)
qc.cx(3, 4)
qc.cx(0, 4)

qc.measure_all()


for name, graph in [
    ("Heavy-hex-inspired", heavy_hex_graph()),
    ("Square grid", square_grid_graph())
]:

    result = route_circuit(qc, graph)

    print(f"\n{name}")
    print("-----------------------")
    print("Depth:", result["depth"])
    print("CX gates:", result["cx_count"])
    print("SWAP gates:", result["swap_count"])
    print("Compile time:", result["compile_time"])