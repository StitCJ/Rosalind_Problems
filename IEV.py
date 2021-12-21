import numpy as np
GG = np.array([[0, 0]])
Gg = np.array([[0, 1]])
gg = np.array([[1, 1]])


def offspring(a, b, c, d, e, f) :
    input = [a, b, c, d, e, f]
    probability = []
    rst = 0
    for i in [GG, Gg, gg] :
        matrix = GG.T * i
        probability.append(np.sum(matrix == 0) / 4)

    for i in (Gg, gg) :
        matrix = Gg.T * i
        probability.append(np.sum(matrix == 0) / 4)
    
    matrix = gg.T * gg
    probability.append(np.sum(matrix == 0) / 4)

    for i in range(0, 6) :
        rst += 2 * input.pop(0) * probability[i]
        
    return rst

print(offspring(16857, 18068, 18649, 18811, 19150, 19505))
    

            
    