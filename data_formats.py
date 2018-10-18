from sys import argv
from Bio import Entrez
from Bio import SeqIO
Entrez.email="mjcook@uw.edu"

with open(argv[1],'r') as in_file:
  in_data = in_file.read().split()
in_file.closed

id_string = ''

for i in in_data:
  id_string += str(i+", ")
id_string = id_string[:-2]

handle = Entrez.efetch(db="nucleotide", id=[id_string], rettype="fasta")

records = list(SeqIO.parse(handle, "fasta"))

shortest_record = records[0]

for i in records:
  if len(i.seq) < len(shortest_record.seq):
    shortest_record = i

with open("data_format.txt",'w') as out_file:
  out_file.write(shortest_record.format("fasta"))
out_file.closed
