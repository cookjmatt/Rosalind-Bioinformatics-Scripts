from sys import argv

n = int(argv[1])
m = int(argv[2])

gen = []
for i in range(n):
  gen.append(1)
for i in range(0,m):
  if not(i == 0 or i == 1):
    gen[i] = gen[i-1]+gen[i-2]
for i in range(m,n):
  gen[i] = gen[i-1]+gen[i-2]-gen[i-m-1]
print gen
