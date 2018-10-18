#!/usr/bin/env python
from sys import argv

with open(argv[1],'r') as in_file:
  in_data = in_file.read().split()
in_file.closed

for i in range(len(in_data)):
  in_data[i] = int(in_data[i])

dom_probs = [1,1,1,0.75,0.5,0]

exp = 0
for i in range(len(in_data)):
  exp += 2*in_data[i]*dom_probs[i]

with open('expected_offspring.txt','w') as out_file:
  out_file.write(str(exp))
out_file.closed
