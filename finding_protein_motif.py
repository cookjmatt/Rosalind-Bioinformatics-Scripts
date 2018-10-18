#!/usr/bin/env python
from sys import argv
import urllib2

def find_site(s):
  sites = []
  for i in range(0,len(s)-3):
    if ((s[i] == 'N') and (s[i+1] != 'P') and ((s[i+2] == 'S') or (s[i+2] == 'T')) and (s[i+3] != 'P')):
      sites.append(str(i+1))
  return sites

def fasta_to_string(f):
  s = ''
  for i in range(1,len(f)):
    s += f[i].strip('\n')
  return s

with open(argv[1],'r') as in_file:
  in_data = in_file.readlines()
in_file.closed

#Turn list of codes into UNIPROT URL's
urls = []
for i in range(len(in_data)):
  urls.append(str('http://www.uniprot.org/uniprot/'+in_data[i].rstrip('\n')+'.fasta'))

#Get fastas from UNIPROT and find sites
sites = []
for i in urls:
  sites.append(find_site(fasta_to_string(urllib2.urlopen(i).readlines())))

#Write to file
with open('finding_protein_motif.txt','w') as out_file:
  for i in range(len(sites)):
    if (len(sites[i]) != 0):
      out_file.write(in_data[i])
      for j in sites[i]:
        out_file.write(str(j+' '))
      out_file.write('\n')
out_file.closed
