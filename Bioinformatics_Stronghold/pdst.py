#  https://rosalind.info/problems/pdst/

#  Given: A collection of n (n≤10) DNA strings s1,…,sn of equal length (at most 1 kbp). Strings are given in FASTA format.
#  
#  Return: The matrix D corresponding to the p-distance dp on the given strings. As always, note that your answer is allowed an absolute error of 0.001.
import numpy as np

def read_file(filepath) :
    with open(filepath, 'r') as f :
        return [l.strip() for l in f.readlines()]

def comp(seq1, seq2) :
    seq1 = list(seq1)
    seq2 = list(seq2)
    count = 0
    for a in range(len(seq1)) :
        if seq1[a] != seq2[a] :
            count += 1
    return count

file = read_file('./rosalind/rosalind_pdst.txt')
dic = {}
seq = ""
for line in file :
    if '>' in line :
        key = line
        dic[key] = ""
    else :
        dic[key] += line
keys = dic.keys()
values = list(dic.values())

mtx = np.zeros((len(keys), len(keys)))
for i in range(len(keys)) :
    for ii in range(len(keys)) :
        if i != ii :
            mtx[i][ii] = comp(values[i], values[ii])/len(values[0])

for i in range(len(keys)) :
    for ii in range(len(keys)) :
        b = mtx[i][ii]
        a = "{:.5f}".format(b)
        print(a, end = " ")
    print("")