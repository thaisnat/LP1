# coding: utf-8
# Unidade 6 - Fila por altura
# Thaís Nicoly - UFCG 2015.2 - 16/04/2016

def insere_na_fila(fila, nome, altura):
	fila.append((nome, float(altura)))
	for i in range(len(fila)):
		for o in range (len(fila)-1):
			if fila[o][1] > fila[o + 1][1]:
				fila[o], fila[o + 1] = fila[o + 1], fila[o]
	return fila
