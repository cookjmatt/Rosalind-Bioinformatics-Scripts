from sys import argv

n = int(argv[1])
m = int(argv[2])

ary = [1]*n
for i in range(2,n):
  if i < m:
    ary[i] = ary[i-1]+ary[i-2]
  else:
    ary[i] = ary[i-1]+ary[i-2]-ary[i-m-1]
print ary[n-1]
