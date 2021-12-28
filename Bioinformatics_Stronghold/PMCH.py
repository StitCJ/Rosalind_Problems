#  https://rosalind.info/problems/pmch/
#  Given: An RNA string s of length at most 80 bp having the same number of occurrences of 'A' as 'U' and the same number of occurrences of 'C' as 'G'.
#  
#  Return: The total possible number of perfect matchings of basepair edges in the bonding graph of s.

import collections

def read_file(filepath) :
    with open(filepath, 'r') as f :
        return [i.strip() for i in f.readlines()]
    
def fac(n) :
    if n < 2 :
        return 1
    else :
        return n * fac(n - 1)
    
RNA_Complement = {"A" : "U", "C" : "G", "G" : "C", "U" : "A"}

FasFile = read_file('./rosalind/rosalind_pmch.txt')
sq = ""
for line in FasFile :
    if '>' not in line :
        sq += line
        
frq = collections.Counter(sq)
a = frq['A']
b = frq['G']

print(fac(a) * fac(b))