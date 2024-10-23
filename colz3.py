from z3 import *
from graphs import read_graph
import sys
import time
import os

# environment variable if set else z3
mode = os.getenv('SMT_SOLVER', 'z3').lower()
# mode = 'cvc5'

filename = sys.argv[1]
n, k, edges = read_graph(filename)

s = Solver()
    
# 3 coloring => 3 colors, no two adjacent vertices have the same color

# create a variable for each vertex
vertices = [Int('v{}'.format(i)) for i in range(n)]
for i in range(n):
    s.add(And(vertices[i] >= 0, vertices[i] < 3))
    
# no two adjacent vertices have the same color
for u, v in edges:
    s.add(vertices[u] != vertices[v])
    
if mode == 'cvc5':
    with open('graph.smt2', 'w') as f:
        f.write(s.to_smt2())
    t0 = time.time()
    res = os.system('cvc5 graph.smt2')
    t1 = time.time()
    print('It took {:.2f} seconds'.format(t1-t0))
    
elif mode == 'z3':
    print("Checking satisfiability")
    t0 = time.time()
    res = s.check()
    t1 = time.time()
    print('It took {:.2f} seconds'.format(t1-t0))

    if res == sat:
        m = s.model()
        print("Solution")
        # for i in range(n):
        #     print(m[vertices[i]].as_long())
    else:
        print("No solution")
        
else:
    print("Unknown mode", mode)
    sys.exit(1)