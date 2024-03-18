import numpy as np
from qiskit import QuantumCircuit, transpile
from qiskit.primitives.sampler import Sampler

# 1. Create a quantum circuit to prepare the quantum state |000> + i |111>
qc_example = QuantumCircuit(3)
qc_example.h(0) # Apply a Hadamard gate to create superposition
qc_example.p(np.pi/2,0) # Add a quantum phase of π/2 to the first qubit
qc_example.cx(0,1) # Apply a CX (Control-X) gate with the first qubit as control and the second qubit as target
qc_example.cx(0,2) # Apply a CX gate with the first qubit as control and the third qubit as target

# 2. Add the classical output in the form of measurement of all qubits
qc_measured = qc_example.measure_all(inplace=False)

# 3. Execute using the Sampler primitive
sampler = Sampler()
job = sampler.run(qc_measured, shots=1000) # Execute the measured circuit multiple times to obtain probabilistic statistics
result = job.result()
print(f" > Quasi probability distribution: {result.quasi_dists}") # Print the quasi probability distribution

# 4. Qiskit transpiler
qc_transpiled = transpile(qc_example, basis_gates=['cz', 'sx', 'rz'], coupling_map=[[0, 1], [1, 2]], optimization_level=3)
