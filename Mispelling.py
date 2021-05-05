for i in range(int(input())):
    inp = input().split()
    temp = list(" ".join(inp[1:]).lstrip().rstrip())
    temp[int(inp[0]) - 1] = ""

    print(str(i + 1) + " " + "".join(temp))