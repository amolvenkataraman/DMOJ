K = int(input())

n = []

for i in range(K):
    temp = int(input())
    if temp == 0:
        n.pop()
    else:
        n.append(temp)

print(sum(n))