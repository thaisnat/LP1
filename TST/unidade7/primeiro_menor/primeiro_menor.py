# coding: utf-8
# Unidade 7 - Primeiro Menor
# Thaís Nicoly - UFCG 2015.2 - 20/04/2016

def primeiro_menor(num, numeros):
	i = 0
	while int(numeros[i]) > num:
		i += 1
		valor = i
	if int(numeros[i]) == num:
	    return -1
	else:
	    return valor

def main():
	numeros = raw_input()
	numero = numeros.split()
	num = int(raw_input())
	resultado = primeiro_menor(num, numero)
	if int(resultado) <= num:
		print 'sem menores que %d' % num
	else:
		print 'primeiro menor que %d: %s' % (num,numero[resultado])
				

if __name__ == '__main__':
    main()
