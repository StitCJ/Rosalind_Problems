from functools import lru_cache

@lru_cache()
def fib(n, m) :
    if n == 1 or n ==2 :
        return 1
    elif n <= m :
        return fib(n - 1, m) + fib(n - 2, m)
    elif n == m + 1 :
        return fib(n - 1, m) + fib(n - 2, m) - 1
    else :
        return fib(n - 1, m) + fib(n - 2, m) - fib(n - m - 1, m)
    
print(fib(93, 20))