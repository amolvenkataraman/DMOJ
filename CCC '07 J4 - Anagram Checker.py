a1 = list(input().replace(" ", ""))
a2 = list(input().replace(" ", ""))

anagram = True

if sorted(a1) == sorted(a2):
    print("Is an anagram.")
else:
    print("Is not an anagram.")