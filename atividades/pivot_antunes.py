# coding: utf-8

lista = [6,4,8,1,7,3]
pivot = 0
	
for i in range(len(lista)-1,-1,-1):
	if lista[i] > lista[pivot]:
		lista.append(lista.pop(i))
	
for i in range(1, len(lista)):
	if lista[i] < lista[pivot]:
		guarda = lista[i]
		lista[i] = lista[pivot]
		lista[pivot] = guarda
		pivot = i
	
print lista
