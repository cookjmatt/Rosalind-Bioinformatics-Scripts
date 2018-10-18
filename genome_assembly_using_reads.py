#!/usr/bin/env python
from sys import argv
import pydot

#Make a directed graph in Pydot for output
graph = pydot.Dot(graph_type='digraph', simplify='true')

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
seq_list = []
if (len(in_data[0]) % 2 == 0):
  check = 0
else:
  check = 1

for i in in_data:
  rc = reverse_comp(i)
  temp   = []
  temprc = []
  for j in range(len(i) / 2 + check):
    temp.append(i[j:j+len(i)/2+check])
    temprc.append(rc[j:j+len(rc)/2+check])
  seq_list.append(temp)
  seq_list.append(temprc)

#Format sets into writeable output
for i in seq_list:
  for j in range(len(i) - 1):
    graph.add_edge(pydot.Edge(i[j],i[j+1]))

seqs = []
i = 0
c = 0
m = len(seq_list)
while (c < m):
  j = 0
  while (j < len(seq_list)):
    if ((i != j) and (seq_list[i][-1] == seq_list[j][0] )):
      seqs.append(seq_list[i])
      i = j
      break
    j += 1
  c += 1

#Output graph
graph.write_svg('genome_assembly.svg')

#Write output
with open('genome_assembly_using_reads.txt','w') as out_file:
  for i in seqs:
    for j in range(len(i)-1):
      out_file.write(i[j][0])
  out_file.write(i[j+1][0])
out_file.closed
