#!/usr/bin/env python
from sys import argv

with open(argv[1],'r') as in_file:
  in_data = in_file.read().splitlines()
in_file.closed

#Turn seqs into single strings
seqs = []
seq = ''
for i in in_data:
  if (i[0] == '>'):
    if (len(seq) != 0):
      seqs.append(seq)
    seq = ''
  else:
    seq += i
seqs.append(seq)

transitions = 0
transversions = 0
for i in range(len(seqs[0])):
  n1 = seqs[0][i]
  n2 = seqs[1][i]
  if (n1 == 'G'):
    if (n2 == 'A'):
      transitions += 1
    elif (n2 == 'T' or n2 == 'C'):
      transversions += 1
  elif (n1 == 'C'):
    if (n2 == 'T'):
      transitions += 1
    elif (n2 == 'A' or n2 == 'G'):
      transversions += 1
  elif (n1 == 'A'):
    if (n2 == 'G'):
      transitions +=1 
    elif (n2 == 'C' or n2 == 'T'):
      transversions += 1
  elif (n1 == 'T'):
    if (n2 == 'C'):
      transitions += 1
    elif (n2 == 'A' or n2 == 'G'):
      transversions += 1

with open('transitions_transversions.txt','w') as out_file:
  out_file.write(str(float(transitions)/float(transversions)))
out_file.closed
