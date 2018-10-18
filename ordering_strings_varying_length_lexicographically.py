#!/usr/bin/env python
from sys import argv
import itertools

with open(argv[1],'r') as in_file:
  in_data = in_file.readlines()
in_file.closed

lst = in_data[0].strip().split()
n = int(in_data[1].strip())

alphabet = ''.join(lst)

perms = []
for i in range(1,n+1):
  temp_perms = itertools.product(lst,repeat=i)
  for j in temp_perms:
    perms.append(j)

sort_perms = sorted(perms, key=lambda word: [alphabet.index(c) for c in word])

with open('ordering_strings_varying_length_lexicographically.txt','w') as out_file:
  for i in range(len(sort_perms)):
    sort_perms[i] = ''.join(sort_perms[i])
    out_file.write(sort_perms[i]+'\n')
out_file.closed
