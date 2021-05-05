m = 0
m1 = 0

N = int(input())
for i in range(N):
    m += int(input())
    m1 += 1

ans = []

N = int(input())
for i in range(N):
    m += int(input())
    m1 += 1
    ans.append(m / m1)

for i in ans:
    print("{:.2f}".format(round(i, 3)))