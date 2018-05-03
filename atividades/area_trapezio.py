#coding: utf-8
#Calcular a area de um trapezio

basema=int(raw_input('informe o valor da base maior'))
baseme=int(raw_input('informe o valor da base menor'))
altura=int(raw_input('informe o valor da altura'))

area=altura*(basema+baseme)/2

print 'o trapezio possui a base maior igual a %d, a base menor igual a %d e sua altura eh %d, com isso, a area desse trapezio eh %d' % (basema,baseme,altura,area)
