#!/usr/bin/env python
from sys import argv

with open(argv[1],'r') as in_file:
  in_data = in_file.read().split()
in_file.closed

s = in_data[0]
k = int(in_data[1])
L = int(in_data[2])
t = int(in_data[3])

#Find all kmers of length k in s that appear at least t times
def find_kmers(k,s,t):
  kmer_list = []
  d = {}
  for i in range(0,len(s)-k+1):
    kmer = s[i:i+k]
    if kmer in d:
      temp_list = d[kmer]
      temp_list.append(i)
      d[kmer] = temp_list
    else:
      d[kmer] = [i]
  for i in d:
    temp_list = d[i]
    if len(temp_list) > (t-1):
      kmer_list.append(i)
  return kmer_list

#Run find_kmers through windows of L in s
kmer_list = []
for i in range(0,len(s)-L+1):
  temp_list = find_kmers(k,s[i:i+L],t)
  for i in temp_list:
    if not i in kmer_list:
      kmer_list.append(i)

ans = ''
for i in kmer_list:
  ans += str(i+' ')

with open('clump_finding_problems_output.txt','w') as out_file:
  out_file.write(ans[:-1])
out_file.closed
