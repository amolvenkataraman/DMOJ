import numpy

N = int(input())
c = []
c1 = []
for i in range(N):
    c.append(input())
for i in range(N - 1):
    c1.append(input())

print(numpy.intersect1d(c, c1)[0])