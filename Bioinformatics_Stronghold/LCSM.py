# Given: A collection of k (k≤100) DNA strings of length at most 1 kbp each in FASTA format.
# Return: A longest common substring of the collection. (If multiple solutions exist, you may return any single solution.)


def read_file(filepath) :
    """Reading a file and returning a list of lines"""
    with open(filepath, 'r') as f :
        return [l.strip() for l in f.readlines()]
  
FasFile = read_file('./rosalind/rosalind_lcsm.txt')
FasDic = {}
Faslabel = ""
for line in FasFile :
    if '>' in line :
        Faslabel = line
        FasDic[Faslabel] = ""
    else :
        FasDic[Faslabel] += line

sqlst = list(FasDic.values())
tmpsq = []

b = min(sqlst, key=len)
sqlst.remove(b)
a = min(sqlst, key=len)
sqlst.remove(a)

for i in range(0, len(b) - 1) :
    tl = len(b) - i
    for ii in range(0, len(b) - tl + 1) :
       tmpsq.append(b[ii:ii+tl]) 
       
m = 0
while True :
    mtf = tmpsq.pop(0)
    n = 0
    for c in sqlst :
        if mtf not in c :
            break
        else :
            n += 1
        if n == len(sqlst) :
            m = 1
            break
    if m == 1 :
        break

print(mtf)
    