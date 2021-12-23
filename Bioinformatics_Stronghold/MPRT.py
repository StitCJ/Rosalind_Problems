# Given: At most 15 UniProt Protein Database access IDs.
# Return: For each protein possessing the N-glycosylation motif, output its given access ID followed by a list of locations in the protein string where the motif can be found.

import requests
from bs4 import BeautifulSoup

f1 = open("./rosalind/rosalind.txt", 'r')
lst = []
while True :
    line = f1.readline()
    if not line :
        break
    lst.append(line.strip('\n'))
    
f1.close()

for nm in lst :
    url = f"https://www.uniprot.org/uniprot/{nm}.fasta"
    txt = requests.get(url)

    f2 = open("./rosalind/data.txt", 'a') 
    data = txt.text
    f2.write(data)

    f2.close()

def read_file(filepath) :
    """Reading a file and returning a list of lines"""
    with open(filepath, 'r') as f :
        return [l.strip() for l in f.readlines()]
    
FasFile = read_file('./rosalind/data.txt')
FasDic = {}
Faslabel = ""
for line in FasFile :
    if '>' in line :
        Faslabel = lst.pop(0)
        FasDic[Faslabel] = ""
    else :
        FasDic[Faslabel] += line
        
for nk in lst :
    for key in FasDic.keys() :
        FasDic[nk] = FasDic.pop(key)
        
rstdic = {}
for key, value in FasDic.items() :
    rstlst = []
    for i in range(0, len(FasDic[key]) - 3 ) :
        if FasDic[key][i] != 'N' :
            continue
        if FasDic[key][i + 1] == 'P' :
            continue
        if FasDic[key][i + 2] != 'S' and FasDic[key][i + 2] != 'T' :
            continue
        if FasDic[key][i + 3] == 'P' :
            continue
        rstlst.append(i+1)
    rstdic[key] = rstlst

    
f3 = open('./rosalind/output.txt', 'w')
for key, value in rstdic.items() :
    if len(value) == 0 :
        continue
    data2 = key
    f3.write(data2)
    f3.write('\n')
    data2 = ' '.join(map(str, value))
    f3.write(data2)
    f3.write('\n')
f3.close()
    