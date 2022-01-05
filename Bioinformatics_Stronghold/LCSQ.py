#  https://rosalind.info/problems/lcsq/
#
#  Given: Two DNA strings s and t (each having length at most 1 kbp) in FASTA format.
#  
#  Return: A longest common subsequence of s and t. (If more than one solution exists, you may return any one.)
import numpy as np

def read_file(filepath) :
    with open(filepath, 'r') as f :
        return [l.strip() for l in f.readlines()]
    
file = read_file('./rosalind/rosalind_lcsq.txt')
sq = ''
seq = []
for line in file :
    if '>' not in line :
        sq += line
    else :
        seq.append(sq)
        sq = ""
seq.pop(0)
seq.append(sq)

sq1 = seq[0]
sq2 = seq[1]

def lcsq(seq1, seq2) :
    seq1 = list(seq1)
    seq2 = list(seq2)
    seq1.insert(0, 0)
    seq2.insert(0, 0)
    if len(seq1) > len(seq2) :
        seq1, seq2 = seq2, seq1
    mtx = np.zeros((len(seq1), len(seq2)))
    for i in range(1, len(seq1)) :
        for ii in range(1, len(seq2)) :
            if seq1[i] == seq2[ii] :
                mtx[i][ii] = mtx[i - 1][ii - 1] + 1
            else :
                mtx[i][ii] = max(mtx[i - 1][ii], mtx[i][ii - 1])
    rst = []
    l, c = len(seq1) - 1, len(seq2) - 1
    while len(rst) != mtx[len(seq1) - 1][len(seq2) - 1] :
        if mtx[l][c] == mtx[l - 1][c] :
            l -= 1
        elif mtx[l][c] == mtx[l][c - 1] :
            c -= 1
        else :
            rst.append(seq1[l])
            l -= 1
            c -= 1
    return ''.join(rst[::-1])

print(lcsq(sq1, sq2))