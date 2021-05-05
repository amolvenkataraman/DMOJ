T = int(input())
chores = []
for i in range(int(input())):
    chores.append(int(input()))

chores = sorted(chores)

ans = 0
ans1 = 0
for i in chores:
    if ans1 + i > T:
        print(ans)
        raise SystemExit
    else:
        ans += 1
        ans1 += i