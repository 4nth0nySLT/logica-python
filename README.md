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

## Pruebas de velocidad 
### Python
```
>>> a=tabla(20)
Posibilidades: 1048576
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1] 99.99990463256836 %
--------------------------100%--------------------------
41.05933380126953
>>> a=tabla_version2(20)
Posibilidades: 1048576
[False, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True] 49.99990463256836 %
--------------------------100%--------------------------
24.78977346420288
>>> a=tabla_version3(20)
Posibilidades: 1048576
0.928030252456665

--------------------------100%--------------------------
6.017228364944458
>>> a=tabla_bruta(20)
Posibilidades: 1048576
1.7344977855682373
>>> a=tabla_bruta(22)
Posibilidades: 4194304
7.5070412158966064
>>> a=tabla_bruta_version2(20)
Posibilidades: 1048576
0.8977727890014648
>>> a=tabla_bruta_version2(22)
Posibilidades: 4194304
3.89097261428833
```
### Go
```
>>> go run tabla_de_verdad.go 20 tabla_bruta
Posibilidades: 1048576
0.2835185
>>> go run tabla_de_verdad.go 22 tabla_bruta
Posibilidades: 4194304
1.0564341
```
