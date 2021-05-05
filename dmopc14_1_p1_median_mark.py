import math
import statistics

n = int(input())

m = []

for i in range(n):
    m.append(int(input()))

m.sort()

print(int(math.floor(statistics.median(m) + 0.5)))
