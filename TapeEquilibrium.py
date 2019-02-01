"""
Written using Python 3.6
Compiled on Linux Manjaro 18
"""
def solution(A):
    
    #Create useful variables
    max_value = 999999
    left = 0
    right = 0
    length = len(A)
    
    #Perform operation
    for i in range(0, length):  #Sum all elements
        right += A[i]
    for i in range(0, length-1):
        left += A[i]    #Value of the sum(1..i)elements
        right -= A[i]   #Value of the sum(1..N)elements - i
        temp = left - right
        if temp < 0:
            temp = -temp
        if max_value > temp:
            max_value = temp
            
    return max_value
