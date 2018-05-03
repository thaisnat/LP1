# Mostrar o nome em forma de escada crescente
nome=(raw_input('informe seu nome'))

for x in range (len(nome)+1):
    print (nome[:x])
