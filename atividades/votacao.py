# coding: utf-8
# Unidade 6 - Analytics Votação
# Thaís Nicoly - UFCG 2015.1 - 13/11/2015

def conta_votos(votacoes,id_prop):
	qnt_sim = 0
	qnt_nao = 0
	
	for voto in votacoes:
		tokens = voto.split(',')
		
		if int(tokens[1]) == id_prop:
			if tokens[-1] == 'sim':
				qnt_sim += 1
			else:
				qnt_nao += 1
	votos = []
	votos.append(qnt_sim)
	votos.append(qnt_nao)

	return votos

votacao = []
votacao.append('lei sobre bancos,543,joao,PPPP,sim')
votacao.append('lei sobre bancos,543,marina,PPPP,nao')
votacao.append('lei maria da penha,5,joao,PPPP,sim')
votacao.append('lei sobre bancos,543,julio,P,nao')
votacao.append('lei sobre bancos,543,carlos,PBBBB,sim')
votacao.append('lei sobre bancos,543,juliana,PP,sim')
votacao.append('lei das brs,99,joao,PPPP,sim')

assert conta_votos(votacao, 543) == [3,2]
		
