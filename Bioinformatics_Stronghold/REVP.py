# Given: A DNA string of length at most 1 kbp in FASTA format.
# 
# Return: The position and length of every reverse palindrome in the string having length between 4 and 12. 
# You may return these pairs in any order.

def read_file(filepath) :
    """Reading a file and returning a list of lines"""
    with open(filepath, 'r') as f :
        return [l.strip() for l in f.readlines()]
    
FasFile = read_file('./rosalind/rosalind_revp.txt')
sq = ""
for line in FasFile :
    if '>' in line :
        continue
    else :
        sq += line
trcDic = {'A' : 'T', 'T' : 'A', 'G' : 'C', 'C' : 'G'}
rcdDic = {}
for i in range(len(sq) - 1) :
    lmt = len(sq) - i - 2
    if trcDic[sq[i]] == sq[i + 1] :
        n = 1
        key = 2
        while i >= n and lmt >= n :
            if trcDic[sq[i - n]] == sq[i + 1 + n] :
                 key += 2
                 if key >= 4 and key <= 12 :
                     rcdDic[i - n + 1] = key
                 n += 1
            else :
                break
        
for key, value in rcdDic.items() :
    print(key, value)