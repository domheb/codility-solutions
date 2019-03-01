def element_occurence(S, A, C, G, T):
    for i in range(0, len(S)):
        if S[i] == 'A':
            A[i+1] = i
            C[i+1] = C[i]
            G[i+1] = G[i]
            T[i+1] = T[i]
        elif S[i] == 'C':
            A[i+1] = A[i]
            C[i+1] = i
            G[i+1] = G[i]
            T[i+1] = T[i]
        elif S[i] == 'G':
            A[i+1] = A[i]
            C[i+1] = C[i]
            G[i+1] = i
            T[i+1] = T[i]
        else:
            A[i+1] = A[i]
            C[i+1] = C[i]
            G[i+1] = G[i]
            T[i+1] = i

def solution(S, P, Q):
    
    A = [-1] * (len(S) + 1)
    C = [-1] * (len(S) + 1)
    G = [-1] * (len(S) + 1)
    T = [-1] * (len(S) + 1)
    
    element_occurence(S, A, C, G, T)

    Result = []
    
    for i in range(len(P)):
        if A[Q[i]+1] >= P[i]:
            Result.append(1)
            continue
        elif C[Q[i]+1] >= P[i]:
            Result.append(2)
            continue
        elif G[Q[i]+1] >= P[i]:
            Result.append(3)
            continue
        else:
            Result.append(4)
            continue
    
    return Result
