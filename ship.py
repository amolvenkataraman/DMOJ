r = ['B', 'F', 'T', 'L', 'C']

a = input()

ok = True
for i in r:
    if i not in a:
        ok = False
        print(i, end="")

if ok == True:
    print("NO MISSING PARTS", end="")

print("")