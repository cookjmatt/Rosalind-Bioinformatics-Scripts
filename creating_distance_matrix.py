#!/usr/bin/env
from sys import argv

#Get input data
with open(argv[1],'r') as in_file:
  in_data = in_file.read().splitlines()
in_file.closed

#Takes two sequences and returns their p-distance
def pdist(v,w):
  i = 0
  diff = 0
  while (i < len(v)):
    if (v[i] != w [i]):
      diff += 1
    i += 1
  return float(diff) / float(len(v))

#Get sequences and names into two corresponding lists
seq_array = []
name_array = []
i = 0
while (i < len(in_data) - 1):
  name_array.append(in_data[i][1:])
  seq = ''
  i += 1
  while (i < len(in_data) and in_data[i][0] != '>'):
    seq += in_data[i]
    i += 1
  seq_array.append(seq)

with open('creating_distance_matrix.txt','w') as out_file:
  for i in range (0, len(seq_array)):
    for j in range (0, len(seq_array)):
      out_file.write('{:.2f} '.format(pdist(seq_array[i], seq_array[j])))
    out_file.write('\n')
out_file.closed
