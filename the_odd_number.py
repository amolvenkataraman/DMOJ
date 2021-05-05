a = {}

for i in range(int(input())):
    temp = int(input())
    try:
        a[temp] += 1
        if a[temp] % 2 == 0:
            a.pop(temp, None)
    except KeyError:
        a[temp] = 1

for i in a:
    if a[i] % 2 == 1:
        print(i)
        raise SystemExit