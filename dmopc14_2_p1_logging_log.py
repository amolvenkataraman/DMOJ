d = int(input())
ans = {}
for i in range(d):
    ans[i] = 0
    t = int(input())
    for j in range(t):
        ans[i] += int(input())

for i in range(1, d + 1):
    if ans[i - 1] > 0:
        print("Day " + str(i) + ": " + str(ans[i - 1]))
    else:
        print("Weekend")