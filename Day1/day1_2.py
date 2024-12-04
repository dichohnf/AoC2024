import bisect
lines = open("../inputs/1.in").read().splitlines()

col0, col1 = [], []
[bisect.insort(col0, int(split[0])) or bisect.insort(col1, int(split[1])) for split in (line.split() for line in lines)]

print(sum(col0[i] * col1.count(col0[i]) for i in range(len(col0))))