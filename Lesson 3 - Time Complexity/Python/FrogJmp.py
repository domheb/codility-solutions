"""
Written using Python 3.6
Compiled on Linux Manjaro 18
"""
def solution(X, Y, D):
    
    #Check possibilities
    if ((X < 1) or (Y < 1) or (D < 1) or
    (X > 1000000000) or (Y > 1000000000) or
    (D > 1000000000)):
        return -1
    if (X > Y): #X is bigger then Y
        return -1
    
    #Perform operation
    jumps = (Y - X) // D
    if ((Y - X) % D): #if there is a rest, it means +1 jump
        jumps+=1
    
    #End the algorithm
    return jumps
