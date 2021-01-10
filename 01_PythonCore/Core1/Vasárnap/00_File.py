#!/usr/bin/pythonw python3

forrasfajl = open('sorok.txt', 'r')
# (r)ead, (w)rite, (a)ppend

lista = forrasfajl.readlines()
masiklista = []

for elem in lista:
	masiklista.append(elem.strip())

celfajl = open('kiiras.txt', 'w')
for sor in masiklista:
	print(sor, file=celfajl)
celfajl.close()