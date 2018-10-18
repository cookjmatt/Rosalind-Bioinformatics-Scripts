#!/usr/bin/env python
from sys import argv

def binomial(n,k):
  bc = [1 for i in range(0,k+1)]
  for j in range(1,n-k+1):
    for i in range(1,k+1):
      bc[i]=bc[i-1]+bc[i]
  return bc[k]

with open(argv[1],'r') as in_file:
  in_data = in_file.read().split()
in_file.closed

n = int(in_data[0])
m = int(in_data[1])

s = 0
for k in range(m,n+1):
  s += binomial(n,k)

with open('alternative_splicing.txt','w') as out_file:
  out_file.write(str(s%1000000))
out_file.closed
