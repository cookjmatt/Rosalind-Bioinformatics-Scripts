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

def LCS(v,w):
  n = len(v)
  m = len(w)
  s = numpy.zeros(shape=(n+1,m+1))
  b = numpy.zeros(shape=(n+1,m+1))
  for i in range(1,n+1):
    for j in range(1,m+1):
      if (v[i-1] == w[j-1]):
        s[i][j] = max(s[i-1][j],s[i][j-1],s[i-1][j-1]+1)
      else:
        s[i][j] = max(s[i-1][j],s[i][j-1])
      if (s[i][j] == s[i-1][j]):
        b[i][j] = 1
      elif (s[i][j] == s[i][j-1]):
        b[i][j] = 2
      elif (s[i][j] == (s[i-1][j-1] + 1)):
        b[i][j] = 3
  return (s[n][m],b,s)

lc_string = []

def PrintLCS(b,v,i,j):
  if (i == 0 or j == 0):
    return
  if (b[i][j] == 3):
    PrintLCS(b,v,i-1,j-1)
    lc_string.append(v[i-1])
  else:
    if (b[i][j] == 1):
      PrintLCS(b,v,i-1,j)
    else:
      PrintLCS(b,v,i,j-1)

PrintLCS(LCS(str1,str2)[1],str1,len(str1),len(str2))
with open("finding_shared_spliced_motif.txt",'w') as out_file:
  out_file.write("".join(lc_string))
out_file.closed
