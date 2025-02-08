from qiskit import Aer, transpile, assemble, QuantumCircuit

def quantum_prediction():
    backend = Aer.get_backend('qasm_simulator')
    qc = QuantumCircuit(2, 2)
    qc.h(0)
    qc.cx(0, 1)
    qc.measure([0, 1], [0, 1])
    
    transpiled = transpile(qc, backend)
    qobj = assemble(transpiled)
    result = backend.run(qobj).result()
    counts = result.get_counts()
    
    return {"prediccion": "Alta congestión" if "11" in counts else "Tráfico fluido"}
