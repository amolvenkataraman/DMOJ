ans = 0
b = int(input())
if b == 1:
    ans += 461
elif b == 2:
    ans += 431
elif b == 3:
    ans += 420

s = int(input())
if s == 1:
    ans += 100
elif s == 2:
    ans += 57
elif s == 3:
    ans += 70

d = int(input())
if d == 1:
    ans += 130
elif d == 2:
    ans += 160
elif d == 3:
    ans += 118

de = int(input())
if de == 1:
    ans += 167
elif de == 2:
    ans += 266
elif de == 3:
    ans += 75

print("Your total Calorie count is " + str(ans) + ".")