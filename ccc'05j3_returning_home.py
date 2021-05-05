dir_ = []

while(True):
    t1 = input()
    t2 = input()
    dir_.append([t1, t2])

    if t2 == "SCHOOL":
        break

l = len(dir_)
dir_.reverse()
print(dir_)

for i in range(l):
    if i < l - 1:
        if dir_[i][0] == 'R':
            print("Turn LEFT onto " + dir_[i - 1][1] + " street.")
        else:
            print("Turn RIGHT onto " + dir_[i - 1][1] + " street.")
    else:
        if dir_[i][0] == 'R':
            print("Turn LEFT into your HOME.")
        else:
            print("Turn RIGHT into your HOME.")