ans = []

for i in range(int(input())):
    N = int(input())
    train = [int(i) for i in input().split(" ")]
    swaps = 0
    for k in range(len(train)):
        for j in range(len(train) - 1):
            if train[j] > train[j + 1]:
                swaps += 1
                temp = train[j]
                train[j] = train[j + 1]
                train[j + 1] = temp

    ans.append(swaps)

for i in ans:
    print("Optimal train swapping takes " + str(i) + " swaps.")