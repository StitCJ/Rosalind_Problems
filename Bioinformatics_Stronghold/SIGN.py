#  https://rosalind.info/problems/sign/
#  Given: A positive integer n≤6.
#
#  Return: The total number of signed permutations of length n, followed by a list of all such permutations 
#  (you may list the signed permutations in any order).

from itertools import permutations

def sign(n) :
    lst = []
    for i in range(1, n+1) :
        lst.append(i)
        lst.append(-i)
    lst.sort()
    ans = list(permutations(lst, n))
    rcd = []
    stop = 0
    for i in ans :
        for ii in range(len(i)) :
            if stop == 1 :
                stop = 0
                break
            for n in range(1, len(i) - ii) :
               if abs(i[ii]) == abs(i[ii + n]) :
                   rcd.append(i)
                   stop += 1
                   break

    for i in rcd :
        ans.remove(i)
        
    return ans

ans = sign(3)
with open('./rosalind/output.txt', 'w') as f :        
    data = len(ans)
    f.write(str(data))
    f.write('\n')
    for i in ans :
        data = ' '.join(map(str, i))
        f.write(data)
        f.write('\n')
