dim = input().split(" ")
l = int(dim[0])
w = int(dim[1])
t = int(input())

ans = int((l // t) * (w // t))

print(ans)