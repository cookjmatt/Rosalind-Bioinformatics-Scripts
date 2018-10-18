#!/usr/bin/env python
from sys import argv
from igraph import *

with open(argv[1],'r') as in_file:
  in_data = in_file.read().splitlines()
in_file.closed

def tree_search(index,l):
  for i in (range(len(adjacency_list))):
    if ((l[index][1] == l[i][0]) or (l[index][1] == l[i][0])):
      return 1+tree_search(i,l)
  return 0

n = int(in_data[0])
adjacency_list = []
for i in range(1,len(in_data)):
  line = in_data[i].split()
  adjacency_list.append((int(line[0])-1,int(line[1])-1))

g = Graph(n)
g.add_edges(adjacency_list)

with open('completing_tree.txt','w') as out_file:
  out_file.write(str(len(g.clusters())-1))
out_file.closed
