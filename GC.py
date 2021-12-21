f = open("rosalind_gc.txt", 'r')
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

RstDicKeys = FasDic.keys()
RstDic = {}
tot = 0
num = 0
for a in RstDicKeys :
    for b in FasDic[a] :
        tot += 1
        if b == "G" or b == "C" :
            num += 1
    RstDic[a] = round(num / tot * 100, 6)
    num = 0
    tot = 0
    
rst = 0
rstName = ""
for c in RstDic.keys() :
    if RstDic[c] > rst :
        rst = RstDic[c]
        rstName = c
        
print(rstName.strip(">"))
print(rst)