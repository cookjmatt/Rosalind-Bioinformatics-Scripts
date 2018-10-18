#!/usr/bin/env python

from sys import argv

with open(argv[1],'r') as in_file:
  in_data = in_file.read().split()
in_file.closed

kmer = in_data[0]
m = int(len(kmer))
s = in_data[1]
ans = ''

for i in range(0,len(s)-m-1):
  temp = s[i:i+m]
  if kmer == temp:
    ans += str(str(i)+' ')

with open('pattern_matching_problem_output.txt','w') as out_file:
  out_file.write(ans[:-1])
out_file.closed
