
'''semente = raw_input()
nova_senha = ''

for i in range(len(semente) -2,-1,-2):
	nova_senha += semente[i]
	print nova_senha'''
p1 = raw_input()
p2 = raw_input()

indice = ''
for letra in p2:
   for i in range(len(p1)):
        if letra == p1[i]:
            indice += str(i)
        else:
			indice += '-1'
	print indice
