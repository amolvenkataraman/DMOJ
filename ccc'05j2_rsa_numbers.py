def rsa(n):
    ans = 0
    for i in range(1, n + 1):
        if n % i == 0:
            ans += 1
        if ans > 4:
            return False
    if ans == 4:
        return True
    return False

m = int(input())
m1 = int(input())

ans = 0
for i in range(m, m1 + 1):
    if rsa(i):
        ans += 1

print("The number of RSA numbers between " + str(m) + " and " + str(m1) + " is " + str(ans))