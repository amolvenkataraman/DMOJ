T = int(input())
S = int(input())
H = int(input())

for i in range(T - 1):
    print("*" + " " * S + "*" + " " * S + "*")
print("*" * (S + S + 3))
for i in range(H):
    print(" " * (S + 1) + "*")
