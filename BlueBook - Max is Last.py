arr = []
for i in range(int(input())):
    arr.append(float(input()))

ans = []
for i in arr:
    if i != max(arr):
        ans.append(i)
ans.append(max(arr))

for i in ans:
    print("%.2f" %i)