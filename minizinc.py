from graphs import read_graph
import sys
import time
import os

filename = sys.argv[1]
n, k, edges = read_graph(filename)

with open("tmp.dzn", "w") as f:
    f.write("n = {};\n".format(n))
    f.write("k = {};\n".format(k))
    f.write("edges = \n")
    for i, (u,v) in enumerate(edges):
        if i==0:
            f.write("[| ")
        else:
            f.write(" | ")
        f.write(f"{u+1}, {v+1},\n")
    # f.write("edges = [|")
    # for u, v in edges:
    #     f.write("  | {},{},\n".format(u,v))
    f.write("|];\n")
    
t0 = time.time()
os.system("minizinc coloring.mzn tmp.dzn")
t1 = time.time()
print('It took {:.2f} seconds'.format(t1-t0))