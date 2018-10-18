#!/usr/bin/env Python
from sys import argv

with open(argv[1],'r') as in_file:
  in_data = in_file.read().splitlines()
in_file.closed
line = in_data[0]

genetic_code = {'UUU':'F','UUC':'F','UUA':'L','UUG':'L',\
                'CUU':'L','CUC':'L','CUA':'L','CUG':'L',\
                'AUU':'I','AUC':'I','AUA':'I','AUG':'M',\
                'GUU':'V','GUC':'V','GUA':'V','GUG':'V',\
                'UCU':'S','UCC':'S','UCA':'S','UCG':'S',\
                'CCU':'P','CCC':'P','CCA':'P','CCG':'P',\
                'ACU':'T','ACC':'T','ACA':'T','ACG':'T',\
                'GCU':'A','GCC':'A','GCA':'A','GCG':'A',\
                'UAU':'Y','UAC':'Y','UAA':'','UAG':'',\
                'CAU':'H','CAC':'H','CAA':'Q','CAG':'Q',\
                'AAU':'N','AAC':'N','AAA':'K','AAG':'K',\
                'GAU':'D','GAC':'D','GAA':'E','GAG':'E',\
                'UGU':'C','UGC':'C','UGA':'','UGG':'W',\
                'CGU':'R','CGC':'R','CGA':'R','CGG':'R',\
                'AGU':'S','AGC':'S','AGA':'R','AGG':'R',\
                'GGU':'G','GGC':'G','GGA':'G','GGG':'G',}

with open("protein_translation_output.txt",'w') as out_file:
  i = 0
  while (i < len(line) - 2):
   codon = ""
   for j in range(3):
      codon += line[i+j]
   out_file.write(genetic_code[codon])
   i += 3
out_file.closed
