def criar_matriz_zeros(l,c):
    matriz = [0]*l
    for i in range(0,l):
        matriz[i] = [0]*c
    return matriz


def transposta(M):
    B = criar_matriz_zeros(len(M[0]), len(M))
    for i in range(0,len(M)):
        for j in range(0,len(M[0])):
            B[j][i] = M[i][j]
    return B
 
M = [[1,1,1,1], [2,2,2,2], [3,3,3,3]]
assert transposta(M) == [[1,2,3], [1,2,3], [1,2,3], [1,2,3]]
assert M == [[1,1,1,1], [2,2,2,2], [3,3,3,3]]
