#  https://rosalind.info/problems/kmer/
#  Given: A DNA string s in FASTA format (having length at most 100 kbp).
#  
#  Return: The 4-mer composition of s.

def read_file(filepath) :
    with open(filepath, 'r') as f :
        return [l.strip() for l in f.readlines()]
    
file = read_file('./rosalind/rosalind_kmer.txt')
sq = ""
for line in file :
    if '>' not in line :
        sq += line
dic = {}
for ii in range(4) :
    sq2 = sq[ii:]
    for i in range(0, len(sq2) - 3, 4) :
        if sq2[i:i+4] not in dic :
            dic[sq2[i:i+4]] = 1
        else :
            dic[sq2[i:i+4]] += 1
        
sdic = sorted(dic.items())

with open('./rosalind/output.txt', 'w') as f2 :
    for data in sdic :
        f2.write(f'{str(data[1])} ')