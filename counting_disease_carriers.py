#!/usr/bin/env python
from sys import argv
from math import *
from decimal import *

A = []
with open(argv[1],'r') as in_file:
  [A.append(float(i)) for i in in_file.read().split()]
in_file.closed

with open ('counting_disease_carriers.txt','w') as out_file:
  for i in A:
    q = sqrt(i)
    p = 1.0 - q
    out_file.write(str(str(round(Decimal(2.0*p*q+i),3))+' '))
out_file.closed
