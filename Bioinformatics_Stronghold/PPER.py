#  https://rosalind.info/problems/pper/
#
#  Given: Positive integers n and k such that 100≥n>0 and 10≥k>0.
#  
#  Return: The total number of partial permutations P(n,k), modulo 1,000,000.

def fac(n) :
    if n < 2 :
        return 1
    else :
        return n * fac(n - 1)
    
def pper(n, k) :
    return (fac(n) / fac(n - k)) % 1000000

print(pper(82, 9))