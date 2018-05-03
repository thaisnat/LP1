# coding: utf-8
# Unidade 4 - Conversão de Matrículas na UFCG
# Thaís Nicoly - UFCG 2015.2 - 18/03/2016

matricula = raw_input()

nova_matricula = '1'

for i in range(1,len(matricula)):
	if i == 5:
		nova_matricula = nova_matricula + '0' + matricula[i]
	else:
		nova_matricula += matricula[i]
	
print nova_matricula
