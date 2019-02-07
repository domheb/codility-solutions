"""
Written using Python 3.6
Compiled on Linux Manjaro 18
"""
def solution(A):
    
    #Check possibilities:
    if not A: #A is empty
        return 1
    
    #Create useful variables
    s = set(A)
    A = list(s) #Rotating to set and back to list sorts elements
    max = A[-1] #Get maximal value
    length = len(A)
    sequence_sum = 0
    a_sum = 0
    counter = 0
    
    #Check possibilities again:
    if length < 0 or length > 100000: #N is not in range
        return -1
    for i in range(0,length):
        if not isinstance(A[i],int): #Elements of A are not integers
            return -1
        if (A[i] < 1) or (A[i] > length+1): #Elements of A are not in range
            return -1
    if length == 1:
        if A[0] == 1:
            return A[0] + 1
    
    #Perform operation
    for i in range(0,length):
        sequence_sum += i+1
        a_sum += A[i]
        if a_sum != sequence_sum:
            return A[i]-1
    return A[i]+1
