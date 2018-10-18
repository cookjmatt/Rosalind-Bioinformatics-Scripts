#!/usr/bin/env Python
from sys import argv

#Genetic code table
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

#Return RNA transcription of a DNA sequence
def transcribe(seq):
  rna = ""
  for nucleotide in seq:
    if (nucleotide == 'T'):
      rna += 'U'
    else:
      rna += nucleotide
  return rna

#Translate an RNA sequence:
def translate(seq):
  prot = ""
  i = 0
  while (i < len(seq) - 2):
    codon = ""
    for j in range(3):
      codon += seq[i+j]
    prot += genetic_code[codon]
    i += 3
  return prot

#Open input file and get data
with open(argv[1],'r') as in_file:
  in_data = in_file.read().splitlines()
in_file.closed

#Get dna sequence and put intron sequences into list
dna_seq = in_data[0]
introns = []
for i in range(len(in_data) - 1):
  introns.append(in_data[i+1])

#Cut out introns from sequence
for i in introns:
  while (i in dna_seq):
    index = dna_seq.find(i)
    dna_seq = dna_seq[:index]+dna_seq[index+len(i):]

#Write output to file
with open("rna_splicing_output.txt",'w') as out_file:
  out_file.write(translate(transcribe(dna_seq))+"\n")
out_file.closed
