from math import gcd

N = int(input())
D = int(input())

g = gcd(N, D)
N = int(N / g)
D = int(D / g)

ans = N // D
ans2 = N - (D * (ans))

if ans != 0:
    if ans2 == 0:
        print(ans)
    else:
        print(str(ans) + " " + str(ans2) + "/" + str(D))
else:
    print (str(ans2) + "/" + str(D))