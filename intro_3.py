#!/usr/bin/env python
from sys import argv

with open(argv[1],'r') as in_file:
  in_data = in_file.readlines()
in_file.closed

s = in_data[0]
num_list = in_data[1].split()

for i in range(len(num_list)):
  num_list[i] = int(num_list[i])

with open('intro_3.txt','w') as out_file:
  out_file.write(str(s[num_list[0]:num_list[1]+1]+' '+s[num_list[2]:num_list[3]+1]))
out_file.closed
