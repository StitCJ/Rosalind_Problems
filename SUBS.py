seq = ""
mtf = ""
rcd = []

for i in range(len(seq) - len(mtf) + 1) :
    if seq[i: i + len(mtf)] == mtf :
        rcd.append(i + 1)

rst = ' '.join(str(n) for n in rcd)
print(rst)
