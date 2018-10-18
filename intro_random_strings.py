#!/usr/bin/env
from sys import argv
import math

def GC_num(s):
  gc = 0.0
  for i in s:
    if ((i == 'G') or (i == 'C')):
      gc += 1.0
  return gc

def seq_prob(s, gc):
  prob = ((gc/2)**GC_num(s))*(((1-gc)/2)**(len(s)-GC_num(s)))
  return math.log(prob,10)

with open(argv[1],'r') as in_file:
  in_data = in_file.read().splitlines()
in_file.closed

A = in_data[1].split()

with open('intro_random_strings.txt','w') as out_file:
  for i in A:
    out_file.write(str("%0.3f " % seq_prob(in_data[0],float(i))))
out_file.closed
