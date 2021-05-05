vowels = [i for i in "aeiouy"]
consonants = [i for i in "bcdfghjklmnpqrstvwxyz"]

N, C, V = [int(i) for i in input().split(" ")]
word = input()

for i in range(N - C):
    temp = 0
    for a in word[i:i+C+1]:
        if a in consonants:
            temp += 1
    if temp > C:
        print("NO")
        raise SystemExit

for i in range(N - V):
    temp = 0
    for a in word[i:i+V+1]:
        if a in vowels:
            temp += 1
    if temp > V:
        print("NO")
        raise SystemExit

print("YES")
