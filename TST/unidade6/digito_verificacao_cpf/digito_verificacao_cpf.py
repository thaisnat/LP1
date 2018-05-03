# coding: utf-8
# Unidade 6 - Dígitos de Verificação do CPF
# Thaís Nicoly - UFCG 2015.2 - 21/04/2016


def calcula_digitos_verificacao(n_cpf):
	# para o calculo do 1° digito
	n_digito = 0
	operador = 2
	for i in range(len(n_cpf)-1,-1,-1):
		digito = int(n_cpf[i]) * operador
		n_digito += digito 
		operador += 1
	n_digito = (n_digito*10) % 11
	
	if n_digito == 10:
		n_digito = 0
	
	# para o calculo do 2° digito
	nv_digito = 0
	n_cpf = str(n_cpf) + str(n_digito)
	operador = 2
	for i in range(len(n_cpf)-1,-1,-1):
		digito = int(n_cpf[i]) * operador
		nv_digito += digito 
		operador += 1
	nv_digito = (nv_digito*10) % 11
	
	if nv_digito == 10:
		n_digito = 0
	
	return '%s%s' % (n_digito,nv_digito)
