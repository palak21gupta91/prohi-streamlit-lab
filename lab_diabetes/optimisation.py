from minizinc import Instance, Solver

MODEL = """
int: n;
array[1..n, 1..5] of 0..100: features;
array[1..5] of int: weights = [35, 25, 20, 10, 10];

var 1..n: patient;

solve maximize
    sum(j in 1..5) (weights[j] * features[patient, j]);
"""

PRIORITY_FEATURES = [
    "number_inpatient",
    "number_emergency",
    "number_diagnoses",
    "time_in_hospital",
    "num_medications",
]

def choose_patient(features: list[list[int]]) -> int:
    instance = Instance(Solver.lookup("gecode"))
    instance.add_string(MODEL)
    instance["n"] = len(features)
    instance["features"] = features

    return instance.solve()["patient"] - 1