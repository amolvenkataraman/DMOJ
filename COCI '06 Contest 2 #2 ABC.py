nums = sorted([int(i) for i in input().split(" ")])
temp = input()
lets = [temp[0], temp[1], temp[2]]
ans = []
for i in lets:
    if i == "A":
        ans.append(nums[0])
    if i == "B":
        ans.append(nums[1])
    if i == "C":
        ans.append(nums[2])
print(*ans, sep=" ")