m = int(input())
n = int(input())

ans = 0

for i in range(1, 10):
    j = 10 - i
    if m >= i and n >= j:
        ans += 1

if ans != 1:
    print(f"There are {ans} ways to get the sum 10.")
else:
    print=(f"There is {ans} way to get the sum 10.")
