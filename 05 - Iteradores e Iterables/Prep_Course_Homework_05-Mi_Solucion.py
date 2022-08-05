# 1) A partir de una lista vacía, utilizar un ciclo while para cargar allí números negativos del -15 al -1
print("Ejercicio 1")
lista =[]
ind = -15
while ind < 0:
    lista.append(ind)
    ind +=1
print(lista)

# 2) ¿Con un ciclo while sería posible recorrer la lista para imprimir sólo los números pares?
print("Ejercicio 2")
lista =[]
ind = -15
while ind < 0:
    if ind%2 == 0:
        lista.append(ind)
    ind +=1
print(lista)

# 3) Resolver el punto anterior sin utilizar un ciclo while
print("Ejercicio 3")
lista = []
for ind in range(-15,0):
    if ind%2 == 0:
        lista.append(ind)
print(lista)

# 4) Utilizar el iterable para recorrer sólo los primeros 3 elementos
print("Ejercicio 4")
for ind in lista[:3]:
    print(ind)

# 5) Utilizar la función **enumerate** para obtener dentro del iterable, tambien el índice al que corresponde el elemento
print("Ejercicio 5")
for ind, lugar in enumerate(lista):
    print(ind, lugar)

# 6) Dada la siguiente lista de números enteros entre 1 y 20, crear un ciclo donde se completen los valores faltantes: lista = [1,2,5,7,8,10,13,14,15,17,20]
print("Ejercicio 6")
lista = [1,2,5,7,8,10,13,14,15,17,20]
for ind in range(20):
    if lista[ind] != (ind+1):
        lista.insert(ind,(ind+1))
print(lista)

# 7) La sucesión de Fibonacci es un listado de números que sigue la fórmula: <br>
#n<sub>0</sub> = 0<br>
#n<sub>1</sub> = 1<br>
#n<sub>i</sub> = n<sub>i-1</sub> + n<sub>i-2</sub><br>
#Crear una lista con los primeros treinta números de la sucesión.<br>
print("Ejercicio 7")
fibo = [0,1]
for ind in range(2,30):
    fibo.append((fibo[ind - 1] + fibo [ind - 2]))
print(fibo)

# 8) Realizar la suma de todos elementos de la lista del punto anterior
print("Ejercicio 8")
print(sum(fibo))

# 9) La proporción aurea se expresa con una proporción matemática que nace el número irracional Phi= 1,618… que los griegos llamaron número áureo. El cuál se puede aproximar con la sucesión de Fibonacci. Con la lista del ejercicio anterior, imprimir el cociente de los últimos 5 pares de dos números contiguos, donde i es la cantidad total de elementos
print("Ejercicio 9")
ind = 29
while  ind >= 19:
    print(fibo[ind], "/", fibo[ind - 1], "=", fibo[ind]/fibo[ind - 1])
    ind -= 2

# 10) A partir de la variable cadena ya dada, mostrar en qué posiciones aparece la letra "n"<br>
cadena = 'Hola Mundo. Esto es una practica del lenguaje de programación Python'
print("Ejercicio 10")
for ind, letra in enumerate(cadena):
    if letra == "n":
        print(ind)

# 11) Crear un diccionario e imprimir sus claves utilizando un iterador
print("Ejercicio 11")
diccio = {"Numeros": [1,2,3], "Letras": ["a","b","c"],"Numeros dec": [1.1,2.2,3.3], "Letras griegas": ["alfa","beta","gamma"]}
for ind in diccio:
    print(ind)

# 12) Convertir en una lista la variable "cadena" del punto 10 y luego recorrerla con un iterador 
print("Ejercicio 12")
cadena = list(cadena)
letra = iter(cadena)
for ind in range(len(cadena)):
    print(next(letra))

# 13) Crear dos listas y unirlas en una tupla utilizando la función zip
print("Ejercicio 13")
tupla = zip(lista,fibo[0:20])
print(tuple(tupla))

# 14) A partir de la siguiente lista de números, crear una nueva sólo si el número es divisible por 7<br>
lista = [18,21,29,32,35,42,56,60,63,71,84,90,91,100]
print("Ejercicio 14")
lista2 = [ind for ind in lista if (ind % 7 == 0)]
print(lista2)

# 15) A partir de la lista a continuación, contar la cantidad total de elementos que contiene, teniendo en cuenta que un elemento de la lista podría ser otra lista:<br>
lista = [[1,2,3,4],'rojo','verde',[True,False,False],['uno','dos','tres']]
print("Ejercicio 15")
cuenta = 0
for ind in lista:
    if type(ind) == list or type(ind) == tuple:
        cuenta += len(ind)
    else:
        cuenta += 1
print("La lista contiene", cuenta, "elementos")

# 16) Tomar la lista del punto anterior y convertir cada elemento en una lista si no lo es
print("Ejercicio 16")
for ind in range(len(lista)):
    if type(lista[ind]) != list:
        lista[ind] = [lista[ind]]
print(lista)