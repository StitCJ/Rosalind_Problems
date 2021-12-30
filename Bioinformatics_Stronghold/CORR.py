#  https://rosalind.info/problems/corr/
#  
#  Given: A collection of up to 1000 reads of equal length (at most 50 bp) in FASTA format. Some of these reads were generated with a single-nucleotide error. For each read s in the dataset, one of the following applies:
#  
#  s was correctly sequenced and appears in the dataset at least twice (possibly as a reverse complement);
#  s is incorrect, it appears in the dataset exactly once, and its Hamming distance is 1 with respect to exactly one correct read in the dataset (or its reverse complement).
#  Return: A list of all corrections in the form "[old read]->[new read]". (Each correction must be a single symbol substitution, and you may return the corrections in any order.)

def read_file(filepath) :
    with open(filepath, 'r') as f :
        return [l.strip() for l in f.readlines()]
    
def reverse_complement(seq) :
    """A<->T, G<->C. Reversing newly generated string"""
    # return ''.join([DNA_ReverseComplement[nuc] for nuc in seq])[::-1]
    mapping = str.maketrans('ATCG', 'TAGC')
    return seq.translate(mapping)[ : : -1]

def mut(seq1, seq2) :
    count = 0
    seq1 = list(seq1)
    seq2 = list(seq2)
    for i in seq1 :
        if i == seq2.pop(0) :
            continue
        else :
            count += 1
    return count
    
file = read_file('./rosalind/rosalind_corr.txt')
sq = ''
sqlst = []
for line in file :
    if '>' in line :
        sqlst.append(sq)
        sq = ''
    else :
        sq += line
sqlst.pop(0)
sqlst.append(sq)
sqlst2 = []
for i in sqlst :
    sqlst2.append(i)

for i in range(len(sqlst)) :
    sqlst[i] = [sqlst[i], reverse_complement(sqlst[i])]
    sqlst[i].sort()
    
    
sqdic = {}
for i in sqlst :
    if i[0] not in sqdic :
        sqdic[i[0]] = 1
    else :
        sqdic[i[0]] += 1
        
rst = []
for key, value in sqdic.items() :
    if value >= 2 :
        for key2, value2 in sqdic.items() :
            if value2 == 1 :
                if mut(key, key2) == 1 :
                    tmp = [key2, key]
                    rst.append(tmp)
                elif mut(key, reverse_complement(key2)) == 1:
                    tmp = [reverse_complement(key2), key]
                    rst.append(tmp)
                     
for i in range(len(rst)) :
    if rst[i][0] not in sqlst2 :
        rst[i] = [reverse_complement(rst[i][0]), reverse_complement(rst[i][1])]

with open('./rosalind/output.txt', 'w') as f2 :
    for i in rst :
        data = '->'.join(i)
        f2.write(data)
        f2.write('\n')
        

