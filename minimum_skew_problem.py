#!/usr/bin/env python

from sys import argv

with open(argv[1],'r') as in_file:
  in_data = in_file.read().split()
in_file.closed

s = in_data[0]
G = 0
C = 0
i = 0
skew_list = [0]
mn = 0
for i in range(0,len(s)):
  if s[i] == 'G':
    G += 1
  elif s[i] == 'C':
    C += 1
  skew_list.append(G-C)
  if (G-C) < mn:
    mn = (G-C)

ans = ''
for i in range(0,len(skew_list)):
  if skew_list[i] < (mn+1) :
    ans += str(str(i)+' ')

with open('minimum_skew_problem_output.txt','w') as out_file:
  out_file.write(ans[:-1])
out_file.closed
