#!/usr/bin/env python
from sys import argv

with open(argv[1],'r') as in_file:
  in_data = in_file.read().split()
in_file.closed


N = int(in_data[0])
GC = float(in_data[1])
s = in_data[2]

GC_num = 0.0
for i in s:
  if (i == 'G' or i == 'C'):
    GC_num += 1

s_prob = (((GC/2)**GC_num)*(((1-GC)/2)**(len(s)-GC_num)))

print str("%0.3f" % (1-(1-s_prob)**N))
