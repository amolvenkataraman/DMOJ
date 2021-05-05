for i in range(int(input())):
    temp = int(input())

    if temp <= 45 or temp >= 315:
        print("N")
    elif temp <= 135 and temp > 45:
        print("E")
    elif temp <= 225 and temp > 135:
        print("S")
    else:
        print("W")