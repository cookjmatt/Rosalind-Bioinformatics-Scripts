#!/usr/bin/env Python
from sys import argv

with open(argv[1],'r') as in_file:
  in_data = in_file.read().splitlines()
in_file.closed

s_len = len(in_data[0])
t_len = len(in_data[1])

locations = []
for i in range(s_len):
  if ((i + t_len) < s_len):
    if (in_data[0][i:i+t_len] == in_data[1]):
      locations.append(i+1)

with open("finding_motif_dna_output.txt",'w') as out_file:
  for i in range(len(locations)):
    out_file.write(str(locations[i]))
    if not(i == len(locations) - 1):
      out_file.write(" ")
out_file.closed
