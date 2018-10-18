#!/usr/bin/env Python
from sys import argv
import itertools
import math

with open(argv[1],'r') as in_file:
  in_data = in_file.read().splitlines()
in_file.closed

n =int(in_data[0])

permute = []
for i in range(n):
  permute.append(i+1)

with open("enumerating_gene_orders_output.txt",'w') as out_file:
  out_file.write(str(math.factorial(n))+"\n")
  for i in set(itertools.permutations(permute)):
    for j in i:
      out_file.write(str(j)+" ")
    out_file.write("\n")
out_file.closed
