# coding: utf-8
# Unidade 5 - Autorização voos
# Thaís Nicoly - UFCG 2015.1 - 11/11/2015

t_disponivel = int(raw_input())
qnt_avioes = int(raw_input())

autorizado = 0

while True:
	for i in range(qnt_avioes):
		t_avioes = int(raw_input())
		if t_avioes < t_disponivel:
			autorizado += 1
			t_disponivel = t_disponivel - t_avioes
		elif t_avioes > t_disponivel:
			break
		
print autorizado
