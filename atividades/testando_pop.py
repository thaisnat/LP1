# coding: utf-8
# Unidade 6 - Testando a função pop()
# Thaís Nicoly - UFCG 2015.2 - 21/04/2016


def testando(nomes,idades):
	for i in range(len(idades)-1,-1,-1):
		if idades[i] < 18:
			nomes.pop(i)
	return nomes

nomes = ['Jorge', 'Carlos', 'Carla','Bianca']
idades = [24,12,45,13]

print testando(nomes,idades)
