N = int(input())

ans = []
for i in range(N):
    temp = input().split(" ")
    a = 0
    for i in temp:
        if i[0].isupper():
            a += 1
    ans.append(a)

for i in ans:
    print(i)