# Given: A DNA string s (of length at most 1 kbp) and a collection of substrings of s acting as introns. All strings are given in FASTA format.
# 
# Return: A protein string resulting from transcribing and translating the exons of s. (Note: Only one solution will exist for the dataset provided.)

def read_file(filepath) :
    """Reading a file and returning a list of lines"""
    with open(filepath, 'r') as f :
        return [l.strip() for l in f.readlines()]
    
RNAtoAA = {
'UUU' : 'F'   ,   'CUU' : 'L',      'AUU' : 'I',      'GUU' : 'V',
'UUC' : 'F'   ,   'CUC' : 'L',      'AUC' : 'I',      'GUC' : 'V',
'UUA' : 'L'   ,   'CUA' : 'L',      'AUA' : 'I',      'GUA' : 'V',
'UUG' : 'L'   ,   'CUG' : 'L',      'AUG' : 'M',      'GUG' : 'V',
'UCU' : 'S'   ,   'CCU' : 'P',      'ACU' : 'T',      'GCU' : 'A',
'UCC' : 'S'   ,   'CCC' : 'P',      'ACC' : 'T',      'GCC' : 'A',
'UCA' : 'S'   ,   'CCA' : 'P',      'ACA' : 'T',      'GCA' : 'A',
'UCG' : 'S'   ,   'CCG' : 'P',      'ACG' : 'T',      'GCG' : 'A',
'UAU' : 'Y'   ,   'CAU' : 'H',      'AAU' : 'N',      'GAU' : 'D',
'UAC' : 'Y'   ,   'CAC' : 'H',      'AAC' : 'N',      'GAC' : 'D',
'UAA' : 'Stop',   'CAA' : 'Q',      'AAA' : 'K',      'GAA' : 'E',
'UAG' : 'Stop',   'CAG' : 'Q',      'AAG' : 'K',      'GAG' : 'E',
'UGU' : 'C'   ,   'CGU' : 'R',      'AGU' : 'S',      'GGU' : 'G',
'UGC' : 'C'   ,   'CGC' : 'R',      'AGC' : 'S',      'GGC' : 'G',
'UGA' : 'Stop',   'CGA' : 'R',      'AGA' : 'R',      'GGA' : 'G',
'UGG' : 'W'   ,   'CGG' : 'R',      'AGG' : 'R',      'GGG' : 'G' 
}
    
FasFile = read_file('./rosalind/rosalind_splc.txt')
FasDic = {}
Faslabel = ""
for line in FasFile :
    if '>' in line :
        Faslabel = line
        FasDic[Faslabel] = ""
    else :
        FasDic[Faslabel] += line
        
sq = ''
for key,value in FasDic.items() :
    if sq == "" :
        sq = value
    else :
        if value in sq :
            sq = sq.replace(value, "")
            
sq = sq.replace("T", "U")
AA = []
for i in range(0, 3) :
    tmsq = list(sq[i:])
    if len(tmsq) % 3 == 1 :
        tmsq.pop()
    elif len(tmsq) % 3 == 2:
        tmsq.pop()
        tmsq.pop()
    tmsq = ''.join(tmsq)
    for ii in range(0, len(tmsq) - 2) :
        if tmsq[ii: ii + 3] == "AUG" :
            tmp = []
            n = 0
            while ii + n + 3 <= len(tmsq)  :
                if RNAtoAA[tmsq[ii + n : ii + n + 3]] == 'Stop' :
                    AA.append(tmp)
                    break
                tmp.append(RNAtoAA[tmsq[ii + n : ii + n + 3]])
                n += 3 
                
print(''.join(AA[0]))