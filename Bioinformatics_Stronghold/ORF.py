#Given: A DNA string s of length at most 1 kbp in FASTA format.
#
#Return: Every distinct candidate protein string that can be translated from ORFs of s. Strings can be returned in any order.

def read_file(filepath) :
    """Reading a file and returning a list of lines"""
    with open(filepath, 'r') as f :
        return [l.strip() for l in f.readlines()]

def orf(seq) :
    #rst list must already exist
    for i in range(0, 3) :
        tmpsq = list(seq[i:])
        lsq = len(tmpsq)
        if lsq % 3 == 1 :
            tmpsq.pop()
        elif lsq % 3 == 2:
            tmpsq.pop()
            tmpsq.pop()

        tmpsq = ''.join(tmpsq)
        for ii in range(0, len(tmpsq) - 2, 3) :
            strt = 'AUG'
            cdn = ""
            stp = 0
            tmp = tmpsq[ii:ii+3]     

            if tmp == strt :
                n = 0
                while ii + (3 * (n + 1)) <= len(tmpsq) :
                    if RNAtoAA[tmpsq[ii + (3 * n) : ii + (3 * (n +1) )]] == 'Stop' :
                        stp += 1
                        break
                    cdn += RNAtoAA[tmpsq[ii + (3 * n) : ii + (3 * (n +1) )]]
                    n += 1

                if stp == 1 :
                    rst.append(cdn)
                    stp = 0
                    
def reverse_complement(seq) :
    """A<->T, G<->C. Reversing newly generated string"""
    # return ''.join([DNA_ReverseComplement[nuc] for nuc in seq])[::-1]
    mapping = str.maketrans('AUCG', 'UAGC')
    return seq.translate(mapping)[ : : -1]
 
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
 
FasFile = read_file('./rosalind/rosalind_orf.txt')
sq = ""
for line in FasFile :
    if '>' in line :
        continue
    else :
        sq += line
        
sq = sq.replace('T', 'U')
rst = []

sq2 = reverse_complement(sq)
orf(sq)
orf(sq2)

rst = set(rst)
while rst :
    print(rst.pop())