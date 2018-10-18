from sys import argv
from sys import setrecursionlimit

######################################################
# Will not use these fxns now because the run-time
#   is much too high for this case

def LCS(x, y):
  #Compute LCS and compute and reuturn c table
  m = len(x)
  n = len(y)
  c = [[0 for i in xrange(m)] for i in xrange(n)]
  for i in range(1,m):
    for j in range(1,n):
      if (x[i] == y[j]):
        c[i][j] = c[i-1][i-1]+1
      else:
        c[i][j] = max(c[i][j-1],c[i-1][j])
  return c

LCS_array = []
def LCS_backtrack(c, x, y, i, j):
  global LCS_array
  if (i == 0):
    LCS_array.apend(x[i])
  elif (j == 0):
    LCS_array.append(y[j]) 
  elif (x[i] == y[j]):
    LCS_array.append(x[i])
    return LCS_backtrack(c, x, y, i-1, j-1)
  else:
    if (c[i][j-1] > c[i-1][j]):
      return LCS_backtrack(c,x,y,i,j-1)
    else:
      return LCS_backtrack(c,x,y,i-1,j)

######################################################

with open(argv[1],'r') as in_file:
  in_data = in_file.read().splitlines()
in_file.closed

ary = in_data[1].split()
rev_ary = []
for i in range(len(ary)):
  ary[i] = int(ary[i])
  rev_ary.append(ary[i])
rev_ary.reverse()

#Finding the longest increasing subsequence
def long_inc_subsequence(a):
  max_length = 1
  m = 0
  A = [0]*len(a)
  for i in range(len(a)):
    A[i] = 1
    for j in range(i-1,-1,-1):
      if ((a[j] < a[i]) and (A[j] + 1 > A[i])):
        A[i] = 1 + A[j]
    if (A[i] > m):
      max_length = A[i]
      m = i

  inc_subseq = []
  inc_subseq.append(a[m])
  while (A[m] > 1):
    i = m - 1
    while not((a[i] < a[m]) and (A[i] == A[m] -1)):
      i = i - 1
    m = i
    inc_subseq.append(a[m])
  inc_subseq.reverse()
  return inc_subseq  
 
lis = ''
lis_ary = long_inc_subsequence(ary)
for i in lis_ary:
  lis += str(i)+" "  

lds = ''
lds_ary = long_inc_subsequence(rev_ary)
lds_ary.reverse()
for i in lds_ary:
  lds += str(i)+" "

with open("longest_increasing_subsequence.txt",'w') as out_file:
  out_file.write(lis)
  out_file.write("\n")
  out_file.write(lds)
out_file.closed
