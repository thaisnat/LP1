# coding: utf-8
# Unidade 7 - Lista Presença
# Thaís Nicoly - UFCG 2015.2 - 20/04/2016

def cria_lista_presenca(turmas, nomes, turma):
	nome_alunos = []
	for i in range(len(turmas)):
		if turma == turmas[i]:
			nome_alunos.append(nomes[i])
	
	return nome_alunos

