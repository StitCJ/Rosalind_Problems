#  https://rosalind.info/problems/rstr/
#  Given: A positive integer N≤100000, a number x between 0 and 1, and a DNA string s of length at most 10 bp.
#  
#  Return: The probability that if N random DNA strings having the same length as s are constructed with GC-content x (see “Introduction to Random Strings”), then at least one of the strings equals s. We allow for the same random string to be created more than once.
import numpy as np
import matplotlib.pyplot as plt
from math import factorial

def bin_dist(k, n, p):
    nck = factorial(n) / (factorial(k) * factorial(n - k))
    pd = nck * p**k * (1-p)**(n-k)
    return pd



N = 87829
x = 0.431590
s = "TGCAAGATAC"
trial = N - len(s) + 1
prb = x/2
nctd = {"A" : (1-x)/2, "T" : (1-x)/2, "G" : prb, "C" : prb}

prob = 1
for i in s :
    prob = prob * nctd[i]


rst = round(1 - bin_dist(0,trial,prob), 3)

print(rst)