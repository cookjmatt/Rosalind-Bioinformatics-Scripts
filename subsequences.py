from sys import argv

with open(argv[1],'r') as in_file:
  in_data = in_file.readlines()
in_file.closed

a = in_data[1].split()
for i in range(len(a)):
  a[i] = int(a[i])

##############################
#Longest Increasing Subsequence

A = [1]*len(a)
for i in range(len(a)):
  for j in range(i):
    if (A[j] + 1 > A[i] and a[j] < a[i]):
      A[i] += 1

m = A[0]
for i in range(len(A)):
  if (m < A[i]):
    m = A[i]

results = []
for i in range(len(A)-1, -1, -1):
  if (m == A[i]):
    results.append(a[i])
    m -= 1
results.reverse()
lis = ''
for i in results:
  lis += str(i)+" "

###############################
#Longest Decreasing Subsequence

A = [1]*len(a)
for i in range(len(a)):
  for j in range(i):
    if (A[j] >= A[i] and a[j] > a[i]):
      A[i] += 1

m = A[0]
for i in range(len(A)):
  if (m < A[i]):
    m = A[i]

results = []
for i in range(len(A)-1, -1, -1):
  if (m == A[i]):
    results.append(a[i])
    m -= 1
results.reverse()
lds = ''
for i in results:
  lds += str(i)+" "

with open("subsequences.txt",'w') as out_file:
  out_file.write(lis)
  out_file.write("\n")
  out_file.write(lds)
out_file.closed
