#!/usr/bin/env Python
from sys import argv

with open(argv[1],'r') as in_file:
  in_data = in_file.read()
in_file.closed

with open("rna_transcription_output.txt",'w') as out_file:
  for nucleotide in in_data:
    if (nucleotide == 'T'):
      out_file.write('U')
    else:
      out_file.write(nucleotide)
out_file.closed
