icon = [
    "*x*",
    " xx",
    "* *"
]

k = int(input())

for i in icon:
    for _ in range(k):
        for a in i:
            print(a * k, end="")
        print()
