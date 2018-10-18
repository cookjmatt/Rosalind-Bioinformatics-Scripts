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

T = 2**int(in_data[0])
N = int(in_data[1])

prob = 0.0
for i in range(N,T+1):
  prob += (binomial(T,i)*(0.25**i)*(0.75**(T-i)))

print prob
