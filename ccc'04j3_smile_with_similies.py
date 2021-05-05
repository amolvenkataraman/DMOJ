N = int(input())
M = int(input())

a = []
n = []

for i in range(N):
    a.append(input())

for i in range(M):
    n.append(input())

for i in a:
    for j in n:
        print(i + " as " + j)