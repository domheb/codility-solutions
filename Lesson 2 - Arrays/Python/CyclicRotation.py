"""
Written using Python 3.6
Compiled on Linux Manjaro 18
"""

def solution(A, K):
    
    #Create useful variables
    length = len(A)
    
    #Check additional conditions:
    if length < 0 or length > 100: #N out of range
        return -1
    if not A:   #A is empty
        return A
    if length == 1: #A has 1 element
        return A
    for i in range(0,length):
        if A[i] < -1000 or A[i] > 1000: #element out of range
            return -1
    if K < 0 or K > 100: #K out of range
        return -1
    if K == 0: #K is equal 0
        return A
    if K == length: #K is equal N; no rotation
        return A
    if K > length: #K is bigger than N, it's full rot + rest
        K = K % length
    left = length - K #K is smaller then N

    #Perform operation
    NewA = [] 
    for i in range(left,length): #Those elements should be at the beginning
        NewA.append(A[i])
    for i in range(0, left): #Those elements should be later
        NewA.append(A[i])

    #End the algorithm
    return NewA
