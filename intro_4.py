#!/usr/bin/env python
from sys import argv

with open(argv[1],'r') as in_file:
  in_data = in_file.read().split()
in_file.closed

s = 0
for i in range(int(in_data[0]),int(in_data[1])):
  if ((i % 2) == 1):
    s += i

with open('intro_4.txt','w') as out_file:
  out_file.write(str(s))
out_file.closed
