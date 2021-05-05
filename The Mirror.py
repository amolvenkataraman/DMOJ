import math

primes = []

def is_prime(n):
    global primes

    i = 0
    if n == 1:
        return False
    if n in primes:
        return True
    while primes[i] <= math.sqrt(n):
        i += 1
        if n % primes[i] == 0:
            return False
    primes.append(n)
    return True

for i in [2, 3, 5, 7]:
    primes.append(i)

ans = []
for i in range(int(input())):
    at = 0
    inp = [int(i) for i in input().split(" ")]
    if inp[0] % 2 == 0:
        inp[0] += 1
    for n in range(inp[0], inp[1], 2):
        if is_prime (n) == True:
            at += 1
    if inp[0] <= 2 and inp[1] >= 2:
        at += 1
    ans.append(at)

for i in ans:
    print(i)