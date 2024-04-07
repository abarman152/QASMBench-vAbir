import os
from qiskit import QuantumCircuit

def verify_circuit(qasm_path):
    QuantumCircuit.from_qasm_file(qasm_path)

# def verify_cat(cat):
#     cat_circ = next(os.walk('C:/Users/abirb/Dropbox/PROJECT/Side_Channel_Attack/QASMBench/'+cat+'/'))
#     for circ in cat_circ:
#         print (circ)
#         path = str('C:/Users/abirb/Dropbox/PROJECT/Side_Channel_Attack/QASMBench/' + cat + '/' + circ + '/' + circ + ".qasm")
#         print ('checking ' + path + '...\n')
#         verify_circuit(path)

def verify_cat(cat):
    cat_path = 'C:/Users/abirb/Dropbox/PROJECT/Side_Channel_Attack/QASMBench/' + cat + '/'
    for root, dirs, files in os.walk(cat_path):
        for circ in files:
            if circ.endswith('.qasm'):
                path = os.path.join(root, circ)
                print('checking ' + path + '...\n')
                verify_circuit(path)


verify_cat('small')
#verify_cat('medium')
#verify_cat('large')
