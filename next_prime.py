import math

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n))):
        if n % i == 0:
            return False
    return True

n = int(input())
n1 = n

while(True):
    if is_prime(n1):
        print(n1)
        raise SystemExit
    n1 += 1