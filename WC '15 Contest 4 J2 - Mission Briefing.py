inp = input()
print(sum([1 if ".00"+str(i)+"."in inp else 0 for i in range(1, 10)]))