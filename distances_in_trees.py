#!/usr/bin/env python
from sys import argv
from cStringIO import StringIO
from Bio import Phylo

with open(argv[1],'r') as in_file:
  in_data = in_file.read().splitlines()
in_file.closed

l = []
i = 0
while(i < len(in_data)):
  l.append([in_data[i],in_data[i+1]])
  i += 3

t = []
for i in range(len(l)):
  targets=l[i][1].split()
  tree = Phylo.read(StringIO(l[i][0]),"newick")
  t.append(len(tree.trace(targets[0],targets[1])))
  #Phylo.draw_ascii(tree)

for i in t:
  print i

with open('distances_in_trees.txt','w') as out_file:
  for i in t:
    out_file.write(str(str(i)+' '))
out_file.closed
