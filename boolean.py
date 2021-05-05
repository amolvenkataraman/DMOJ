a = input().split(" ")

if (((len(a) - 1) % 2) == 0):
    print(a[-1])
else:
    if a[-1] == "True":
        print("False")
    else:
        print("True")