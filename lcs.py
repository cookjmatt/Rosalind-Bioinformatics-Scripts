from sys import argv

with open(argv[1],'r') as in_file:
  in_data = in_file.read().splitlines()
in_file.closed

x = in_data[0]
y = in_data[1]
m = len(x)
n = len(y)

# 1 0 0 0 0 0 3       1 == [0][0]
# 0 0 0 0 0 0 0       2 == [5][0]
# 0 0 0 0 0 0 0       3 == [0][6]
# 0 0 0 0 0 0 0       4 == [5][6]
# 0 0 0 0 0 0 0
# 2 0 0 0 0 0 4

def lcs(x,y):
  m = len(x)
  n = len(y)
  c = [[0 for i in range(m)] for j in range(n)]
  for j in range(n):
    for i in range(m):
      if (i == 0):
        c[j][i] = j
      elif (j == 0):
        c[j][i] = i
      elif (x[i] == y[j]):
        c[j][i] = c[j-1][i-1]+1
      else:
        c[j][i] = min(c[j-1][i]+1,c[j][i-1]+1)
  return c

lcs_array = []
def backtrack(c,x,y,i,j):
  global lcs_array
  if (i == 0):
    lcs_array.append(x[i])
    return
  elif (j == 0):
    lcs_array.append(y[j])
    return
  elif (x[i] == y[j]):
    lcs_array.append(x[i])
    return backtrack(c,x,y,i-1,j-1)
  else:
    if (c[j][i-1] > c[j-1][i]):
      lcs_array.append(y[j])
      return backtrack(c,x,y,i-1,j)
    else:
      lcs_array.append(x[i])
      return backtrack(c,x,y,i,j-1)

c = lcs(x,y)
for i in c:
  print i
backtrack(lcs(x,y),x,y,m-1,n-1)
lcs_array.reverse()
s = ''
for i in lcs_array:
  s += i
print s
