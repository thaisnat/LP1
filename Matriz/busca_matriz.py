def busca_matriz(matriz,elem):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] == elem:
                return i,j
            
    return None

matriz = [[2, 3, 5, 3, 1],[3, 2, 1, 5, 6],[1, 2, 3, 2, 1]]

print busca_matriz(matriz, 1)
assert busca_matriz(matriz, 4) == None
assert busca_matriz(matriz, 3) == (0,1)
assert busca_matriz(matriz, 1) == (0,4)
