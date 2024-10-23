from z3 import *
from graphs import read_graph
import sys
import time
import itertools
import os

# environment variable if set else z3
mode = os.getenv('SMT_SOLVER', 'z3').lower()
# mode = 'cvc5'

filename = sys.argv[1]
n, k, edges = read_graph(filename)

s = Solver()
    
colors = [
    [ Bool('v{}_{}'.format(i, j)) for j in range(3) ]
    for i in range(n)
]

for i in range(n):
    # at least one color for each vertex
    s.add(Or(colors[i]))
    # at most one color for each vertex
    # (redundant here but strictly speaking necessary)
    # => 3 more clauses per vertex
    for c1,c2 in itertools.combinations(colors[i], 2):
        # not both (~/\ = \/~)
        s.add(Or(Not(c1), Not(c2)))

for u, v in edges:
    for c in range(3):
        s.add(Or(Not(colors[u][c]), Not(colors[v][c])))
    
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