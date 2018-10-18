#!/usr/bin/env python
from sys import argv

with open (argv[1],'r') as in_file:
  in_data = in_file.readlines()
in_file.closed

lines = []
i = 0
while (i < len(in_data)):
  lines.append((in_data[i].strip().split(),in_data[i+1].strip().split()))
  i += 3

def reverse(w,i,j):
  v = w[:]
  v[i:j+1] = reversed(v[i:j+1])
  return v

def all_permutations(v):
  perms = []
  for i in range(len(v)):
    for j in range(i+1,len(v)):
      perms.append(reverse(v,i,j))
  return perms

matches = []
for pair in lines:
  print
  v = pair[0]
  w = pair[1]
  check_list = []
  check_list.append(v)
  match_found = 0
  distance = 0
  while (match_found == 0):
    check_list_2 = []
    print len(check_list)
    for i in check_list:
      if (i == w):
        match_found = 1
        matches.append(distance)
        break
    if (match_found == 0):
      distance += 1
      print distance
      for i in check_list:
        temp_perms = all_permutations(i)
        for j in temp_perms:
          check_list_2.append(j)
      check_list = check_list_2
    print
