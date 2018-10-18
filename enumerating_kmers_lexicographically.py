#!/usr/bin/env Python
from sys import argv
import itertools
import math
import sys

with open(argv[1],'r') as in_file:
  in_data = in_file.read().splitlines()
in_file.closed

n =int(in_data[1])

class ordered_alphabet:
  def __init__(self,letter,order):
    self.letter = letter
    self.order  = order

permute = []
order = 1
for i in in_data[0].split():
  permute.append(ordered_alphabet(i,order))
  order += 1

perms = (list(itertools.product(permute,repeat=n)))

for i in reversed(range(n)):
  sorted(perms[i], key=lambda ordered_alphabet: ordered_alphabet.order)

with open("enumerating_kmers_lexicographically_output.txt",'w') as out_file:
  for i in perms:
    for j in i:
      out_file.write(j.letter)
    out_file.write("\n")
out_file.closed
