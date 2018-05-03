# coding: utf-8
# Unidade 7 - selection sort
# Thaís Nicoly - UFCG 2015.2 - 21/04/2016

def selection_sort(lista):
    for i in range(len(lista)):
        pos_menor = i
        for j in range(i, len(lista)):
            if lista[j] < lista[pos_menor]:
                pos_menor = j
        lista[i],lista[pos_menor] = lista[pos_menor], lista[i]
l = [5,2,3,4,6,9,0]
print l
selection_sort(l)
print l
assert l == [0,2,3,4,5,6,9]
