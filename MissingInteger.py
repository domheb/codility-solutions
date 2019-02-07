"""
Written using Python 3.6
Compiled on Linux Manjaro 18
"""
def solution(A):
    
    #Create useful variables
    s = set(A)
    length = len(A)
    
    
    #Check possibilities:
    neg_L = [A[i] for i in range(0,length) if A[i] < 0]
    if len(neg_L) == length: #Case 1: All elements are negative
        return(1)
    A = list(s - set(neg_L))  #Removing negative values
    if not (A): #Case 2: N == 0, so returns error
        return -1
    if length == 1: #Case 3: 1 element only
        if A[0] == 1:
            return 2 #Case 3.1: element == 1
        else:
            return 1 #Case 3.2: element > 1
            
    #Perform standard operation
    normal_series = [i for i in range(1,length+1)]
    if sum(A) == sum(normal_series): 
        return max(A)+1 #Case 4.1: list is complete
    else:
        return list(set(normal_series) - s)[0] #Case 4.2: list is incomplete
