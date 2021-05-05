temp = input().split(" ")
n = int(temp[0])
k = int(temp[1])

c = []
for i in range(n):
    temp = input().split(" ")
    c.append([int(temp[0]), int(temp[1])])

c1 = sorted(c, key=lambda c: c[0], reverse = True)

ans = 0
for i in c1:
    if k > 0:
        ans += i[1]
        k -= 1
    else:
        ans += i[0]

print(ans)