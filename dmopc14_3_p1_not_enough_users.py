n = int(input())
k = int(input())
d = int(input())

ans = n
for i in range(d):
    ans *= k

print(ans)