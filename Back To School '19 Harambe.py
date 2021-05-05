n = int(input())
words = input().split(" ")
word = input()

words1 = [i for i in words if len(i) <= len(word)]

words1 = sorted(words1, key=lambda words1 : len(words1), reverse=True)

print(words1[0])