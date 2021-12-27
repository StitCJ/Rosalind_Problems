# https://rosalind.info/problems/lgis/
#
# Given: A positive integer n≤10000 followed by a permutation π of length n.
# 
# Return: A longest increasing subsequence of π, followed by a longest decreasing subsequence of π.

def increasing(numbers) :
    tr = [1] * len(numbers)
    low = [None] * len(numbers)

    for i in range(1, len(numbers)) :
        tmp = []
        for ii in range(0, i) :
            if numbers[ii] < numbers[i] :
                tmp.append(tr[i] + tr[ii])
            else :
                tmp.append(1)
        if len(tmp) != 0 : 
            tr[i] = max(tmp)
            lwidx = tmp.index(max(tmp))
            low[i] = lwidx
    
    idx = tr.index(max(tr))
    a = low[idx]
    rst = []
    rst.append(numbers[idx])
    while a != 0 :
        rst.append(numbers[a])
        a = low[a]

    return rst[::-1]
     
f = open('./rosalind/rosalind_lgis.txt', 'r')
lngth = int(f.readline().strip('\n'))
line = f.readlines()
f.close()
line = line[0].split()
num = []
for i in line :
    num.append(int(i))    

f2 = open('./rosalind/output.txt', 'w')
data = increasing(num)
f2.write(' '.join(map(str, data)))
f2.write('\n')
num2 = num[::-1]
data2 = increasing(num2)[::-1]
f2.write(' '.join(map(str,data2)))
f2.close()



