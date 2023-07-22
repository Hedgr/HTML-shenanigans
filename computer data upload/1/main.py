import os
import tempfile
from qiskit.exceptions import MissingOptionalLibraryError
from qiskit.circuit.library.phase_oracle import PhaseOracle
from qiskit.algorithms import AmplificationProblem
from qiskit.algorithms import Grover
from qiskit.primitives import Sampler
from qiskit.tools.visualization import plot_histogram


def do_grovers(num):
    input_3sat_instance = '''
    c example DIMACS-CNF 3-SAT
    p cnf 3 5
    -1 -2 -3 0
    1 -2 3 0
    1 2 -3 0
    1 -2 -3 0
    -1 2 3 0
    '''

    fp = tempfile.NamedTemporaryFile(mode='w+t', delete=False)
    fp.write(input_3sat_instance)
    file_name = fp.name
    fp.close()
    oracle = None
    try:
        oracle = PhaseOracle.from_dimacs_file(file_name)
    except ImportError as ex:
        print(ex)
    finally:
        os.remove(file_name)

    problem = None
    if oracle is not None:
        problem = AmplificationProblem(oracle, is_good_state=oracle.evaluate_bitstring)

    grover = Grover(sampler=Sampler())
    result = None
    if problem is not None:
        result = grover.amplify(problem)
        print(result.assignment)

    if result is not None:
        plot_histogram(result.circuit_results[0], filename="histogram.png")


# for i in range(2^15):
byte = bytearray