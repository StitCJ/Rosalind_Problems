#  https://rosalind.info/problems/prob/
#
#  Given: A DNA string s of length at most 100 bp and an array A containing at most 20 numbers between 0 and 1.
#
#  Return: An array B having the same length as A in which B[k] represents the common logarithm of the probability that a random string constructed with the GC-content found in A[k] will match s exactly.
#


import math

with open('./rosalind/rosalind_prob.txt', 'r') as f :
    sq = f.readline().strip('\n')
    gc_content = list((f.readline().split()))

ans = []

for i in gc_content :
    i = float(i)
    pro = { 'A' : (1 - i) / 2, 'T' : (1 - i) / 2, 'G' : i / 2, 'C' : i / 2}
    rst = 1
    for nuc in sq :
        rst *= pro[nuc]
    ans.append(rst)
    
for ii in range(len(ans)) :
    ans[ii] = round(math.log10(ans[ii]), 3)
    
print(' '.join(map(str, ans)))
