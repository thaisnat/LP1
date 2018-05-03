# coding: utf-8
# Unidade 7 - Meu Posto
# Thaís Nicoly - UFCG 2015.2 - 20/04/2016

while True:
	entrada = raw_input()
	if entrada == 'finalizar' : break
	
	if entrada == 'cadastrar':
		n_cpf = int(raw_input())
		nome = raw_input()
		posto = raw_input()
		saldo = 300
		usuario.append(nome)
		usuario.append(n_cpf)
		usuario.append(posto)
		usuario.append(saldo)
		print 'Usuário cadastrado com sucesso.'
	
	if 


'''
1) Cadastrar novo consumidor.
O cadastro deve constar de nome, CPF, e posto preferido. 
Um novo consumidor ganha 300 pontos.
Caso o CPF já exista no cadastro, deve ser informada a mensagem: 
"Usuário já existente." e o cadastro não deve ser efetivado.
Caso contrário, deve ser feito o cadastro e informado: "Usuário cadastrado com sucesso.".
 Para realizar esta operação o usuário deve digitar "cadastrar".'''

'''
2) Atualizar pontos.
O usuário deve informar o CPF do consumidor e o posto onde foi realizado o abastecimento. 
Se for no posto cadastrado como preferido, ele ganha 200 pontos. 
Se não for no posto preferido, ganha 100 pontos.
caso o usuário não exista, deve ser informada a mensagem: "Usuário inexistente."
caso contrário: "Usuário atualizado com sucesso.".
Para realizar esta operação o usuário deve digitar "atualizar".'''

'''
3) Consultar pontos.
O usuário deve informar o CPF do consumidor e exibir as informações conforme o exemplo de saída abaixo.
Caso o usuário não exista, 
deve ser informada a mensagem: "Usuário inexistente.".
Para realizar esta operação o usuário deve digitar "consultar".
'''

'''
O programa acaba quando o usuário informa "finalizar".
'''
