n = int(input())
s = []
for i in range(n):
    s.append(input())

ans = 'N'

for i in range(len(s)):
    if s[i] == "Bessarion":
        try:
            if (s[i-1] == "Leslie" and s[i+1] == 'Bayview') or (s[i+1] == "Leslie" and s[i-1] == 'Bayview'):
                ans = 'Y'
        except IndexError:
            ans = 'N'

print(ans)