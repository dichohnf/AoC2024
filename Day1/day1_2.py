import bisect
lines = open("../inputs/1.in").read().splitlines()

col0 = []
col1 = []
for line in lines:
  split = line.split()
  bisect.insort(col0, int(split[0]))
  bisect.insort(col1, int(split[1]))

result = 0
for i in range(len(col0)):
  result += col0[i] * col1.count(col0[i])

print(result)