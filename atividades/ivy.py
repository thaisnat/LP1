#coding: utf-8
#Ivyna Alves/Programção 1/UFCG 2015.1/Soma simétricos
 
def soma_simetricos(valores):
	soma = []
	if len(valores) % 2 == 0:
 
		for i in range((len(valores)/2)):
			conta = valores[i] + valores[len(valores)-1-i]
			soma.append(conta)
	else:
		for i in range((len(valores)/2)+1):
			if i == len(valores)-i-1:
				soma.append(valores[i])
				break
			conta = valores[i] + valores[len(valores)-1-i]
			soma.append(conta)
 
 
	return soma

#assert soma_simetricos([2, 5, 3, 9]) == [11, 8]
#assert soma_simetricos([2, 5, 3, 9, 4]) == [6, 14, 3]
