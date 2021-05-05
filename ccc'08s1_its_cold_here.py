t = []

while True:
    temp = input().split(" ")
    t.append([temp[0], int(temp[1])])
    if temp[0] == "Waterloo":
        break

t = sorted(t, key=lambda t: t[1])

print(t[0][0])