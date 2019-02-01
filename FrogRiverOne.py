"""
Written using Python 3.6
Compiled on Linux Manjaro 18
"""

def solution(X, A):
    
    #Create useful variables
    all_points = set(A)
    minimal_way = list(all_points)
    road = set() #frog's path
    
    #Perform operation
    left = sum([i for i in range(0,X+1)])
    right = sum([minimal_way[i] for i in range(0,len(minimal_way))])
    if (left != right): return -1 #frog is never able to jump
    for i in range(0,len(A)):
        road.add(A[i])
        if (all_points <= road): return i #the fastest way
