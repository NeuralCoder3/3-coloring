from mip import *
from graphs import read_graph
import sys
import time
import os

filename = sys.argv[1]
n, k, edges = read_graph(filename)

m = Model(solver_name=CBC)

# colors = [m.add_var(var_type=INTEGER, lb=0, ub=2) for i in range(n)]
colors = [
    [ m.add_var(var_type=BINARY) for j in range(3) ] 
    for i in range(n)
]

# each vertex has a color
for i in range(n):
    m += xsum(colors[i]) == 1

for u, v in edges:
    for c in range(3):
        m += colors[u][c] + colors[v][c] <= 1
    # m += colors[u] != colors[v]
    
t0 = time.time()
s = m.optimize()
t1 = time.time()
print('It took {:.2f} seconds'.format(t1-t0))
print('Status:', s)