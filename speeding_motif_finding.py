from sys import argv

with open(argv[1],'r') as in_file:
  in_data = in_file.readlines()
in_file.closed

v = in_data[0].strip()

def kmpPreprocess(p):
  m = len(p)
  b = []
  for i in range(m+1):
    b.append(0)
  i = 0
  j = -1
  b[i] = j
  while (i < m):
    while (j>=0 and p[i]!=p[j]):
      j=b[j]
    i += 1
    j += 1
    b[i]=j
  return b

fail_array = kmpPreprocess(v)

with open('speeding_motif_finding.txt','w') as out_file:
  for i in range(1,len(fail_array)):
    out_file.write(str(fail_array[i])+" ")
out_file.closed
