#!/usr/bin/env python
from sys import argv

with open(argv[1],'r') as in_file:
  in_data = in_file.read().split()
in_file.closed

n = int(in_data[0])
k = int(in_data[1])

prod = 1
for i in range((n-k+1),n+1):
  prod *= i

with open('partial_permutations.txt','w') as out_file:
  out_file.write(str(prod%1000000))
out_file.closed
