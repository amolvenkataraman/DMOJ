def red(num, lim):
    num -= lim
    if num < 0:
        num = 0
    return num

d = int(input())
e = int(input())
w = int(input())

a = (red(d, 100) * 0.25) + (e * 0.15) + (w * 0.20)
b = (red(d, 250) * 0.45) + (e * 0.35) + (w * 0.25)

print("Plan A costs " + str(round(a, 2)))
print("Plan B costs " + str(round(b, 2)))

if a < b:
    print("Plan A is cheapest.")
elif b < a:
    print("Plan B is cheapest.")
else:
    print("Plan A and B are the same price.")