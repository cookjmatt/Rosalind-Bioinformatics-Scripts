from sys import argv

#Info for a DNA sequence (name, seq, first and last three nucleotides)
class DNAseq:
  def __init__(self, name, sequence, first, last):
    self.name       = name
    self.sequence   = sequence
    self.first      = first
    self.last       = last

#Open input file and read lines, chomping closing newline character
with open(argv[1],'r') as in_file:
  in_data = in_file.read().splitlines()
in_file.closed

#Create a DNAseq object for each fasta sequence (name and seq),
#  saving the first and last three nucleotides, and add to a list.
seq_list = []
i = 0
while (i < len(in_data)):
  name = in_data[i]
  i += 1
  seq = ""
  while ((i < len(in_data)) and (in_data[i][0] != '>')):
    seq += in_data[i]
    i += 1
  x = DNAseq(name[1:],seq,seq[0:3],seq[-3:])
  seq_list.append(x)

with open("overlap_graph_output.txt",'w') as out_file:
  for i in seq_list:
    for j in seq_list:
      if not(i.name == j.name):
        if (i.last == j.first):
          out_file.write(i.name+" "+j.name)
          out_file.write("\n")
out_file.closed
