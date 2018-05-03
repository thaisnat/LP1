# coding: utf-8
# Unidade 6 - Maioridade Penal Função
# Thaís Nicoly - UFCG 2015.2 - 21/04/2016


def maioridade_penal(nomes,idades):
	names = nomes.split()
	ages = idades.split()
	for i in range(len(ages)-1,-1,-1):
		if int(ages[i]) < 18:
			names.pop(i)
	
	
			
nomes = "Jansen Italo Ana"
idades = "14 21 60"
print maioridade_penal(nomes,idades)
assert maioridade_penal("Jansen Italo Ana","14 21 60") == "Italo Ana"
