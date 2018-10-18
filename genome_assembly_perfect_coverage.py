#!/usr/bin/env python
from sys import argv

#Open input file and get data
with open(argv[1],'r') as in_file:
  in_data = in_file.read().splitlines()
in_file.closed

#Get input sequences
seq_list = []
for i in in_data:
  seq_list.append((i[:-1],i[1:]))

#Get sequence
seq = ''
counter = 0
i = 0
while (counter < len(seq_list)):
  counter += 1
  seq += seq_list[i][0][0]
  for j in range(len(seq_list)):
    if (seq_list[j][0] == seq_list[i][1]):
      i = j
      break

#Write output
with open('genome_assembly_perfect_coverage.txt','w') as out_file:
  out_file.write(seq)
out_file.closed
