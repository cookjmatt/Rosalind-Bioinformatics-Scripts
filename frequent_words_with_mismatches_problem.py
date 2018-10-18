#!/usr/bin/env python
from sys import argv
with open(argv[1],'r') as in_file:
  in_data = in_file.read().split()
in_file.closed

s = in_data[0]
k = int(in_data[1])
diff = int(in_data[2])

#Calculate the number of mismatches between two kmers
def num_mismatches(k,l):
  mismatches = 0
  for i in range(0,len(k)):
    if (not(k[i] == l[i])):
      mismatches += 1
  return mismatches

#Create dictionary with number of occurances of all kmers
d = {}
for i in range(0,len(s)-k+1):
  kmer = s[i:i+k]
  if kmer in d:
    d[kmer] = d[kmer] + 1
  else:
    d[kmer] = 1

#Create list of all kmers
kmer_list = []
for i in d:
  kmer_list.append(i)

#Create dictionary with all possible mutant kmers

