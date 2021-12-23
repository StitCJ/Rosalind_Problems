# Given: Two positive integers k (k≤7) and N (N≤2k). In this problem, we begin with Tom, who in the 0th generation has genotype Aa Bb. Tom has two children in the 1st generation, 
# each of whom has two children, and so on. Each organism always mates with an organism having genotype Aa Bb.
# Return: The probability that at least N Aa Bb organisms will belong to the k-th generation of Tom's family tree (don't count the Aa Bb mates at each level). 
# Assume that Mendel's second law holds for the factors.

def fac(n) :
    if n <= 1 :
        return 1
    else :
        rst = 1
        return n * fac(n - 1)
    
def cmb(n, k):
    return fac(n) / (fac(k) * fac(n - k))

p1 = 1/4
p2 = 3/4

def msl(k, n) :
    np = 2 ** k
    pos = 0
    for i in range(n, np + 1) :
        rst = cmb(np, i)
        pos += rst * (p1 ** i) * (p2 ** (np - i))
    
    return round(pos, 3)
    
print(msl(6, 16))
