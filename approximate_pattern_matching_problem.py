#!/usr/bin/env python
from sys import argv

with open(argv[1],'r') as in_file:
  in_data = in_file.read().split()
in_file.closed

kmer = in_data[0]
s    = in_data[1]
d    = int(in_data[2])
k    = len(kmer)

def num_mismatches(k,l):
  mismatches = 0
  for i in range(0,len(k)):
    if (not(k[i] == l[i])):
      mismatches += 1
  return mismatches

ans = ''
for i in range(0,len(s)-k+1):
  temp_kmer = s[i:i+k]
  if num_mismatches(kmer,temp_kmer) < (d+1):
    ans += str(str(i)+' ')

with open('approximate_pattern_matching_problems_output.txt','w') as out_file:
  out_file.write(ans[:-1])
out_file.closed
