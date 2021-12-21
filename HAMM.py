SeqA = list("")
SeqB = list("")
count = 0
for i in SeqA :
    if i == SeqB.pop(0) :
        continue
    else :
        count += 1
    
print(count)
