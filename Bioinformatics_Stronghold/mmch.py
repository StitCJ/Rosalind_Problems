#  https://rosalind.info/problems/mmch/
#  Given: An RNA string s of length at most 100.
#  
#  Return: The total possible number of maximum matchings of basepair edges in the bonding graph of s
#  Recommend to use Python 2.7 to solve this problem

import collections

def read_file(filepath) :
    with open(filepath, 'r') as f :
        return [l.strip() for l in f.readlines()]

def count_nucleotides(seq) :
    dic = collections.Counter(seq)
    return dic

fdic = {}
def fac(n) :
    if n in fdic :
        return fdic[n]
    if n == 0 or n == 1 :
        fdic[n] = 1
        return fdic[n]
    else :
        fdic[n] = n * fac(n - 1)
        return fdic[n]

file = read_file('./rosalind/rosalind_mmch.txt')
seq = ""
for line in file :
    if '>' not in line :
        seq += line

fre = count_nucleotides(seq)
a = fre['A']
b = fre['U']
c = fre['G']
d = fre['C']

if a < b :
    a, b = b, a
if c < d :
    c, d = d, c


answer = (fac(a)/fac(a - b)) * (fac(c)/fac(c - d))
print(seq)
print(fre)
print(int(answer))