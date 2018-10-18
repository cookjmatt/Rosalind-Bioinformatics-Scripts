#!/usr/bin/env Python
from sys import argv
from collections import Counter

with open(argv[1],'r') as in_file:
  in_data = in_file.read()
in_file.closed

nuc_cnt = Counter()
for nuc in in_data:
  nuc_cnt[nuc] += 1
print nuc_cnt['A'], nuc_cnt['C'], nuc_cnt['G'], nuc_cnt['T']
