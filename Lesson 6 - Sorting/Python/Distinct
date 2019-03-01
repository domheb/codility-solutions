# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
     # write your code in Python 3.6
    
    if not A:
        return 0
    
    minimum = min(A)
    maximum = max(A)
    #rangeL = maximum - minimum
    #print(rangeL)
    
    if min(A) >= 0:
        L = [0] * (maximum + 1)
    
        for i in range(len(A)):
            L[A[i]] += 1
        
        counter = 0
        for i in range(len(L)):
            if L[i] != 0:
                counter += 1
        
        return counter
    else:
        minimum *= -1
        L = [0] * (maximum + 1 + minimum)
        
        for i in range(len(A)):
            L[A[i] + minimum] += 1
        
        counter = 0
        for i in range(len(L)):
            if L[i] != 0:
                counter += 1
        
        return counter
