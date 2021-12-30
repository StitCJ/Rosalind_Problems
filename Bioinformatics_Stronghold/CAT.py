#  https://rosalind.info/problems/cat/
#  Given: An RNA string s having the same number of occurrences of 'A' as 'U' and the same number of occurrences of 'C' as 'G'. The length of the string is at most 300 bp.
#  
#  Return: The total number of noncrossing perfect matchings of basepair edges in the bonding graph of s, modulo 1,000,000.

# typical catalan number
# def cat(n) :
#     if n < 2 :
#         return 1
#     rst = 0
#     for i in range (0, n) :
#         ii = i + 1
#         rst += cat(n - ii) * cat(i)
#     return rst


RNA_Complement = {"A" : "U", "C" : "G", "G" : "C", "U" : "A"}

dic = {}
def cat_num(seq) :
    if seq not in dic :
        n = len(seq)
        if n == 0 :
            dic[seq] = 1
            return dic[seq]
        elif n == 2 and RNA_Complement[seq[0]] == seq[1] :
            dic[seq] = 1
            return dic[seq]
        else :
            rst = 0
            for i in range(1, n, 2) :
                if RNA_Complement[seq[0]] == seq[i] :
                    test = seq[1:i]
                    test2 = seq[i + 1:]
                    if len(test) > len(test2) :
                        test, test2 = test2, test
                    if cat_num(test) > 0 :
                        if cat_num(test2) > 0:
                            rst += dic[test] * dic[test2]
            dic[seq] = rst
    return dic[seq]
    
def read_file(filepath) :
    with open(filepath, 'r') as f :
        return [l.strip() for l in f.readlines()]
    
file = read_file('./rosalind/rosalind_cat.txt')
sq = ""
for line in file :
    if '>' not in line :
        sq += line
        
answer = cat_num(sq) % 1000000
print(answer)