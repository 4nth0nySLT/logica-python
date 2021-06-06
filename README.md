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
>>> tabla_de_verdad.getValores(5,1)
[0, 0, 0, 0, 0]
>>> tabla_de_verdad.getValores(5,2)
[0, 0, 0, 0, 1]
>>> tabla_de_verdad.getValores(5,21)
[1, 0, 1, 0, 0]
>>> tabla_de_verdad.getValores(5,32)
[1, 1, 1, 1, 1]
```


## Pruebas de velocidad 
### Python
```
x=tabla_de_verdad.tabla(20)
Posibilidades: 1048576

--------------------------100%--------------------------
6.449751615524292
x=tabla_de_verdad.tabla_version2(20)
Posibilidades: 1048576

--------------------------100%--------------------------
6.022998571395874
x=tabla_de_verdad.tabla_version3(20)
Posibilidades: 1048576
3.2254438400268555

--------------------------100%--------------------------
6.0349509716033936
x=tabla_de_verdad.tabla_version4(20)
Posibilidades: 1048576
0.926584005355835

--------------------------100%--------------------------
4.103060483932495
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
