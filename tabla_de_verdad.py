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
		print(matriz2[index],(index/total)*100,"%",end='             \r')
	print("")
	print("--------------------------100%--------------------------")
	print(time.time()-ini)
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
	print(time.time()-ini)
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
	print(time.time()-ini)
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
	print(time.time()-ini)
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
	print(time.time()-ini)
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
	print(time.time()-ini)
	return matriz2
