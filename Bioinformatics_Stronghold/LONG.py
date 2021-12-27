# https://rosalind.info/problems/long/
#
# Given: At most 50 DNA strings of approximately equal length, not exceeding 1 kbp, in FASTA format (which represent reads deriving from the same strand of a single linear chromosome).
# 
# The dataset is guaranteed to satisfy the following condition: there exists a unique way to reconstruct the entire chromosome from these reads by gluing together pairs of reads that overlap by more than half their length.
# 
# Return: A shortest superstring containing all the given strings (thus corresponding to a reconstructed chromosome).

def read_file(filepath) :
    """Reading a file and returning a list of lines"""
    with open(filepath, 'r') as f :
        return [l.strip() for l in f.readlines()]
    
    
FasFile = read_file('./rosalind/rosalind.txt')
FasDic = {}
Faslabel = ""
for line in FasFile :
    if '>' in line :
        Faslabel = line
        FasDic[Faslabel] = ""
    else :
        FasDic[Faslabel] += line
        
seq = list(FasDic.values())
super = seq.pop(0)
while seq :
    for i in seq:
        for ii in range(len(i)//2, len(i))[::-1]:
            if super[-ii:] == i[:ii]:
                super = super + i[ii:]
                seq.remove(i)
            elif super[:ii] == i[-ii:]:
                super = i[:-ii] + super
                seq.remove(i)

f2 = open('./rosalind/output.txt', 'w')
data = super
f2.write(data)
f2.close()


