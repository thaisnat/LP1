# coding: utf-8
# Unidade 4 - Fatorial
# Thaís Nicoly - UFCG 2015.2- 28/03/2015

numero = int(raw_input())
resultado = 1

for x in range(1,numero+1):
    resultado = x * resultado

print '%s' % resultado
