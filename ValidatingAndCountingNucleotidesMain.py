from rosalind.ValidatingAndCountingNucleotidesDNAToolkit import*
import random

# Creating a random DNA seqeunce for testing
rndDNAstr = ''.join([random.choice(Nucleotides)
                      for nuc in range(20)])

print(validateSeq(rndDNAstr))
print(countNucFrequency(rndDNAstr))