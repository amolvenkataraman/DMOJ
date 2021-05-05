N = int(input())

ans = []
for i in [25, 10, 5, 1]:
    ans.append(N // i)
    N -= i * (N // i)

ans1 = f"{N} cents requires "
if ans[0] > 0:
    ans += f"{ans[0]} quarters"
if ans[1] > 0:
    ans += f",{ans[0]} quarters, "
if ans[2] > 0:
    ans += f"{ans[0]} quarters, "
if ans[3] > 0:
    ans += f"{ans[0]} quarters, "
