from sys import argv

with open(argv[1],'r') as in_file:
  in_data = in_file.read().splitlines()
in_file.closed

def lcs(x,y):
  n = len(x)
  m = len(y)
  c = [[0 for i in xrange(m)] for i in xrange(n)]
  for i in range(n):
    for j in range(m):
      if (i == 0):
        c[i][j] = j
      elif (j == 0):
        c[i][j] = i
      elif (i == j):
        c[i][j] = c[i-1][j-1]+1
      else:
        c[i][j] = min(c[i][j-1],c[i-1][j])+1
  return c

lcs_array = []
def lcs_backtrack(c, x, y, i, j):
  global lcs_backtrack
  if (i == 0):
    lcs_array.append(y[j])
  elif (j == 0):
    lcs_array.append(x[i])
  elif (x[i] == y[j]):
    lcs_array.append(x[i])
    return lcs_backtrack(c, x, y, i-1, j-1)
  else:
    if (c[i][j-1] > c[i-1][j]):
      lcs_array.append(x[i])
      return lcs_backtrack(c, x, y, i-1, j)
    else:
      lcs_array.append(y[j])
      return lcs_backtrack(c, x, y, i, j-1)

c = lcs(in_data[0],in_data[1])
for i in c:
  print i

#lcs_backtrack(lcs(in_data[0],in_data[1]),in_data[0],in_data[1],len(in_data[0])-1, len(in_data[1])-1)
#lcs_array.reverse()
#scss = ''
#for i in lcs_array:
#  scss += i
#print scss
