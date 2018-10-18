#!/usr/bin/env python
from sys import argv

def set_output(fset):
  s = []
  for i in fset:
    s.append(i)
  st = '{'
  for i in range(len(s) - 1):
    st += (str(s[i])+', ')
  st += str(s[len(s)-1])+'}'
  return st

with open(argv[1],'r') as in_file:
  in_data = in_file.read().splitlines()
in_file.closed

#Get input 'n' and two sets into proper variables
n = int(in_data[0])
fullset  = []
for i in range(1,n+1):
  fullset.append(i)
fullset = frozenset(fullset)
line1 = in_data[1][1:-1].split(',')
line2 = in_data[2][1:-1].split(',')
set1 = []
set2 = []
for i in line1:
  set1.append(int(i))
for i in line2:
  set2.append(int(i))
set1 = frozenset(set1)
set2 = frozenset(set2)

##########
# Results
##########

res = []

#Union of two sets
res.append(frozenset.union(set1,set2))
#Intersection of two sets
res.append(frozenset.intersection(set1,set2))
#Difference of sets 1 and 2
res.append(set1 - set2)
#Difference of sets 2 and 1
res.append(set2 - set1)
#Complement of set1
res.append(fullset - set1)
#Complement of set2
res.append(fullset - set2)

#Output
with open('intro_set_operations.txt','w') as out_file:
  for i in res:
    out_file.write(set_output(i)+'\n')
out_file.closed
