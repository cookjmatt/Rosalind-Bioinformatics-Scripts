#!/usr/bin/env Python
from sys import argv
from collections import Counter
import decimal

with open(argv[1],'r') as in_file:
  in_data = in_file.read().rstrip().split(" ")
in_file.closed

prob_list = []
for entry in in_data:
  i = float(entry)
  prob = 2*((i/2)*(i/2))+2*(((1-i)/2)*((1-i)/2))
  prob_list.append(round(decimal.Decimal(prob),3))

with open("intro_probability_output.txt",'w') as out_file:
  for i in range(len(prob_list)):
    out_file.write(str(prob_list[i]))
    if (i < len(prob_list) - 1):
      out_file.write(" ")
out_file.closed
