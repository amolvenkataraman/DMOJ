ans = []

for i in range(int(input())):
    temp = input().split(" ")
    ans.append("")
    for i in temp:
        if len(i) == 4:
            ans[-1] += "****" + " "
            ans[-1] += " "
        else:
            ans[-1] += i + " "
            ans[-1] += " "
        ans[-1] = ans[-1][:-1]
            

for i in ans:
    print(i)