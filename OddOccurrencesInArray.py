"""
Written using Python 3.6
Compiled on Linux Manjaro 18
"""

def solution(A):
    s1 = set()  #looking for element in set is
                #way faster then in list

    for i in range(0,len(A)):
        if (not A[i] in s1):
            s1.add(A[i])
            continue
        if (A[i] in s1):
            s1.remove(A[i])

    exp_value = list(s1) #if there is odd number of elements,
                         #there will always be one left
    
    return(exp_value[0])
    
print(solution([9, 3, 9, 3, 9, 7, 9]))
