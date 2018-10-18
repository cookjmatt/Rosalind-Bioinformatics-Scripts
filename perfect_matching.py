from sys import argv
import math

with open(argv[1],'r') as in_file:
  in_data=in_file.read().splitlines()
in_file.closed

s = ''
for i in range(1,len(in_data)):
  s += in_data[i]

AU = 0
GC = 0
for i in s:
  if (i == 'A' or i == 'U'):
    AU += 1
  elif (i == 'G' or i == 'C'):
    GC += 1
AU /= 2
GC /= 2

print math.factorial(AU)*math.factorial(GC)
