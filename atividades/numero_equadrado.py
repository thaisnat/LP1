# coding: utf-8
# mostrar o numero e o seu quadrado

n1=int(raw_input('informe o valor do 1° numero'))
n2=int(raw_input('informe o valor do 2° numero'))

if n1 > n2:
    print('--')
else:
    for i in range (n1,n2+1):
        print(i,i*i)
