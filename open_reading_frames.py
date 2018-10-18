#!/usr/bin/env Python
from sys import argv
import sets

#Genetic code table
genetic_code = {'UUU':'F','UUC':'F','UUA':'L','UUG':'L',\
                'CUU':'L','CUC':'L','CUA':'L','CUG':'L',\
                'AUU':'I','AUC':'I','AUA':'I','AUG':'M',\
                'GUU':'V','GUC':'V','GUA':'V','GUG':'V',\
                'UCU':'S','UCC':'S','UCA':'S','UCG':'S',\
                'CCU':'P','CCC':'P','CCA':'P','CCG':'P',\
                'ACU':'T','ACC':'T','ACA':'T','ACG':'T',\
                'GCU':'A','GCC':'A','GCA':'A','GCG':'A',\
                'UAU':'Y','UAC':'Y','UAA':'*','UAG':'*',\
                'CAU':'H','CAC':'H','CAA':'Q','CAG':'Q',\
                'AAU':'N','AAC':'N','AAA':'K','AAG':'K',\
                'GAU':'D','GAC':'D','GAA':'E','GAG':'E',\
                'UGU':'C','UGC':'C','UGA':'*','UGG':'W',\
                'CGU':'R','CGC':'R','CGA':'R','CGG':'R',\
                'AGU':'S','AGC':'S','AGA':'R','AGG':'R',\
                'GGU':'G','GGC':'G','GGA':'G','GGG':'G',}

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

#Given a protein sequence, remove non-stop codon trailing residues
def chomp_prot(seq):
  i = len(seq) - 1
  while ((i > -1) and (seq[i] != '*')):
    i -=1
  return seq[:i]

#Given a protein sequence, split into residues separated by stop codons
def modify_prot(seq):
  i = 0
  seqs = []
  while (i < len(seq)):
    new_seq = ""
    while ((i < len(seq)) and (seq[i] != '*')):
      new_seq += seq[i]
      i += 1
    seqs.append(new_seq)
    i += 1
  return seqs

#Given a modified protein sequence, return a list of open reading frames
def orf(seq):
  orfs = []
  i = 0
  while (i < len(seq)):
    if (seq[i] == 'M'):
      orfs.append(seq[i:])
    i += 1
  return orfs

#Open input file
with open(argv[1],'r') as in_file:
  in_data = in_file.read().split()
in_file.closed

#Create 6 possible frames and add them to a list
frames = []
frame1 = in_data[0]
frames.append(frame1)
frame2 = frame1[1:]
frames.append(frame2)
frame3 = frame2[1:]
frames.append(frame3)
frame4 = reverse_complement(in_data[0])
frames.append(frame4)
frame5 = frame4[1:]
frames.append(frame5)
frame6 = frame5[1:]
frames.append(frame6)

#Create list of open reading frames
orfs = []
for i in frames:
  for j in (modify_prot(chomp_prot(translate(transcribe(i))))):
    for k in orf(j):
      orfs.append(k)

#Write open reading frames to file
with open("open_reading_frames_output.txt",'w') as out_file:
  for i in set(orfs):
    out_file.write(i+"\n")
out_file.closed
