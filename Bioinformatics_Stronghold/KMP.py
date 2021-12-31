#  https://rosalind.info/problems/kmp/
#  Given: A DNA string s (of length at most 100 kbp) in FASTA format.
#  
#  Return: The failure array of s.

def read_file(filepath) :
    with open(filepath, 'r') as f :
        return [l.strip() for l in f.readlines()]
    
file = read_file('./rosalind/rosalind_kmp.txt')
sq = ""
for line in file :
    if '>' not in line :
        sq += line

fail = [0] * len(sq)
for i in range(1, len(sq)) :
    if sq[i] == sq[0] :
        if fail[i] == 0 :
            fail[i] = 1
        err = 0
        n = 2
        while err == 0 :
            if sq[i: i + n] == sq[:n] :
                if n > fail[i + n - 1] :
                    fail[i+n-1] = n
                n +=1
            else :
                err = 1


with open('./rosalind/output.txt', 'w') as f2 :
    data = ' '.join(map(str, fail))
    f2.write(data)
    
#for i in range(1, len(sq)) :
#    if fail[i] == 0 :
#        if sq[i] == sq[0] :
#            fail[i] = 1
#            err = 0
#            n = 2
#            while err == 0 :
#                if sq[i: i + n] == sq[:n] :
#                    fail[i+n-1] = n
#                    n +=1
#                else :
#                    err = 1
#        for j in range(1, i + 1) :
#            if sq[j:i + 1] == sq[:i - j + 1] :
#                fail[i] = i - j + 1
#                break
#    