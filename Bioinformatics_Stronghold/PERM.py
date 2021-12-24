# Given: A positive integer n≤7.
# 
# Return: The total number of permutations of length n, followed by a list of all such permutations (in any order).

from itertools import permutations

def prm(n) :
    lst = []
    for i in range(1, n + 1) :
        lst.append(i)
    rst = list(permutations(lst, n))
    while rst :
        tmp = list(rst.pop())
        print(' '.join(map(str, tmp)))

def fac(n) :
    if n <= 1 :
        return 1
    else :
        return n * fac(n - 1)
    
print(fac(6))
prm(6)
