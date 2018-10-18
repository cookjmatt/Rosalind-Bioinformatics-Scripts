#!/usr/bin/env Python
from sys import argv
import sys
import numpy
import itertools

sys.setrecursionlimit(10000)

with open(argv[1],'r') as in_file:
  in_data = in_file.read().splitlines()
in_file.closed

switch_flag = 0
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
  b = numpy.zeros(shape=(n+1,m+1))
  for i in range(1,n+1):
    s[i][0] = i
  for j in range(1,m+1):
    s[0][j] = j
  for i in range(1,n+1):
    for j in range(1,m+1):
      if (v[i-1] == w[j-1]):
        s[i][j] = min(s[i-1][j]+1,s[i][j-1]+1,s[i-1][j-1])
      else:
        s[i][j] = min(s[i-1][j]+1,s[i][j-1]+1,s[i-1][j-1]+1)
      if (s[i][j] == s[i-1][j]+1):
        b[i][j] = 1
      elif (s[i][j] == s[i][j-1]+1):
        b[i][j] = 2
      else: # (s[i][j] == s[i-1][j-1]):
        b[i][j] = 3
  return (s[n][m],b,s)

aln = []

def PrintLCS(b,v,w,i,j):
  if (i == 0 or j == 0):
    if (i == 0 and j != 0):
      aln.append(('-',w[j-1]))
    elif (j == 0 and i != 0):
      aln.append((v[i-1],'-'))
    return
  if (b[i][j] == 3):
    PrintLCS(b,v,w,i-1,j-1)
    aln.append((v[i-1],w[j-1]))
  else:
    if (b[i][j] == 1):
      PrintLCS(b,v,w,i-1,j)
      aln.append((v[i-1],"-"))
    else:
      PrintLCS(b,v,w,i,j-1)
      aln.append(('-',w[j-1]))

PrintLCS(LCS(str1,str2)[1],str1,str2,len(str1),len(str2))

aln1 = []
aln2 = []
for i in aln:
  aln1.append(i[0])
  aln2.append(i[1])

def hamm(v,w):
  dist = 0
  for i,j in itertools.izip(v,w):
    if (i != j):
      dist += 1
  return dist

with open("edit_distance_alignment.txt",'w') as out_file:
  out_file.write(str(hamm(aln1,aln2))+"\n")
  if (switch_flag == 0):
    out_file.write("".join(aln1)+"\n")
    out_file.write("".join(aln2))
  else:
    out_file.write("".join(aln2)+"\n")
    out_file.write("".join(aln1))
out_file.closed
