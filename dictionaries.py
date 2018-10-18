#!/usr/bin/env python

from sys import argv

with open(argv[1],'r') as in_file:
  in_data = in_file.read()[:-1].split(' ')
in_file.closed

d = {}
for i in in_data:
  if i in d:
    d[i] = d[i] + 1
  else:
    d[i] = 1

with open('dictionaries.txt','w') as out_file:
  for i in d:
    out_file.write(str(str(i)+' '+str(d[i])+'\n'))
out_file.closed
