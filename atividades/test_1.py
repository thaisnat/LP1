# coding: utf-8
# Teste 

valores = [3, 7, 11, 9, 5]
indices2 = [2, 4, 9, 0]
nova_seq = [] 
guarda_elem = []

for elem in indices2:
    for i in range(len(valores)):
	    if i == elem:
			guarda_elem.append(elem)
print guarda_elem 
for x in indices2:
	for z in guarda_elem:
		if x in guarda_elem:
			nova_seq.append(valores[z])
		else:
			nova_seq.append('None')
print nova_seq
	     
