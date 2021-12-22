#stupy more !

f = open("./rosalind/rosalind_cons.txt", 'r')
FasDic = {}
FasList = []
KeyName = "0"
while True :
    line = f.readline()
    if not line:
        FasDic[KeyName] = "".join(FasList)
        break
    if line[0] == ">" and KeyName != "0" :
        FasDic[KeyName] = "".join(FasList)
        KeyName = line.strip("\n")
        FasList = []
    elif line[0] == ">" :
        KeyName = line.strip("\n")
    else :
         FasList.append(line.strip("\n"))
f.close()
Fas = []
for key, value in FasDic.items() :
    Fas.append(value)
    
pro = {'A' : [], 'C' : [], "G" : [], "T" : []}

for n in ['A', 'T', 'G', 'C'] :
    for nn in range (0, len(Fas[0])) :
        pro[n].append(0)

for i in range (0, len(Fas)) :
    for ii in range (0, len(Fas[0])) :
        pro[Fas[i][ii]][ii] += 1 


rst = []        
for a in range(0, len(Fas[0])) :
    tmp = 0
    tmprst = ""
    for aa in ['A', 'C', 'G', 'T'] :
        if pro[aa][a] >= tmp :
            tmp = pro[aa][a]
            tmprst = aa
    rst.append(tmprst)        
    
f = open("./rosalind/ouput.txt", "w")
data = ''.join(rst)
f.write(data)
f.write("\n")

for key,value in pro.items() :
    val = ' '.join(map(str, value))
    data = f'{key}: {val}\n'
    f.write(data)