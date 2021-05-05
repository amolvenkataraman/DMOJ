N, W, H = [int(i) for i in input().split(" ")]
matches = [int(input()) for i in range(N)]
for i in matches:
    if i ** 2 <= W ** 2 + H ** 2:
        print("DA")
    else:
        print("NE")