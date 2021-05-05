import math

N, Q = [int(i) for i in input().split(" ")]
A = [int(i) for i in input().split(" ")]
for i in range(Q):
    op = [int(i) for i in input().split(" ")]
    if op[0] == 1:
        A[A.index(op[1])] = 0
        A.append(math.floor(op[1] / 2))
        A.append(math.ceil(op[1] / 2))

    else:
        #print(A)
        print(A.count(op[1]))