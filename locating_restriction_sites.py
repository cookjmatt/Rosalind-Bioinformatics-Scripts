#!/usr/bin/env Python
from sys import argv

#Return reverse complement of a DNA sequence
def reverse_complement(seq):
  rc_seq = ""
  for nucleotide in reversed(seq):
    if (nucleotide == 'A'):
      rc_seq += ('T')
    elif (nucleotide == 'T'):
      rc_seq += ('A')
    elif (nucleotide == 'G'):
      rc_seq += ('C')
    elif (nucleotide == 'C'):  
      rc_seq += ('G')
  return rc_seq

with open (argv[1],'r') as in_file:
  in_data = in_file.read().splitlines()
in_file.closed

#Search for reverse complements between 4-8 nucleotides and add to list
sites = []
i = 0
while (i < len(in_data[0])):
  for x in range(5):
    j = 0
    sub_seq = ""
    if (i < (len(in_data[0]) - (x + 3))):
      while (j < (x + 4)):
        sub_seq += in_data[0][i+j]
        j += 1
    if ((sub_seq != "") and (sub_seq == reverse_complement(sub_seq))):
      sites.append([i+1,(x+4)])
  i += 1

#Write restriction sites and lengths to file
with open("locating_restriction_sites_output.txt",'w') as out_file:
  for i in sites:
    out_file.write(str(i[0])+" "+str(i[1])+"\n")
out_file.closed
