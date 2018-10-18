#!/usr/bin/env Python
from sys import argv
import sys
import numpy

sys.setrecursionlimit(10000)

with open(argv[1],'r') as in_file:
  in_data = in_file.read().splitlines()
in_file.closed

if (len(in_data[0]) > len(in_data[1])):
  str1 = in_data[0]
  str2 = in_data[1]
else:
  str1 = in_data[1]
  str2 = in_data[0]

def ED(v,w):
  n = len(v)
  m = len(w)
  d = numpy.zeros(shape=(n+1,m+1))
  for i in range(1,n+1):
    d[i][0] = i
  for j in range(1,m+1):
    d[0][j] = j
  for i in range(1,n+1):
    for j in range(1,m+1):
      if (v[i-1] == w[j-1]):
        d[i][j] = min(d[i-1][j]+1,d[i][j-1]+1,d[i-1][j-1])
      else:
        d[i][j] = min(d[i-1][j]+1,d[i][j-1]+1,d[i-1][j-1]+1)
  return (d[n][m],d)

with open("edit_distance.txt",'w') as out_file:
  out_file.write(str(int(ED(str1,str2)[0])))
out_file.closed
