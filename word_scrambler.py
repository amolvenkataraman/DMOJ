from itertools import permutations

a = sorted([c for c in input()])

l = list(permutations(a))

for i in l:
    for j in i:
        print(j, end="")
    print()