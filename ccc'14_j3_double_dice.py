N = int(input())

a = 100
d = 100

for i in range(N):
    temp = [int(i) for i in input().split(" ")]

    if temp[0] > temp[1]:
        d -= temp[0]
    elif temp[0] < temp[1]:
        a -= temp[1]

print(a)
print(d)