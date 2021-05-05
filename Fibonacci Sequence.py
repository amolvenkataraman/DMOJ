fib_ = [0, 1]

def fib(n):
    global fib_
    try:
        return fib_[n]
    except IndexError:
        return fib(n - 1) + fib(n - 2)

"""
def memoize(f):
    memo = {}
    def helper(x):
        if x not in memo:            
            memo[x] = f(x)
        return memo[x]
    return helper
    

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

fib = memoize(fib)
"""

n = int(input())
print(fib(n) % 1000000007)