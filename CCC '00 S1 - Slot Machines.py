def broke(money, turns):
    if money <= 0:
        print(f"Martha plays {turns} times before going broke.")
        raise SystemExit

n = int(input())
c1 = int(input())
c2 = int(input())
c3 = int(input())

turns = 0

while True:
    n -= 1
    turns += 1
    c1 += 1
    if c1 == 35:
        n += 30
        c1 = 0
    broke(n, turns)
    
    n -= 1
    turns += 1
    c2 += 1
    if c2 == 100:
        n += 60
        c2 = 0
    broke(n, turns)
    
    n -= 1
    turns += 1
    c3 += 1
    if c3 == 10:
        n += 9
        c3 = 0
    broke(n, turns)
    