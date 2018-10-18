#!/usr/bin/env python
from sys import argv
from decimal import *

with open(argv[1],'r') as in_file:
  in_data = in_file.read().splitlines()
in_file.closed

n = int(in_data[0])
s = in_data[1]
A = [float(i) for i in in_data[2].split()]

gc = 0
for i in s:
  if (i == 'G' or i == 'C'):
    gc += 1
at = len(s)-gc

gc_array = []
for i in A:
  gc_array.append(((i/2)**gc)*(((1-i)/2)**at))

with open('expected_number_restriction_sites.txt','w') as out_file:
  for i in gc_array:
    out_file.write(str(str(round(Decimal(i*(n-1)),3))+' '))
out_file.closed
