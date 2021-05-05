def main():
    for i in range(int(input())):
        n = int(input())
        while n > 1:
            pn = n;
            while prime(pn) == 0 or not n%pn == 0:
                pn -= 1
            print(pn, end="")
            n = int(n / pn)
        print()

def prime(num):
	factors = 0
	for i in range(2,num):
		if (num % i) == 0:
 			factors += 1
 			break
	if factors == 0:
		return 1
	else:
		return 0

if __name__ == '__main__':
	main()