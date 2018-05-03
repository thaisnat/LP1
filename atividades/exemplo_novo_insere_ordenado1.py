# coding: utf-8

# tem efeito colateral -> altera a lista
# [9,1,3,11,15,18,21]

def insere_ordenado_primeiro(lista):
    for i in range(len(lista)-1):
        if lista[i] > lista[i+1]:
            lista[i],lista[i+1] = lista[i+1],lista[i]
        else:
            break

