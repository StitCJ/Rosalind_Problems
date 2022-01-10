#  https://rosalind.info/problems/lexv/
#
#  Given: A permutation of at most 12 symbols defining an ordered alphabet A and a positive integer n (n≤4).
#
#  Return: All strings of length at most n formed from A, ordered lexicographically. (Note: As in “Enumerating k-mers Lexicographically”, 
#  alphabet order is based on the order in which the symbols are given.)

def read_file(filepath) :
    with open(filepath, 'r') as f :
        return [l.strip() for l in f.readlines()]
    
file = read_file('./rosalind/rosalind_lexv.txt')
alpha = file[0].split()
num = int(file[1])

dic = {(1, 1) : [0], (2, 1) : [0, 1], (3, 1) : [0, 1, 2], (4, 1) : [0, 1, 2, 3]}
def lexv(a, b) :
    if (a, b) in dic :
        return dic[(a, b)]
    elif b == 1 :
        rst = []
        for i in range(a) :
            rst.append(i)
        dic[(a, b)] = rst
        return dic[(a, b)]
    rst = []
    if b == 2 :
        for i in range(a) :
            tmp = []
            tmp.append(i)
            rst.append(tmp)
            for ii in range(len(lexv(a, b - 1))) :
                tmp = []
                tmp.append(lexv(a, b-1)[ii])
                tmp.insert(0, i)
                rst.append(tmp)
        dic[(a, b)] = rst
    else :
        for i in range(a) :
            tmp = []
            tmp.append(i)
            rst.append(tmp)
            for ii in range(len(lexv(a, b - 1))) :
                tmp = []
                tmp.extend(lexv(a, b-1)[ii])
                tmp.insert(0, i)
                rst.append(tmp)
        dic[(a, b)] = rst
        
    return dic[(a, b)]

with open('./rosalind/output.txt', 'w') as f2 :  
    answer = lexv(len(alpha), num)
    while answer :
        q = answer.pop(0)
        ans = []
        while q :
            q2 = q.pop(0)
            ans.append(alpha[q2])
        data = ''.join(ans)
        f2.write(data)
        f2.write('\n')