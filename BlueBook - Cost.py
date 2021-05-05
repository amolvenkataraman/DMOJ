import math

def get_cost(N):
    if N <= 30:
        return 38
    elif N <= 50:
        return 55
    else:
        return 73 + (24 * math.ceil(((N - 100)) / 50))

inp = []
for i in range(int(input())):
    print(get_cost(int(input())))