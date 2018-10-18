from sys import argv
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC

with open(argv[1], 'r') as in_file:
  in_data = in_file.read().splitlines()
in_file.closed

seq_list = []

seq = ''
i = 1
while (i < len(in_data)):
  if (in_data[i][0] == '>'):
    seq_list.append(seq)
    seq = ''
    i += 1
  else:
    seq += in_data[i]
    i += 1
seq_list.append(seq)

running_total = 0
for i in seq_list:
  my_seq = Seq(i, IUPAC.unambiguous_dna)
  re_seq = my_seq.reverse_complement()
  if (str(my_seq) == str(re_seq)):
    running_total += 1

print running_total
