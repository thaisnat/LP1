# coding: utf-8
# Unidade 6 - Insere Ordenado - feito em sala
# Thaís Nicoly - UFCG 2015.2 - 21/04/2016

# tem efeito colateral -> altera a lista
# [9,1,3,11,15,18,21]

def insere_ordenado_primeiro(lista):
    for i in range(len(lista)-1):
        if lista[i] > lista[i+1]:
            lista[i],lista[i+1] = lista[i+1],lista[i]
        else:
            break

