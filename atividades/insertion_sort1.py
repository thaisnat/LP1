# coding: utf-8
# Insertion sort

# [2,5,6,9,11,3]
'''
for j in range(len(l)-1,0,-1):
    if l[j] < l[j-1]:
        l[j],l[j-1] = l[j-1],l[j] # -> aux = l[j-1], l[j-1] = l[j], l[j] = aux
    else:
        return 
    
# ---
# tem efeito colateral -> altera a lista
#[3,1,6,7,2,-3,8] -> vai fazendo por partes
#-> [1,3,6,7,2,-3,8] -> [ 1,2,3,6,7,-3,] -> [-3,1,2,3,6,7,8]

def insertion_sort(lista):
    for i in range(len(1,len(lista)):
        for j in range(i,0,-1):
            if lista[j] < lista[j-1]:
                lista[j],lista[j-1] = lista[j-1],lista[j]
            else:
                break
'''
# trocando for por while no exemplo de cima

def insertion_sort(lista):
    for i in range(len(1,len(lista)):
        j = i          
        while True:
        if j > 0 and lista[j] < lista[j-1]:
            lista[j],lista[j-1] = lista[j-1],lista[j]
            j -= 1
        else:
            break
    print lista
lista = [6,3,7,9,1,0]
insertion_sort(lista)



               
               
        
