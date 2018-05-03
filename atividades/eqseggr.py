#equação do 2° grau
a=(int(raw_input('insira o numero da variavel a', )))
b=(int(raw_input('insira o numero da variavel b', )))
c=(int(raw_input('insira o numero da variavel c', )))

delta=(b**2)-4*a*c

if a==0 :
    print('essa equação não é do 2° grau')
elif a!=0 and delta >=0:
    print('Essa equação é do 2° grau')
    raiz=delta**(1/2)
    x1 =int((-b+raiz)/2*a)
    print ('as raizes sao:')
    print x1
    x2 =int((-b-raiz)/2*a)
    print x2
if delta <=0:
    print('Essa equação é o do 2° grau, porem não tem raizes reais')


