#!/usr/bin/env python
from sys import argv

def binomial(n,k):
  bc = [1 for i in range(0,k+1)]
  for j in range(1,n-k+1):
    for i in range(1,k+1):
      bc[i]=bc[i-1]+bc[i]
  return bc[k]

def bin_cdf(x,n,p):
  s = 0
  for i in range(0,x+1):
    s += (binomial(n,i)*(p**i)*((1-p)**(n-i)))
  return s

A = []
with open(argv[1],'r') as in_file:
  [A.append(float(i)) for i in in_file.read().split()]
in_file.closed

N = int(A[0])
m = A[1]
g = int(A[2])
k = int(A[3])

p = (m/(2*N))
q = (1.0 - p)

print "%0.4f " % (1-bin_cdf(k,N,p**g))
