board = [[i for i in input()] for i in range(3)]

a = []

for letter in ['X', 'O']:
    for i in range(3):
        if board[i] == [letter, letter, letter]:
            a.append(letter)
        if board[0][i] == letter and board[1][i] == letter and board[2][i] == letter:
            a.append(letter)
    if board[0][0] == letter and board[1][1] == letter and board[2][2] == letter:
        a.append(letter)
    if board[0][2] == letter and board[1][1] == letter and board[2][0] == letter:
        a.append(letter)

a = list(set(a))

if a == ['X', 'O'] or a == ['O', 'X']:
    print("Error, redo")
elif a == ['X']:
    print("Timothy")
elif a == ['O']:
    print("Griffy")
elif a == []:
    print("Tie")