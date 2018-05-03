# coding: utf-8
# Unidade 4 - Nome Maluco (Questão do Miniteste)
# Thaís Nicoly - UFCG 2015.1 - realizado dia 29/05/2015

''' 
O programa deseja que voce crie uma nova senha, a partir de uma que sera fornecida pelo usuario
as modificações são em tres etapas
-> na primeira voce irá percorrer de tras pra frente a palavra sempre pulando uma casa, mas começando da primeira(que é a ultima[-1])
-> na segunda, voce irá percorrer da mesma forma, porém irá comecar da segunda(que é a penultima[-2])
< sim ! e sempre armazenando, porque voce irá fazer uma outra string, e nao modificar a original >
na terceira etapa, voce irá adicionar primeiro a ultima letra da palavra de origem, e em seguida a primeira letra
'''
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
'''OBSERVAÇÃO !
Quando for na primeira etapa voce ira percorrer apenas os indices pares,
e na segunda etapa, os indices impares,
então, se precisar percorrer em outra questão dessa mesma forma, poderá utilizar o mesmo estilo do comando for.
'''
