from graphs import read_graph
import sys
import itertools
import time
import os

from pysat.formula import CNF
from pysat.solvers import Solver, Glucose3, Minisat22, Lingeling

filename = sys.argv[1]
n, k, edges = read_graph(filename)
mode = os.getenv('SOLVER', 'solver').lower()

vars = [
    [
        n*i+j+1
        for j in range(3)
    ]
    for i in range(n)
]

formula = CNF()

for i in range(n):
    # each node has a color
    # Or(colors of vertex i)
    formula.append(vars[i])
    # at most one color (see colz3_sat)
    for c1,c2 in itertools.combinations(vars[i], 2):
        formula.append([-c1, -c2])
    
# no two adjacent nodes have the same color
# Or(Not(color of vertex u), Not(color of vertex v)) for each color
for u, v in edges:
    for c in range(3):
        formula.append([-vars[u][c], -vars[v][c]])

if mode == 'glucose':
    Sol = Glucose3
elif mode == 'minisat':
    Sol = Minisat22
elif mode == 'lingeling':
    Sol = Lingeling
else:
    Sol = Solver

with Sol(bootstrap_with=formula) as solver:
    t0 = time.time()
    res = solver.solve()
    t1 = time.time()
    print('It took {:.2f} seconds'.format(t1-t0))
    if res:
        print("Solution")
        # for i in range(n):
        #     for j in range(3):
        #         if solver.solve(assumptions=[vars[i][j]]):
        #             print(i, j)
    else:
        print("No solution")