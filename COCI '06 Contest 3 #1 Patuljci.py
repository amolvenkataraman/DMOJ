from itertools import permutations

d = [int(input()) for i in range(9)]

for i in permutations(d, 7):
    if sum(i) == 100:
        print(*i, sep=" ")
        raise SystemExit