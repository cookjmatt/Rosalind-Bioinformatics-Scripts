#!/usr/bin/env python
from sys import argv
import pydot

#Make a directed graph in Pydot for output
graph = pydot.Dot(graph_type='digraph')

#Return the reverse complement of a sequence
def reverse_comp(v):
  w = ''
  rc_dict = {'A':'T','T':'A','G':'C','C':'G'}
  for i in reversed(v):
    w += rc_dict[i]
  return w

#Open input file and get data
with open(argv[1],'r') as in_file:
  in_data = in_file.read().splitlines()
in_file.closed

#Get input sequences and their reverse complements into sets
s = []
rc = []
for i in in_data:
  s.append(i)
  rc.append(reverse_comp(i))
s = frozenset(s)
rc = frozenset(rc)
uset = frozenset.union(s,rc)
seq_list = []
for i in uset:
  seq_list.append(i)
seq_list.sort()

#Format sets into writeable output
write_list = []
for i in seq_list:
  #Add edges to graph
  graph.add_edge(pydot.Edge(i[:-1],i[1:]))
  write_list.append('('+i[:-1]+', '+i[1:]+')')

#Output graph
graph.write_png('debruijn_graph.png')

#Write output
with open('debruijn_graph.txt','w') as out_file:
  for i in write_list:
    out_file.write(i+'\n')
out_file.closed
