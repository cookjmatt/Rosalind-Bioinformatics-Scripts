#!/usr/bin/env Python
from sys import argv
import sys

#Open file and get data
with open (argv[1],'r') as in_file:
  in_data = in_file.read().splitlines()
in_file.closed

#Determine the shortest string and break it up into
# all possible substrings. These will be used to
# determine the greatest common substring
in_data.sort(key = len)
shortest = in_data[0]
strings = []
for i in range(len(shortest)):
  for j in reversed(range(len(shortest))):
    sub_string = ""
    for k in range(j-i+1):
      sub_string += shortest[k+i]
    if (sub_string != ""):
      strings.append(sub_string)
strings.sort(key = len)
strings.reverse()

#Determine the longest common substring
correct = 1
for i in strings:
  if (correct == 1):
    in_all = 1
  for j in in_data:
    if (j.find(i) == -1):
      in_all = 0
  if (in_all == 1):
    shortest_common_substring = i
    correct = 0
    in_all = 0

#Write longest common substring to file
with open("finding_shared_motif_output.txt",'w') as out_file:
  out_file.write(shortest_common_substring)
out_file.closed
