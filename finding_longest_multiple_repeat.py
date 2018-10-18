#!/usr/bin/env python
from sys import argv

with open(argv[1],'r') as in_file:
  in_data = in_file.read().splitlines()
in_file.closed

s = in_data[0][:-1]
k = int(in_data[1])

#Get number of nodes and create array for number of children of each node
nodes = 0
for i in range(2,len(in_data)):
  line = in_data[i].split()
  if (int(line[0][4:]) > nodes):
    nodes = int(line[0][4:])
  if (int(line[1][4:]) > nodes):
    nodes = int(line[1][4:])
narray = [0]*nodes

#Make array for each node that indicates number of children for the node
for i in range(2,len(in_data)):
  line = in_data[i].split()
  narray[int(line[0][4:])-1] += 1

#Find deepest node with number of children > k-1
dnode = 0
for i in reversed(range(len(narray))):
  if (narray[i] > (k-1)):
    dnode = i+1
    break

#Get deepest node lists
dnode_list = []
for i in range(2,len(in_data)):
  line = in_data[i].split()
  if (int(line[0][4:]) == dnode):
    dnode_list.append(line)

for i in dnode_list:
  print i
#with open('finding_longest_multiple_repeat.txt','w') as out_file:

#out_file.closed
