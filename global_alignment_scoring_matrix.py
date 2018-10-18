#!/usr/bin/env Python
from sys import argv
import sys
import numpy

#Import BLOSUM62 matrix
with open('BLOSUM62.txt','r') as B62_file:
  B62_data = B62_file.readlines()
B62_file.closed
BLOSUM = []
for i in B62_data:
  vals = i.rstrip("\n").split()
  BLOSUM.append(vals)
AA = {'A':0,'C':1,'D':2,'E':3,'F':4,'G':5,'H':6,'I':7,'K':8,'L':9,'M':10,
      'N':11,'P':12,'Q':13,'R':14,'S':15,'T':16,'V':17,'W':18,'Y':19}

with open(argv[1],'r') as in_file:
  in_data = in_file.read().splitlines()
in_file.closed

if (len(in_data[0]) >= len(in_data[1])):
  str1 = in_data[0]
  str2 = in_data[1]
else:
  switch_flag = 1
  str1 = in_data[1]
  str2 = in_data[0]

def LCS(v,w):
  n = len(v)
  m = len(w)
  s = numpy.zeros(shape=(n+1,m+1))
  for i in range(0,n+1):
    s[i,0] = -5*i
  for j in range(0,m+1):
    s[0,j] = -5*j
  for i in range(1,n+1):
    for j in range(1,m+1):
      s[i][j] = max(s[i-1][j]-5,s[i][j-1]-5,s[i-1][j-1]+numpy.float64(BLOSUM[AA[v[i-1]]][AA[w[j-1]]]))
  return (s[n][m],s)

score = LCS(str1,str2)

with open("global_alignment_scoring_matrix.txt",'w') as out_file:
  out_file.write(str(int(score[0])))
out_file.closed
