#!/usr/bin/env
from sys import argv

with open(argv[1],'r') as in_file:
  in_data = in_file.readlines()
in_file.closed

with open('intro_5.txt','w') as out_file:
  for i in range(len(in_data)):
    if ((i % 2) == 1):
      out_file.write(in_data[i])
out_file.closed
