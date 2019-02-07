"""
Written using Python 3.6
Compiled on Linux Manjaro 18
"""
def solution(A):
    
    #Create useful variables
    l = len(A)
    s = set(A)
    A = list(s)
    l2 = len(A)
    s_temp = set()
    
    #Check possibilities
    if l != l2:
        return 0

    #Perform operation
    for i in range(1,l+1):
        s_temp.add(i)
    if not (s_temp - s):
        return 1
    else:
        return 0
