# coding: utf-8
# Unidade 4 - Conta caracteres inversa
# Thaís Nicoly - UFCG 2015.1 - 15/06/2015

palavra = raw_input()
coincidentes = 0
palavra_invertida =''

for i in range(len(palavra)-1,-1,-1):
	palavra_invertida += palavra[i]
for j in range(len(palavra)):
	if palavra[j] == palavra_invertida[j]:
		coincidentes += 1

print 'A palavra %s contém %d caractere(s) coincidente(s) com a sua inversa.' % (palavra,coincidentes)
