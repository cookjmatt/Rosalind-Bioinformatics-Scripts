#!/usr/bin/env Python
from sys import argv

with open(argv[1],'r') as in_file:
  in_data = in_file.read().splitlines()
in_file.closed

len_seqs = len(in_data[0])
num_seqs = len(in_data)

profile_A = []
profile_C = []
profile_G = []
profile_T = []
consensus_seq = ""

for i in range(len_seqs):
  num_A = 0
  num_C = 0
  num_G = 0
  num_T = 0
  for j in range(num_seqs):
    if in_data[j][i] == 'A':
      num_A += 1
    elif in_data[j][i] == 'C':
      num_C += 1
    elif in_data[j][i] == 'G':
      num_G += 1
    elif in_data[j][i] == 'T':
      num_T += 1
  profile_A.append(num_A)
  profile_C.append(num_C)
  profile_G.append(num_G)
  profile_T.append(num_T)
  num_set = [num_A,num_C,num_G,num_T]
  if (num_A == max(num_set)):
    consensus_seq += 'A'
  elif (num_C == max(num_set)):
    consensus_seq += 'C'
  elif (num_G == max(num_set)):
    consensus_seq += 'G'
  elif (num_T == max(num_set)):
    consensus_seq += 'T'

with open("consensus_profile_output.txt",'w') as out_file:
  out_file.write(consensus_seq+"\n")
  out_file.write("A: ")
  for i in range(len_seqs):
    out_file.write(str(profile_A[i]))
    if (i < len_seqs - 1):
      out_file.write(" ")
  out_file.write("\n")
  out_file.write("C: ")
  for i in range(len_seqs):
    out_file.write(str(profile_C[i]))
    if (i < len_seqs - 1):
      out_file.write(" ")
  out_file.write("\n")
  out_file.write("G: ")
  for i in range(len_seqs):
    out_file.write(str(profile_G[i]))
    if (i < len_seqs - 1):
      out_file.write(" ")
  out_file.write("\n")
  out_file.write("T: ")
  for i in range(len_seqs):
    out_file.write(str(profile_T[i]))
    if (i < len_seqs - 1):
      out_file.write(" ")
out_file.closed
