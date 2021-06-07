# logica-python
Lógica proposicional en python, tabla de verdad

```
>>> import tabla_de_verdad
>>> x=tabla_de_verdad.tabla(5)
Posibilidades: 32
[1, 1, 1, 1, 1] 96.875 %
--------------------------100%--------------------------
>>> for i in range(len(x)):
...     print(x[i])
...
[0, 0, 0, 0, 0]
[0, 0, 0, 0, 1]
[0, 0, 0, 1, 0]
[0, 0, 0, 1, 1]
[0, 0, 1, 0, 0]
[0, 0, 1, 0, 1]
[0, 0, 1, 1, 0]
[0, 0, 1, 1, 1]
[0, 1, 0, 0, 0]
[0, 1, 0, 0, 1]
[0, 1, 0, 1, 0]
[0, 1, 0, 1, 1]
[0, 1, 1, 0, 0]
[0, 1, 1, 0, 1]
[0, 1, 1, 1, 0]
[0, 1, 1, 1, 1]
[1, 0, 0, 0, 0]
[1, 0, 0, 0, 1]
[1, 0, 0, 1, 0]
[1, 0, 0, 1, 1]
[1, 0, 1, 0, 0]
[1, 0, 1, 0, 1]
[1, 0, 1, 1, 0]
[1, 0, 1, 1, 1]
[1, 1, 0, 0, 0]
[1, 1, 0, 0, 1]
[1, 1, 0, 1, 0]
[1, 1, 0, 1, 1]
[1, 1, 1, 0, 0]
[1, 1, 1, 0, 1]
[1, 1, 1, 1, 0]
[1, 1, 1, 1, 1]
```

```
>>> x=getValores(5,1)
0.0 seg
[0, 0, 0, 0, 0]
>>> x=getValores(5,2)
0.0 seg
[0, 0, 0, 0, 1]
>>> x=getValores(5,21)
0.0 seg
[1, 0, 1, 0, 0]
>>> x=getValores(5,32)
0.0 seg
[1, 1, 1, 1, 1]
```

```
>>> 2**203
12855504354071922204335696738729300820177623950262342682411008
>>> resultado=getValores_unalinea(203,10293291)
>>> print(resultado)
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1]
>>> getValores_inverso_index(resultado)
10293291.0
```

## Pruebas de velocidad 
### Python
#### Tablas utilizando una tabla bruta, todas las respuestas, y luego separando
```
>>> x=tabla_de_verdad.tabla(20)
Posibilidades: 1048576

--------------------------100%--------------------------
6.449751615524292 seg
>>> x=tabla_de_verdad.tabla_version2(20)
Posibilidades: 1048576

--------------------------100%--------------------------
6.022998571395874
>>> x=tabla_de_verdad.tabla_version3(20)
Posibilidades: 1048576
3.2254438400268555 seg creando la tabla bruta

--------------------------100%--------------------------
6.0349509716033936
>>> x=tabla_de_verdad.tabla_version4(20)
Posibilidades: 1048576
0.926584005355835 seg creando la tabla bruta

--------------------------100%--------------------------
4.103060483932495 seg
```
#### Comprobacion de tabla completa y generador de resultados
```
>>> x=tabla_version4 (20)
>>> for i in range(1,len(x)/2+1):
...     print(x[i-1]==getValores(20,i),i)
```
#### Tablas utilizando un generador en cada una
```
>>> x=tabla_version5(20)

13.088716268539429
>>> x=tabla_version6(20)

6.666651964187622
```

### Go, tabla bruta sin separarla
```
>>> go run tabla_de_verdad.go 20 tabla_bruta
Posibilidades: 1048576
0.2835185 seg
>>> go run tabla_de_verdad.go 22 tabla_bruta
Posibilidades: 4194304
1.0564341 seg
```
