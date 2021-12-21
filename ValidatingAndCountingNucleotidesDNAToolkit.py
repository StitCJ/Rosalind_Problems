Nucleotides = ["A", "C", "G", "T"]
import collections

# Check the sequence to make sure it is a DNA string
def validateSeq(dna_seq) :
    tmpseq = dna_seq.upper()
    for nuc in tmpseq :
        if nuc not in Nucleotides :
            return False
        return tmpseq
    
def countNucFrequency(seq) :
    #tmpFreDict = { "A" : 0, "C" : 0, "G" : 0, "T" : 0}
    #for nuc in seq :
    #    tmpFreDict[nuc] += 1
    #return tmpFreDict
     return dict(collections.Counter(seq))
    