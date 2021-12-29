#  https://rosalind.info/problems/tree/
#
#  Given: A positive integer n (n≤1000) and an adjacency list corresponding to a graph on n nodes that contains no cycles.
#  
#  Return: The minimum number of edges that can be added to the graph to produce a tree.

def read_file(filepath) :
    with open(filepath, 'r') as f :
        return [l.strip() for l in f.readlines()]
    
file = read_file('./rosalind/rosalind_tree.txt')
lst = []
for line in file :
    lst.append(line)

edge = int(lst.pop(0)) - len(lst) - 1 

print(edge)