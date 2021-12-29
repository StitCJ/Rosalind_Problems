#  https://rosalind.info/problems/tran/
#  
#  Given: Two DNA strings s1 and s2 of equal length (at most 1 kbp).
#  
#  Return: The transition/transversion ratio R(s1,s2).

def read_file(filepath) :
    with open(filepath, 'r') as f :
        return [l.strip() for l in f.readlines()]
    
Fasfile = read_file('./rosalind/rosalind_tran.txt')
tmpsq = ""
sq = []
for line in Fasfile :
    if '>' in line :
        sq.append(tmpsq)
        tmpsq = ""
    else :
        tmpsq += line
sq.append(tmpsq)
sq.pop(0)
transition = 0
transversion = 0
purine = ['A', 'G']
pyramidine = ['T', 'C']
for i in range(len(sq[0])) :
    a = sq[0][i]
    b = sq[1][i]
    if a == b :
        continue
    else :
        if a in purine and b in purine :
            transition += 1
        elif a in purine and b in pyramidine :
            transversion += 1
        elif a in pyramidine and b in purine :
            transversion += 1
        else :
            transition += 1
            
print(round(transition/transversion, 11))