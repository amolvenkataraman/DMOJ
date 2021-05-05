n = int(input())
ans = 0
for i in range(n):
    temp = input().split(" ")
    if int(temp[1]) - int(temp[0]) > ans:
        ans = int(temp[1]) - int(temp[0])

print(ans)