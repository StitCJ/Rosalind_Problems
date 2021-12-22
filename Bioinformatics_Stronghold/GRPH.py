def read_file(filepath) :
    """Reading a file and returning a list of lines"""
    with open(filepath, 'r') as f :
        return [l.strip() for l in f.readlines()]
    
Fas = read_file('./rosalind/rosalind_grph.txt')
FasDic = {}
key = ""
rst = []
for line in Fas :
    if  '>' in line :
        key = line
        FasDic[key] = ""
    else :
        FasDic[key] += line
        
while FasDic :
    nm, sq = FasDic.popitem()
    nm = nm.strip(">")
    for key, value in FasDic.items() :
        key = key.strip(">")
        if sq[-3:] == value[:3] :
            rst.append(f'{nm} {key}')
        if sq[:3] == value[-3:] :
            rst.append(f'{key} {nm}')
   
f = open("./rosalind/output.txt", "w")
data = '\n'.join(rst)
f.write(data)