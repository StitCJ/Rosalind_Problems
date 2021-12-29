#  https://rosalind.info/problems/sseq/
#  
#  Given: Two DNA strings s and t (each of length at most 1 kbp) in FASTA format.
#
#  Return: One collection of indices of s in which the symbols of t appear as a subsequence of s. If multiple solutions exist, you may return any one.

def read_file(filepath) :
    with open(filepath, 'r') as f :
        return [l.strip() for l in f.readlines()]
    
Fasfile = read_file('./rosalind/rosalind_sseq.txt')
tmpsq = ""
sq = []
for line in Fasfile :
    if '>' in line :
        sq.append(tmpsq)
        tmpsq = ""
    else :
        tmpsq += line
sq.pop(0)
sq.append(tmpsq)


rst = []
n = 0
for i in sq[1] :
    for ii in range(n, len(sq[0])) :
        if i == sq[0][ii] :
            rst.append(ii + 1)
            n = ii + 1
            break
        
print(' '.join(map(str, rst)))