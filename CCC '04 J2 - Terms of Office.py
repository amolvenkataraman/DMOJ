import math

X = int(input())
Y = int(input())

for i in range(X - 1, Y, math.lcm(4, 2, 3, 5)):
    print("All positions change in year " + str(i + 1))