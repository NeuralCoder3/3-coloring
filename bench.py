import os
import time 
import sys
import re

files = [
    ("","python colz3.py"),
    ("SMT_SOLVER=cvc5","python colz3.py"),
    ("","python minizinc.py"),
    ("","python colmip.py"),
    ("","python colz3_sat.py"),
    ("SMT_SOLVER=cvc5","python colz3_sat.py"),
    ("SOLVER=solver","python sat.py"),
    ("SOLVER=glucose","python sat.py"),
    ("SOLVER=minisat","python sat.py"),
    ("SOLVER=lingeling","python sat.py"),
]
graphs = os.listdir("graphs")
graphs = [
    # "graph_1000_1000.txt", 
    "graph_1000_2000.txt", # 4s / 21s
    "graph_1000_10000.txt", 
    # "graph_10000_1000.txt", 
    # "graph_10000_5000.txt", 
    # "graph_10000_10000.txt", 
    # "graph_1000_249750.txt"
]
timeout = 10

def sort_by_numbers(xs):
    # sort strings by numbers in them
    def key(s):
        numbers = re.findall(r'\d+', s)
        return [int(n) for n in numbers]
    
    return sorted(xs, key=key)
    

for graph in sort_by_numbers(graphs):
    print("graph", graph)
    print("env","command","file","time", sep="\t")
    for env,file in files:
        t0 = time.time()
        # os.system("python3 " + file + " graphs/" + graph)
        # run without printing
        # os.system("python3 " + file + " graphs/" + graph + " > /dev/null")
        # run with timeout
        os.system(env+" timeout " + str(timeout) + " " + file + " graphs/" + graph + " > /dev/null 2>&1")
        t1 = time.time()
        tdiff = t1 - t0
        # print(env, file, graph, tdiff)
        # separated by tab
        print(env, file, graph, tdiff, sep="\t")
        sys.stdout.flush()