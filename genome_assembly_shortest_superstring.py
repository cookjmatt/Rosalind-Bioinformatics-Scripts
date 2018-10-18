#!/usr/bin/env python
from sys import argv

#Open file and get data
with open(argv[1],'r') as in_file:
  in_data = in_file.read().splitlines()
in_file.closed

#Make list of words
words = []
for i in in_data:
  words.append(i)

def overlap(v,w):
  max_overlap = 0
  overlap_type = ''
  merged = ''
  for i in xrange(1,1+min(len(v),len(w))):
    v_suffix = v[-i:]
    v_prefix = v[:i]
    w_suffix = w[-i:]
    w_prefix = w[:i]
    if (v_prefix == w_suffix):
      max_overlap = i
      overlap_type = 'prefix'
    if (w_prefix == v_suffix):
      max_overlap = i
      overlap_type = 'suffix'
  if (overlap_type == 'prefix'):
    merged = w + v[max_overlap:]
  if (overlap_type == 'suffix'):
    merged = v + w[max_overlap:]
  return (max_overlap,merged)

while(len(words) > 1):
  index = 0
  max_overlap = 0
  best_merge = ''
  for i in xrange(1,len(words)):
    merge = overlap(words[0],words[i])
    if (merge[0] > max_overlap):
      index = i
      best_merge = merge[1]
      max_overlap = merge[0]
  words.pop(index)
  words.pop(0)
  words.append(best_merge)

with open('genome_assembly_shortest_superstring.txt','w') as out_file:
  out_file.write(words[0])
out_file.closed
