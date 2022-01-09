import random


grafo =	[	[0,1],
			[1,0],[1,0],[1,2],[1,3],[1,2],[1,1],
			[2,0],[2,0],[2,2],[2,3],[2,1],
			[3,0],[3,0],[3,2],[3,3],[3,1],[3,1],[3,4],[3,5],[3,4],[3,5],
			[4,0],[4,0],[4,2],[4,3],[4,1],[4,1],
			[5,0],[5,0],[5,2],[5,3],[5,1],[5,1]
		]



print("\ncalcolando PAGERANK...\n")
"""
-----------------------------------
		FUNZIONI DI SUPPORTO
-----------------------------------
"""
#ritorna la lista dei nodi raggiungibili con un passo da nodo
def get_vicini_uscenti(grafo,nodo):
	return list(map(lambda x: x[1],filter(lambda x: x[0]==nodo , grafo)))


#ritorna la lista dei nodi del grafo che hanno un arco uscente verso nodo
def get_vicini_entranti(grafo,nodo):
	return list(map(lambda x: x[0],filter(lambda x: x[1]==nodo , grafo)))


#ritorna la lista dei nodi del grafo
def get_nodi(grafo):
	lst=[]
	for x in grafo:
		lst.append(x[0])
		lst.append(x[1])

	lst = list(dict.fromkeys(lst))

	return list(map(lambda x: x,lst))


#ritorna il numero degli archi uscenti da nodo
def get_numero_archi_uscenti(nodo):
	return len(list(filter(lambda x: x[0]==nodo , grafo)))



"""
-----------------------------------
			 PAGERANK
-----------------------------------
"""
nodi = get_nodi(grafo)
nr_nodi = len(nodi)

nodi_coppie=[]
l = 0.15

for nodo in nodi:
	lst=[nodo,nr_nodi/l]
	nodi_coppie.append(lst)

nodo=nodi[random.randint(0, nr_nodi-1)]

i=1
while i < 500:
	lista_vicini_entranti = get_vicini_entranti(grafo,nodo)
	pgRank = 0

	for _nodo in lista_vicini_entranti:
		lst=list(filter(lambda x: x[0]==_nodo , nodi_coppie))
		actual_pageRank=lst[0][1]
		pgRank = pgRank + actual_pageRank/get_numero_archi_uscenti(_nodo)

	pgRank=pgRank*(1-l)
	pgRank=pgRank+l/nr_nodi

	for _nodo in nodi_coppie:
		if(_nodo[0]==nodo):
			_nodo[1]=pgRank

	if random.random()<l:
		nodo=nodi[random.randint(0, nr_nodi-1)]
	else:
		vicini = get_vicini_uscenti(grafo,nodo)
		nodo=vicini[random.randint(0, len(vicini)-1)]

	#normalizzazione
	somma_pageRank = sum(list(map(lambda a: a[1], nodi_coppie)))
	nodi_coppie = list(map(lambda a: [a[0],a[1]/somma_pageRank], nodi_coppie))

	i=i+1



print ("   {:<30}|           {:<45}".format('PAGE','PAGERANK'))
print ("------------------------------------------------------------")
for _nodo in nodi_coppie:
	if _nodo[0]==0:
		print ("{:<30}   |      {:<45}".format('index',str(_nodo[1])))
	if _nodo[0]==1:
		print ("{:<30}   |      {:<45}".format('whoIAm',str(_nodo[1])))
	if _nodo[0]==2:
		print ("{:<30}   |      {:<45}".format('activities',str(_nodo[1])))
	if _nodo[0]==3:
		print ("{:<30}   |      {:<45}".format('blog',str(_nodo[1])))
	if _nodo[0]==4:
		print ("{:<30}   |      {:<45}".format('azureBotUnity',str(_nodo[1])))
	if _nodo[0]==5:
		print ("{:<30}   |      {:<45}".format('cognitiveServicesUnity',str(_nodo[1])))


print("\n.\n.\n.\n.\n.\n.\n.\n.\n\ncalcolando HITS...\n")
"""
-----------------------------------
			 HITS
-----------------------------------
"""
nodi = get_nodi(grafo)
nodi_triple=[]

for nodo in nodi:
	lst=[nodo,1,1]
	nodi_triple.append(lst)


i=1
while i < 500:
	authority=0
	hub=0

	#aggiornamento dei valori di authority
	for nodo in nodi_triple:
		nodo[1]=0
		authority=0
		lista_vicini_entranti = get_vicini_entranti(grafo,nodo[0])
		for _nodo in lista_vicini_entranti:
			lst=list(filter(lambda x: x[0]==_nodo , nodi_triple))
			authority=authority+lst[0][2]
		nodo[1]=authority


	#aggiornamento dei valori di hub
	for nodo in nodi_triple:
		nodo[2]=0
		hub=0
		lista_vicini_uscenti = get_vicini_uscenti(grafo,nodo[0])
		for _nodo in lista_vicini_uscenti:
			lst=list(filter(lambda x: x[0]==_nodo , nodi_triple))
			hub=hub+lst[0][1]
		nodo[2]=hub


	#normalizzazione
	somma_authority = sum(list(map(lambda a: a[1], nodi_triple)))
	somma_hub = sum(list(map(lambda a: a[2], nodi_triple)))

	nodi_triple = list(map(lambda a: [a[0],a[1]/somma_authority,a[2]/somma_hub], nodi_triple))

		
	i=i+1



print ("   {:<30}|           {:<43}|           {:<40}".format('PAGE','AUTHORITY','HUB'))
print ("--------------------------------------------------------------------------------------------------------------")
for _nodo in nodi_triple:
	if _nodo[0]==0:
		print ("{:<30}   |      {:<45}   |      {:<45}".format('index',str(_nodo[1]),str(_nodo[2])))
	if _nodo[0]==1:
		print ("{:<30}   |      {:<45}   |      {:<45}".format('whoIAm',str(_nodo[1]),str(_nodo[2])))
	if _nodo[0]==2:
		print ("{:<30}   |      {:<45}   |      {:<45}".format('activities',str(_nodo[1]),str(_nodo[2])))
	if _nodo[0]==3:
		print ("{:<30}   |      {:<45}   |      {:<45}".format('blog',str(_nodo[1]),str(_nodo[2])))
	if _nodo[0]==4:
		print ("{:<30}   |      {:<45}   |      {:<45}".format('azureBotUnity',str(_nodo[1]),str(_nodo[2])))
	if _nodo[0]==5:
		print ("{:<30}   |      {:<45}   |      {:<45}".format('cognitiveServicesUnity',str(_nodo[1]),str(_nodo[2])))
