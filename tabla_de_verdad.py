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
	print(time.time()-ini,"seg","creando la tabla bruta")
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
	print(time.time()-ini,"seg","creando la tabla bruta")
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
	return [bin(cuadrado,indice) for cuadrado in cuadrados]

def getValores_version2(numero,indice,restas=[]):
	cuadrados=[(2**cuadrado)/2 for cuadrado in range(1,numero+1)][::-1]
	return [1 if (indice-sum(restas)>=cuadrados[i] and restas.append(cuadrados[i])==None)  else 0 for i in range(len(cuadrados))] if restas.clear()==None else "xd"
	#return [1 if cuadrados[i+1]<=( ( indice-sum(restas) if (indice-sum(restas)>=cuadrados[i] and restas.append(cuadrados[i])==None and print(restas,indice,indice-sum(restas),i)==None) else indice) if i!=0 else indice) else 0 for i in range(len(cuadrados))]


getValores_unalinea=lambda numero,indice: [int((indice)/cuadrado)%2 if (indice)!=int((indice)/cuadrado)+1 else int((indice)-1/cuadrado)%2  for cuadrado in [(2**cuadrado)/2 for cuadrado in range(1,numero+1)][::-1]] 



getValores_unalinea_version2=lambda numero,indice,restas=[]: [1 if (indice-sum(restas)>=cuadrado and restas.append(cuadrado)==None) else 0 for cuadrado in [(2**cuadrado)/2 for cuadrado in range(1,numero+1)][::-1]] if restas.clear()==None else "xd"



def bin_to_num(cuadrado,binario):
	if binario==1:
		return cuadrado
	else:
		return 0

def getValores_inverso_index(binario):
	# return 0, first
	# >>> getValores_inverso([1, 1, 1, 1, 1, 1])
	# 63.0
	numero=len(binario)
	cuadrados=[(2**cuadrado)/2 for cuadrado in range(1,numero+1)][::-1]
	return sum([ cuadrados[i] if binario[i]==1 else 0 for i in range(len(cuadrados))])
	#return sum([bin_to_num(cuadrados[i],binario[i]) for i in range(len(cuadrados))])



def tabla_version_unalinea(numero):
	return [getValores_unalinea(numero,indice) for indice in range(0,2**numero)]


def tabla_version5(numero):
	ini=time.time()
	resultado=[]
	total=2**numero
	for indice in range(0,total):
		resultado.append(getValores_unalinea(numero,indice))
		#print(indice,"de",total,end="\r")
	print("")
	print(time.time()-ini)
	return resultado


def tabla_version6(numero):
	ini=time.time()
	resultado=[]
	total=2**numero
	for indice in range(0,int(total/2)):
		resultado.append(getValores_unalinea(numero,indice))
		#print(indice,"de",total,end="\r")
	print("")
	print(time.time()-ini)
	return resultado+logical_not(resultado).tolist()


