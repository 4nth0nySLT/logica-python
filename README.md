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
```
