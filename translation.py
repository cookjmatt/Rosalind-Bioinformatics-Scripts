from sys import argv
from Bio.Seq import translate
from Bio.Seq import transcribe

with open(argv[1], 'r') as in_file:
  in_data = in_file.read().splitlines()
in_file.closed

dna = in_data[0]
protein = in_data[1]
rna = transcribe(dna)

for i in range(1,15):
  if not (i == 7 or i == 8):
    if (protein == translate(rna,table=i, stop_symbol='', to_stop=False)):
      print i
