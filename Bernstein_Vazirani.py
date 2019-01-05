
# coding: utf-8


from qiskit import IBMQ, QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit import execute, Aer
from qiskit.qasm import pi
from qiskit.tools.visualization import plot_histogram, circuit_drawer
import numpy as np

APItoken = "Replace me"
url = "Replace me"
IBMQ.enable_account(APItoken, url)

IBMQ.backends()

# Suppose a(the number we want to obtain) = 111
# This is the oracle
def bv_oracle(qci,n):
    for i in range(n):
        qci.cx(q[i],q[n])
#The number of qubits    
bn = 4
#The number of classical bits
cn = 3

q = QuantumRegister(bn)
c = ClassicalRegister(cn)
qc = QuantumCircuit(q,c)

#Flip the last qubit
qc.x(q[3])

#Put hadamard transform on all the qubits
for i in range(bn):
    qc.h(q[i])
    
#Put the oracle
bv_oracle(qc,3)

#Put Put hadamard transform again
for i in range(bn):
    qc.h(q[i])
    
for j in range(cn):
    qc.measure(q[cn-j-1],c[j])

#Pick one real device as the first choice and put the simulator next. 
#I put ibmq20tokyo because this is the only device I'm allowed to use.  
backends = ['ibmq_20_tokyo', 'qasm_simulator']

#Use this for the actual machine
backend_sim = IBMQ.get_backend(backends[0])
#{'000': 201, '100': 71, '110': 210, '011': 366, '101': 476, '010': 77, '111': 2605, '001': 90}

#Use this for the simulation
#backend_sim = Aer.get_backend(backends[1])
result = execute(qc, backend_sim, shots=4096).result()
#{'111': 4096} <-  This is the value that we wanted to obtain

#You can obtain the quantum circuit in Latex format.
circuit_drawer(qc).show()

print(result.get_counts(qc))

# The following command doesn't work in commandline, so I recommend you to execute it on a new cell in Anaconda
plot_histogram(result.get_counts(qc))


