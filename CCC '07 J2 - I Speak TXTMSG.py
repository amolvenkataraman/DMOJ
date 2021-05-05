t = {"CU": "see you", ":-)": "I'm happy", ":-(": "I'm unhappy", ";-)": "wink", ":-P": "stick out my tongue", "(~.~)": "sleepy", "TA": "totally awesome", "CCC": "Canadian Computing Competition", "CUZ": "because", "TY": "thank-you", "YW": "you're welcome", "TTYL": "talk to you later"}

ans = []

while True:
    temp = input()
    tr = False
    for i in t:
        if i == temp:
            ans.append(t[i])
            tr = True

    if tr == False:
        ans.append(temp)

    if temp == "TTYL":
        break

for i in ans:
    print(i)