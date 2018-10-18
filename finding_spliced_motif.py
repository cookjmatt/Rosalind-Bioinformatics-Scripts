#!/usr/bin/env Python
from sys import argv

with open(argv[1],'r') as in_file:
  in_data = in_file.read().splitlines()
in_file.closed

s = in_data[0]
t = []
for i in in_data[1]:
  t.append(i)

indices = []

for i in range(len(s)):
  if ((len(t) != 0) and (s[i] == t[0])):
    indices.append(i+1)
    t.pop(0)

with open("finding_spliced_motif.txt",'w') as out_file:
  for i in indices:
    out_file.write(str(i)+" ")
out_file.closed
