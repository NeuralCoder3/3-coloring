# generate random graphs

import sys
import os
import itertools
import random

# n = int(sys.argv[1])
# k = int(sys.argv[2])

def generate(n,k):
    # sample k edges from n choose 2
    edges = list(itertools.combinations(range(n), 2))
    if k > len(edges):
        # print('k is too large')
        # print('max k is', len(edges))
        # print('k was', k)
        k = len(edges)
    edges = [edges[i] for i in sorted(random.sample(range(len(edges)), k))]
    
    lines = []

    # print(n, k)
    lines += [str(n) + " " + str(k)]
    for edge in edges:
        # print(edge[0], edge[1])
        lines += [str(edge[0]) + " " + str(edge[1])]
        
    return n,k,lines

def read_graph(filename):
    with open(filename) as f:
        lines = f.readlines()
    n, k = map(int, lines[0].split())
    edges = []
    for line in lines[1:]:
        u, v = map(int, line.split())
        edges.append((u, v))
    return n, k, edges
            

def write_graph(filename, lines):
    with open(filename, 'w') as f:
        for line in lines:
            f.write(line + '\n')
            
if __name__ == '__main__':
    output_dir = 'graphs'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    for n in [10,100,1000,10000]:
        max_k = n*(n-1)//2
        for k in [n//10,n//2,n,2*n,10*n,max_k//2, max_k]:
            n,k,lines = generate(n,k)
            filename = os.path.join(output_dir,'graph_' + str(n) + '_' + str(k) + '.txt')
            write_graph(filename, lines)
            print('generated', filename)
            n, k, edges = read_graph(filename)
            # print(n, k, edges)
            # print()