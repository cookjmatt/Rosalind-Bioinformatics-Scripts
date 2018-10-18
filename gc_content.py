#!/usr/bin/env Python
from sys import argv
import decimal

#Info for a DNA sequence (name, seq, GC%)
class DNAseq:
  def __init__(self, name, sequence, gc_content):
    self.name       = name
    self.sequence   = sequence
    self.gc_content = gc_content

#Returns the GC-content in percent for a DNA sequence
def get_gc(sequence):
  gc = 0
  for nucleotide in sequence:
    if ((nucleotide == 'G') or (nucleotide == 'C')):
      gc += 1
  return (round((decimal.Decimal(gc) / decimal.Decimal(len(sequence))) * 100,2))

#Open input file and read lines, chomping closing newline character
with open(argv[1],'r') as in_file:
  in_data = in_file.read().splitlines()
in_file.closed

#Create a DNAseq object for each two successive lines (name and seq),
# calculating the GC content for the sequence in the process, and add to a list.
seq_list = []
i = 0
while (i < len(in_data)):
  name = in_data[i]
  i += 1
  seq = ""
  while ((i < len(in_data)) and (in_data[i][0] != '>')):
    seq += in_data[i]
    i += 1
  x = DNAseq(name[1:],seq,get_gc(seq))
  seq_list.append(x)

#Sort list in descending order by GC content
seq_list.sort(key = lambda x: x.gc_content, reverse = True)

#Write name and GC content of sequence with highest GC% to file
with open("gc_content_output.txt",'w') as out_file:
  out_file.write(seq_list[0].name+"\n")
  out_file.write(str(seq_list[0].gc_content)+"%")
out_file.closed
