#!/usr/bin/env Python
from sys import argv
import itertools

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
amino_acids = [key for key in monoisotopic_mass_table.keys()]
reverse_mass_table = dict((reversed(item) for item in monoisotopic_mass_table.items()))

total_mass = float(in_data[0])
peaks = []
for i in range(1,len(in_data)):
  peaks.append(float(in_data[i]))
peaks.sort()
length = ((len(peaks) - 2) / 2)


#Collect pairs of peaks
do_not_add = []
col_peaks = []
for i in peaks:
  for j in peaks:
    sum = i + j
    if (((sum < (total_mass + 0.01)) and (sum > (total_mass - 0.01))) and not((i in do_not_add) or (j in do_not_add))):
      col_peaks.append((i,j))
      col_peaks.append((j,i))
      do_not_add.append(i)
      do_not_add.append(j)
col_peaks.sort()

do_not_add = []
i = 0
j = 1
m = len(col_peaks)
  


'''
do_not_add = []
collected = []
for i in range(len(peaks)-1):
  for j in range(i+1,len(peaks)):
    diff = peaks[j] - peaks[i]
    summ = peaks[j] + peaks[i]
    for k in reverse_mass_table:
      if (((diff > (k - 0.01)) and (diff < (k + 0.01))) and not((sum < (total_mass + 0.1)) and (sum > (total_mass - 0.1)))):
        if not((peaks[i] in do_not_add) or (peaks[j] in do_not_add)):
          collected.append((peaks[i],peaks[j],reverse_mass_table[k]))
          do_not_add.append(peaks[i])
          do_not_add.append(peaks[j])
for i in collected:
  print i
'''

#with open('peptide_full_spectrum.txt','w') as out_file:
#  out_file.write("".join(seq))
#out_file.closed()
