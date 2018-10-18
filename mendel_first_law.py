#!/usr/bin/env
from sys import argv

with open(argv[1],'r') as in_file:
  in_data = in_file.read().split()
in_file.closed

k = float(in_data[0])
m = float(in_data[1])
n = float(in_data[2])
tot = k + m + n

rec = 1 - ((n/tot)*((n-1)/(tot-1))+(n/tot)*(m/(tot-1))*0.5+(m/tot)*((m-1)/(tot-1))*0.25+(m/tot)*(n/(tot-1))*0.5)

with open('mendel_first_law.txt','w') as out_file:
  out_file.write('{:.5}'.format(rec))
out_file.closed
