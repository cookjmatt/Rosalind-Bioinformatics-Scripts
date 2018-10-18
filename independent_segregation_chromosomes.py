#!/usr/bin/env python
from sys import argv
from math import *
from decimal import *

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

with open(argv[1],'r') as in_file:
  n = int(in_file.read().split()[0])
in_file.closed

A = []
for x in reversed(range(0,(2*n))):
  A.append(bin_cdf(x,(2*n),0.5))

with open('independent_segregation_chromosomes.txt','w') as out_file:
  for i in A:
    out_file.write(str(str(round(Decimal(log(i,10)),4))+' '))
out_file.closed
