#!/usr/bin/env Python
from sys import argv
import itertools

with open(argv[1],'r') as in_file:
  in_data = in_file.read().splitlines()
in_file.closed

hamming_distance = 0

for nuc1,nuc2 in itertools.izip(in_data[0],in_data[1]):
  if not(nuc1 == nuc2):
    hamming_distance += 1

with open("counting_point_mutations_output.txt",'w') as out_file:
  out_file.write(str(hamming_distance))
out_file.closed
