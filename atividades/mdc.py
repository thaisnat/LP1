#coding: utf-8
#calcular o mdc

num1=int(raw_input('informe o valor'))
num2=int(raw_input('informe o valor'))

while num2 != 0:
    mdc = num1 % num2
    num1 = num2
    num2 = mdc

print "o mdc desses dois numeros eh:",num1
