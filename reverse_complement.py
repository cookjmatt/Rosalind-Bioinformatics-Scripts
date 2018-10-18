#!/usr/bin/env Python
from sys import argv

with open(argv[1],'r') as in_file:
  in_data = in_file.read()
in_file.closed

with open("reverse_complement_output.txt",'w') as out_file:
  for nucleotide in reversed(in_data):
    if (nucleotide == 'A'):
      out_file.write('T')
    elif (nucleotide == 'T'):
      out_file.write('A')
    elif (nucleotide == 'G'):
      out_file.write('C')
    elif (nucleotide == 'C'):
      out_file.write('G')
out_file.closed
