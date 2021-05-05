n = int(input())
o = 0
while True:
    if n == 1:
        print(o)
        raise SystemExit

    o += 1
    if n % 2 == 0:
        n /= 2
    else:
        n *= 3
        n += 1