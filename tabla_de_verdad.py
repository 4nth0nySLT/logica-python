import time
def tabla(numero):
	ini=time.time()
	total=2**numero
	print("Posibilidades:",total)
	memoria=total
	matriz=[]
	matriz2=[]
	for z in range(1,numero+1):
		ceros=memoria/2
		veces=total/ceros
		contador=0
		for index in range(int(veces)):
			for _ in range(int(ceros)):
				matriz.append(int( index%2))
			valor=int( index%2)
		contador=contador+1
		memoria=memoria/2
	for index in range(0,total):
		matriz2.append([])
		matriz2[index].append(matriz[index])
		base=index
		for veces in range(numero-1):
			base=base+total
			matriz2[index].append(matriz[base])
		#print(matriz2[index],(index/total)*100,"%",end='             \r')
	print("")
	print("--------------------------100%--------------------------")
	print(time.time()-ini,"seg")
	return matriz2

import numpy as np
def tabla_version2 (numero):
	ini=time.time()
	total=2**numero
	print("Posibilidades:",total)
	memoria=total
	matriz=[]
	matriz2=[]
	for z in range(1,numero+1):
		ceros=memoria/2
		veces=total/ceros
		for index in range(int(veces)):
			for _ in range(int(ceros)):
				matriz.append(bool( index%2))
		memoria=memoria/2
	for index in range(0,int(total/2)):
		matriz2.append([])
		matriz2[index].append(matriz[index])
		base=index
		for veces in range(numero-1):
			base=base+total
			matriz2[index].append(matriz[base])
		#print(matriz2[index],(index/total)*100,"%",end='             \r')
	print("")
	print("--------------------------100%--------------------------")
	matriz2+=np.logical_not(matriz2).tolist()
	print(time.time()-ini,"seg")
	return matriz2

def tabla_bruta (numero):
	ini=time.time()
	total=2**numero
	print("Posibilidades:",total)
	memoria=total
	matriz=[]
	for z in range(1,numero+1):
		ceros=memoria/2
		veces=total/ceros
		for index in range(int(veces)):
			for _ in range(int(ceros)):
				matriz.append(bool( index%2))
			#print(valor,(index/total)*100,"%",end='             \r')
		memoria=memoria/2
	print(time.time()-ini,"seg")
	return matriz

def tabla_bruta_version2 (numero):
	ini=time.time()
	total=2**numero
	print("Posibilidades:",total)
	memoria=total
	matriz=[]
	for z in range(1,numero+1):
		ceros=memoria/2
		veces=total/ceros
		for index in range(int(veces)):
			valor=int( index%2)
			matriz+=[valor]*int(ceros)
			#print(valor,(index/total)*100,"%",end='             \r')
		memoria=memoria/2
	print(time.time()-ini,"seg")
	return matriz

def tabla_version3 (numero):
	ini=time.time()
	total=2**numero
	matriz2=[]
	matriz=tabla_bruta(numero)
	for index in range(0,int(total/2)):
		matriz2.append([])
		matriz2[index].append(matriz[index])
		base=index
		for veces in range(numero-1):
			base=base+total
			matriz2[index].append(matriz[base])
		#print(matriz2[index],(index/total)*100,"%",end='             \r')
	print("")
	print("--------------------------100%--------------------------")
	matriz2+=np.logical_not(matriz2).tolist()
	print(time.time()-ini,"seg")
	return matriz2

def tabla_version4 (numero):
	ini=time.time()
	total=2**numero
	matriz2=[]
	matriz=tabla_bruta_version2(numero)
	for index in range(0,int(total/2)):
		matriz2.append([])
		matriz2[index].append(matriz[index])
		base=index
		for veces in range(numero-1):
			base=base+total
			matriz2[index].append(matriz[base])
		#print(matriz2[index],(index/total)*100,"%",end='             \r')
	print("")
	print("--------------------------100%--------------------------")
	matriz2+=np.logical_not(matriz2).tolist()
	print(time.time()-ini,"seg")
	return matriz2


def getValores(numero,indice):
	ini=time.time()
	# ERROR ON getValores(20,29392)
	# Falla cuando cuadrado>8, falta establecer una constante
	total=2**numero
	if indice>total:
		return
	cuadrados=[(2**cuadrado)/2 for cuadrado in range(1,numero+1)][::-1]
	resultado=[]
	for cuadrado in cuadrados:
		if cuadrado==1:
			resultado.append(int(not indice%2))
		#elif cuadrados.index(cuadrado)==0:
		elif cuadrado==indice:
			resultado.append(0)
		#else:
		#	print(int(indice//cuadrado))
		#elif indice*2==cuadrado:
		#	resultado.append(1)
		elif indice==total:
			resultado.append(1)
		elif cuadrado==2:
			resultado.append(int(not(int((indice/cuadrado)+0.5))%2))
		elif cuadrado==4:
			valor=round((indice/cuadrado)+0.325)%2
			resultado.append(int(not valor))
		elif cuadrado==8:
			valor=round((indice/cuadrado)+0.425)%2
			resultado.append(int(not valor))
		elif cuadrado%2==1:
			resultado.append(not (int((indice/cuadrado)+0.5))%2)
		else:
			resultado.append(int((indice//cuadrado)%2))
		#print(indice,cuadrado)
	print(time.time()-ini,"seg")
	print(resultado)
	return resultado

def bin(cuadrado,indice):
	minimo=int(indice/cuadrado)
	if minimo+1==indice:
		minimo=int(indice-1/cuadrado)
	return minimo%2
	#return int(indice/cuadrado)%2 if indice!=int(indice/cuadrado)+1 else int(indice-1/cuadrado)%2

def getValores(numero,indice):
	if indice>2**numero:
		return
	cuadrados=[(2**cuadrado)/2 for cuadrado in range(1,numero+1)][::-1]
	return [bin(cuadrado,indice-1) for cuadrado in cuadrados]

getValores_unalinea=lambda numero,indice: [int((indice-1)/cuadrado)%2 if (indice-1)!=int((indice-1)/cuadrado)+1 else int((indice-1)-1/cuadrado)%2  for cuadrado in [(2**cuadrado)/2 for cuadrado in range(1,numero+1)][::-1]] 


