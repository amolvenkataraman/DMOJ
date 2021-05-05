def printarr(arr):
    for i in arr[:-1]:
        print(str(i) + " ", end="")
    print(arr[-1])

N = int(input())
inp = input().split(" ")
arr = [int(i) for i in inp]

printarr(arr)

while(True):
    s = False
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            temp = arr[i]
            arr[i] = arr[i + 1]
            arr[i + 1] = temp
            s = True
            printarr(arr)

    if s == False:
        raise SystemExit