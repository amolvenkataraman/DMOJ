import math

n = int(input())

while True:
    temp = math.sqrt(n)
    if math.floor(temp) == math.ceil(temp):
        print("The largest square has side length " + str(int(temp)) + ".")
        raise SystemExit
    else:
        n -= 1