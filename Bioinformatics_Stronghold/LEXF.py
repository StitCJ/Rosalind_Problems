# Given: A collection of at most 10 symbols defining an ordered alphabet, and a positive integer n (n≤10).
# 
# Return: All strings of length n that can be formed from the alphabet, ordered lexicographically (use the standard order of symbols in the English alphabet).

from itertools import product
def lexf(lst, n) :
    for i in product(lst, repeat = n) :
        print(''.join(i))
        
lexf(['A', 'B', 'C', 'D', 'E'], 4)