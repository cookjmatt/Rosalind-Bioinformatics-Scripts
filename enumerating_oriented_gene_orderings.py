#!/usr/bin/env Python
from sys import argv
import itertools

with open(argv[1],'r') as in_file:
  in_data = in_file.read().splitlines()
in_file.closed

lst = []
n =int(in_data[0])
sum = 0
for i in range(1,n+1):
  sum += i
  lst.append(int(i))
  lst.append(-int(i))

final_list = []
perms = itertools.permutations(lst,n)
for i in perms:
  temp_set = []
  for j in i:
    temp_set.append(abs(j))
  if (len(set(temp_set)) == len(i)):
    final_list.append(i)

with open("enumerating_oriented_gene_orderings_output.txt",'w') as out_file:
  out_file.write(str(len(final_list))+"\n")
  for i in final_list:
    for j in i:
      out_file.write(str(j)+" ")
    out_file.write("\n")
out_file.closed
