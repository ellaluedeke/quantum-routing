import stim


def generate_surface_code(
    distance: int = 3,
    rounds: int = 3,
    basis: str = "Z"
) -> stim.Circuit:
    """
    Generate a rotated surface-code memory experiment.

    Args:
        distance: Code distance.
        rounds: Number of syndrome measurement rounds.
        basis: Logical memory basis ('X' or 'Z').

    Returns:
        Stim circuit containing the QEC experiment.
    """
    if basis not in ("X", "Z"):
        raise ValueError("Basis must be X or Z")

    circuit = stim.Circuit.generated(
        f"surface_code:rotated_memory_{basis.lower()}",
        distance=distance,
        rounds=rounds,
        after_clifford_depolarization=0.001,
        after_reset_flip_probability=0.001,
        before_measure_flip_probability=0.001,
    )

    return circuit


if __name__ == "__main__":
    circuit = generate_surface_code()

    print("Surface code circuit")
    print("--------------------")
    print(f"Physical qubits: {circuit.num_qubits}")
    print(f"Measurements: {circuit.num_measurements}")
    print(f"Detectors: {circuit.num_detectors}")
    print()
    print(circuit)