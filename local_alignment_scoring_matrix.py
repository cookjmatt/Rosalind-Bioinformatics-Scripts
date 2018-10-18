#!/usr/bin/env Python
from sys import argv
import sys
import numpy

#Import PAM250 matrix
with open('PAM250.txt','r') as P250_file:
  P250_data = P250_file.readlines()
P250_file.closed
PAM = []
for i in P250_data:
  vals = i.rstrip("\n").split()
  PAM.append(vals)
AA = {'A':0,'C':1,'D':2,'E':3,'F':4,'G':5,'H':6,'I':7,'K':8,'L':9,'M':10,
      'N':11,'P':12,'Q':13,'R':14,'S':15,'T':16,'V':17,'W':18,'Y':19}

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

def LocAln(v,w):
  n = len(v)
  m = len(w)
  s = numpy.zeros(shape=(n+1,m+1))
  b = numpy.zeros(shape=(n+1,m+1))
  for i in range(1,n+1):
    for j in range(1,m+1):
      s[i][j] = max(0,s[i-1][j]-5,s[i][j-1]-5,s[i-1][j-1]+numpy.float64(PAM[AA[v[i-1]]][AA[w[j-1]]]))
      if (s[i][j] == s[i-1][j]-5):
        b[i][j] = 1
      elif (s[i][j] == s[i][j-1]-5):
        b[i][j] = 2
      elif (s[i][j] == s[i-1][j-1]+numpy.float64(PAM[AA[v[i-1]]][AA[w[j-1]]])):
        b[i][j] = 3
  high = (0,0)
  for i in range(1,n+1):
    for j in range(1,m+1):
      if (s[i][j] > s[high[0]][high[1]]):
        high = (i,j)
  return (high,s,b)


loc1 = []
loc2 = []
def PrintLoc(v,w,b,s,i,j):
  if ((s[i][j] == 0) or (b[i][j] == 0) or (i == 0) or (j == 0)):
    return
  if (b[i][j] == 3):
    PrintLoc(v,w,b,s,i-1,j-1)
    loc1.append(v[i-1])
    loc2.append(w[j-1])
  else:
    if (b[i][j] == 1):
      PrintLoc(v,w,b,s,i-1,j)
      loc1.append(v[i-1])
      loc2.append("-")
    else:
      PrintLoc(v,w,b,s,i,j-1)
      loc2.append(w[j-1])
      loc1.append("-")

score = LocAln(str1,str2)
PrintLoc(str1,str2,score[2],score[1],score[0][0],score[0][1])
with open("local_alignment_scoring_matrix.txt",'w') as out_file:
  out_file.write(str(int(score[1][score[0][0]][score[0][1]]))+"\n")
  if (switch_flag == 0):
    out_file.write("".join(loc1)+"\n")
    out_file.write("".join(loc2))
  else:
    out_file.write("".join(loc2)+"\n")
    out_file.write("".join(loc1))
out_file.closed
