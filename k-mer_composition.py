#!/usr/bin/env python
from sys import argv
import itertools

#Open file and get data
with open(argv[1],'r') as in_file:
  in_data = in_file.read().splitlines()
in_file.closed

#Get DNA as single string from FASTA format
dna = ''
for i in range(1,len(in_data)):
  dna += in_data[i]

#Generate k-mer array, A
mer = 4
A = {}
prod = itertools.product('ACGT',repeat = mer)
prod_list = []
for i in prod:
  prod_list.append(''.join(i))
  A[''.join(i)] = 0

#Loop through all k-mers in the dna string and add to k-mer array
for i in range(0,len(dna)-3):
  kmer = ''
  for j in range(i,i+4):
    kmer += dna[j]
  A[kmer] += 1

#Write output to file:
with open('k-mer_composition.txt','w') as out_file:
  for i in prod_list:
    out_file.write(str(A[i])+' ')
out_file.closed
