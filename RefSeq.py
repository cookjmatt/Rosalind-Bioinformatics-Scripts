from sys import argv
from Bio import Entrez

Entrez.email = "mjcook@uw.edu"

with open(argv[1],'r') as in_file:
  in_data = in_file.read().splitlines()
in_file.closed

organism = str("\""+in_data[0]+"\"")
len1 = str("\""+in_data[1]+"\"")
len2 = str("\""+in_data[2]+"\"")
date = str("\""+in_data[3]+"\"")

search_string = str(organism+"[Organism] AND srcdb_refseq[PROP] AND \"1986/1/1\"[PDAT]:"+date+"[PDAT] AND "+len1+"[SLEN]:"+len2+"[SLEN]")

handle = Entrez.esearch(db="nucleotide", term=search_string)

record = Entrez.read(handle)

with open("RefSeq.txt",'w') as out_file:
  out_file.write(record["Count"])
out_file.closed
