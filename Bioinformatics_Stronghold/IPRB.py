# study more !!
# code from youtube 

import numpy as np
GG = np.array([[0, 0]])
Gg = np.array([[0, 1]])
gg = np.array([[1, 1]])
each_prob = []
each_dominant_fraction = []
sum_probs = []

def probability_dom(k, m, n) :
    input = (k, m, n)
    
    for ii in range(len([k, m, n])) :
        for iii in range(len([k, m, n])) :
            t = k + m + n
            if ii != iii :
                probability = (input[ii] / t) * (input[iii] / (t - 1))
            else :
                probability = (input[ii] / t) * ((input[iii] - 1) / (t - 1))
            each_prob.append(probability)
    print(each_prob)
    print(sum(each_prob))
    
    for iT in [GG, Gg, gg] :
        for i in [GG, Gg, gg] :
            matrix = iT.T * i
            Dominant_fraction = np.sum(matrix == 0) / 4
            each_dominant_fraction.append(Dominant_fraction)
    print(each_dominant_fraction)
    
    for n in range(0, 9) :
        sum_probs.append(each_dominant_fraction[n] * each_prob[n])
    print(sum(sum_probs))
    

probability_dom(27, 18, 21)
