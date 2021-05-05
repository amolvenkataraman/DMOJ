for i in range(int(input())):
    inp = sorted([int(i) for i in input().split(" ")])
    if (inp[0] ** 2) + (inp[1] ** 2) == (inp[2] ** 2):
        print("R")
    elif (inp[0] ** 2) + (inp[1] ** 2) >= (inp[2] ** 2):
        print("A")
    else:
        print("O")

    #print(inp)