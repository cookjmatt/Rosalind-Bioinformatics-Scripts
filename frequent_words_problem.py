#!/usr/bin/env python

from sys import argv

with open(argv[1],'r') as in_file:
  in_data = in_file.read().split()
in_file.closed

s = in_data[0]
m = int(in_data[1])
d={}
mx = 0
for i in range(0,len(s)-m-1):
  kmer = s[i:i+m]
  if kmer in d:
    d[kmer] = d[kmer] + 1
    if d[kmer] > mx:
      mx = d[kmer]
  else:
    d[kmer] = 1

answer = ''
for i in d:
  if d[i] == mx:
    answer += str(i+' ')

with open('frequent_words_problem.txt','w') as out_file:
  out_file.write(answer)
out_file.closed
