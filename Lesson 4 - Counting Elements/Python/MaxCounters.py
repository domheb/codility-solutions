"""
Written using Python 3.6
Compiled on Linux Manjaro 18
"""
def solution(N, A):
    
    #Create useful variables
    Array = [0] * N
    max_val = 0
    length = len(A)
    limit = N+1
    
    #Perform operation
    for i in A:
        if (i != limit):
            Array[i-1] += 1
            if max_val < Array[i-1]:
                max_val = Array[i-1]
        else:
            Array = [max_val] * N

    return Array
