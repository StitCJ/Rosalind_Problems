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