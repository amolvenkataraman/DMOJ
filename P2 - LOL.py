units = []

for i in range(int(input())):
    units.append([int(i) for i in input().split(" ")])

u1 = sorted(units, key=lambda units: units[0])
u2 = sorted(units, key=lambda units: units[1])

ans = (u1[-1][0] - u1[0][0]) * (u2[-1][1] - u2[0][1])

print(ans)