# coding: utf-8
# Unidade 4 - Nome Maluco (Questão do Miniteste)
# Thaís Nicoly - UFCG 2015.1 - realizado dia 29/05/2015

semente = raw_input()

# Primeira etapa
nova_senha = ''
for i in range(len(semente) -1,-1,-2):
	nova_senha += semente[i]

# Segunda etapa
for i in range(len(semente) -2,-1,-2):
	nova_senha += semente[i]

# Terceira etapa
nova_senha += semente[-1]
nova_senha += semente[0]

print nova_senha
 
