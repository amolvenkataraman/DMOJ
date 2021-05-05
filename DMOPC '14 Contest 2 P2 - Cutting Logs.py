def cnt(arr):
    ans = 0
    for i in arr:
        if i != '':
            ans += 1
    return ans

N = int(input())

log = input().split("X")

c = cnt(log)
print(c)

for i in log:
    if i != '':
        print(i)