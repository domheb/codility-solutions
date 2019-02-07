"""
Written using Python 3.6
"""
def solution(A):

	#Create useful utilities
    s1 = set()  #Looking for element in set is
                #way faster then in list

	#Perform operation
    for i in range(0,len(A)):
        if (not A[i] in s1): #first element of pair - add it
            s1.add(A[i])
            continue
        if (A[i] in s1):	#second element of pair - remove it
            s1.remove(A[i])
    exp_value = list(s1) #if there is odd number of elements,
                         #there will always be one left
    
    return(exp_value[0])
