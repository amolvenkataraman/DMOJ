n = int(input())
a = []
ans = 0
for i in range(n):
    temp = int(input())
    if temp not in a:
        ans += 1
        a.append(temp)

print(ans)