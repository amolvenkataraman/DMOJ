ladders = {9: 34, 40: 64, 67: 86}
snakes = {54: 19, 90: 48, 99: 77}

pos = 1
while True:
    dice = int(input())

    if dice == 0:
        print("You Quit!")
        raise SystemExit
    
    if pos + dice <= 100:
        pos += dice

    for i in ladders:
        if pos == i:
            pos = ladders[i]
    for i in snakes:
        if pos == i:
            pos = snakes[i]
    
    print("You are now on square " + str(pos))

    if pos == 100:
        print("You Win!")
        raise SystemExit
