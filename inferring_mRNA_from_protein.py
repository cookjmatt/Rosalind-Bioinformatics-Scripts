#!/usr/bin/env Python
from sys import argv

with open(argv[1],'r') as in_file:
  in_data = in_file.read().splitlines()
in_file.closed

possibility_table = {'A':4,'C':2,'D':2,\
                     'E':2,'F':2,'G':4,\
                     'H':2,'I':3,'K':2,\
                     'L':6,'M':1,'N':2,\
                     'P':4,'Q':2,'R':6,\
                     'S':6,'T':4,'V':4,\
                     'W':1,'Y':2}

total = 1
for res in in_data[0]:
  total *= possibility_table[res]

with open("inferring_mRNA_from_protein_output.txt",'w') as out_file:
  out_file.write(str(total*3))
out_file.closed
