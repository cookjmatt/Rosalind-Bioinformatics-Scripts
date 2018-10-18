#!/usr/bin/env Python
from sys import argv
import decimal

with open(argv[1],'r') as in_file:
  in_data = in_file.readlines()
in_file.closed

#Given gc and length m, returns prob. two sequences are equal
def get_prob(p,m):
  return (((2*((p/2)**2))+(2*(((1-p)/2)**2)))**m)

line1 = in_data[0].rstrip().split(" ")
line2 = in_data[1].rstrip().split(" ")

m = int(line1[0])
n = int(line1[1])

gc_list = []
for i in line2:
  gc_list.append(float(i))

with open("intro_expected_value_output.txt",'w') as out_file:
  for prob in range(len(gc_list)):
    i       = gc_list[prob]
    num     = (n-m+1)*get_prob(i,m)
    string  = "%.3f" % num
    out_file.write(string)
    if (prob < len(gc_list) - 1):
      out_file.write(" ")
out_file.closed
