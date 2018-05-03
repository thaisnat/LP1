# coding: utf-8
# Unidade 5 - Tiro ao Alvo
# Thaís Nicoly - UFCG 2015.2 - 14/04/2015
import math 

cont,soma_media,media_total = 0,0.0,0.0
media = []
tem = True

while True:
	x,y = raw_input().split(', ')
	
	d = math.sqrt(float(x)**2 + float(y)**2)
	
	if d > 200:
		break
	cont += 1	
	media.append(d)

for i in range(len(media)):
	soma_media += float(media[i])
	
if len(media) >= 1:
	media_total = soma_media/float(len(media))
else:
	tem = False
	print '--'
	print 'num disparos: %d' % cont
	print 'distancia media: %.2f' % media_total
	

for elem in media:
	print '%.2f' % float(elem)

if tem:
	print '--'
	print 'num disparos: %d' % cont
	print 'distancia media: %.2f' % media_total
