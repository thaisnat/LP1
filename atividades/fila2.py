# coding: utf-8
# Unidade 6 - Fila por altura
# Thaís Nicoly - UFCG 2015.1 - 13/11/2015

def insere_na_fila(fila, nome, altura):
	fila.append((nome, float(altura)))
	for i in range(len(fila)):
		for o in range (len(fila)-1):
			if fila[o][1] > fila[o + 1][1]:
				fila[o], fila[o + 1] = fila[o + 1], fila[o]
	return fila

fila = [("maria", 1.05), ("joao", 1.09), ("ana", 1.16)]
insere_na_fila(fila, "jose", 1.12)
assert fila == [("maria", 1.05), ("joao", 1.09), ("jose", 1.12), ("ana", 1.16)]
