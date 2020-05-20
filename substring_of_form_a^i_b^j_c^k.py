Created on Wed May 20 10:51:18 2020

@author: interview_CodingSolution
"""

#Input Values
s = "abcabc"

def subStringCount(s):
    n_a = 0
    n_b = 0
    n_c = 0
    for i in s:
        if (i == 'a'):
            n_a = 2*n_a + 1
        elif (i == 'b'):
            n_b = 2*n_b + n_a
        else:
            n_c = 2*n_c + n_b
    print("The total number of valid substrings is "+str(int(n_c)))
