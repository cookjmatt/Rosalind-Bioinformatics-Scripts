#!/usr/bin/env Python
from sys import argv
import decimal

with open(argv[1],'r') as in_file:
  in_data = in_file.read().splitlines()
in_file.closed

monoisotopic_mass_table = {'A':71.03711,'C':103.00919,'D':115.02694,\
                           'E':129.04259,'F':147.06841,'G':57.02146,\
                           'H':137.05891,'I':113.08406,'K':128.09496,\
                           'L':113.08406,'M':131.04049,'N':114.04293,\
                           'P':97.05276,'Q':128.05858,'R':156.10111,\
                           'S':87.03203,'T':101.04768,'V':99.06841,\
                           'W':186.07931,'Y':163.06333}

reverse_mass_table = dict((reversed(item) for item in monoisotopic_mass_table.items()))

diff_table = []
for i in range(len(in_data)-1):
  diff_table.append(float(in_data[i+1])-float(in_data[i]))

seq = []
for i in diff_table:
  for j in reverse_mass_table:
    if ((i > (j - 0.01)) and (i < (j + 0.01))):
      seq.append(reverse_mass_table[j])

with open('inferring_protein_spectrum.txt','w') as out_file:
  out_file.write("".join(seq))
out_file.closed
