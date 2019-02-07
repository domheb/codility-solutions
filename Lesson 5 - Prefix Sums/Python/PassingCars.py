# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    
    #Useful variables
    result = 0
    length = len(A)
    ones = 0
    
    """ <-- O(N**2), 100% correct
    #Perform operation
    for j in range(0,length):
        if A[j] == 0:
            for i in range (j+1,length):
                if A[i] != 0:
                    result += 1
        else:
            pass
    """
    
    #Perform operation <-- O(N), 100% correct
    for i in range(0,length):
        if A[i] == 1:
            ones += 1        
    for i in range(0,length):
        if A[i] == 0:
            result += ones
            if result > 1000000000: #Additional condition
                return -1
        else:
            ones -= 1
    
    #End the algorithm
    return result
