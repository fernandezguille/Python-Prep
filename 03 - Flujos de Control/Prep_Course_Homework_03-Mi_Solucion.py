#Homework de la clase 3 - Flujos de control

# 1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla si es mayor o menor a cero
from ast import Continue
from operator import truediv


entero = int(0)
if (entero > 0):
    print(entero, "es mayor a cero")
elif (entero < 0):
    print(entero, "es menor a cero")
else:
    print(entero, "es igual a cero")

# 2) Crear dos variables y un condicional que informe si son del mismo tipo de dato
decimal = 3.5
if (type(entero) == type(decimal)):
    print("Ambas variables son del tipo ",type(entero))
else:
    print("Las variables son diferentes tipos de datos")

# 3) Para los valores enteros del 1 al 20, imprimir por pantalla si es par o impar
for entero in range(1,21):
    if entero%2 == 0:
        print(entero," es par.")
    else:
        print(entero," es impar.")

# 4) En un ciclo for mostrar para los valores entre 0 y 5 el resultado de elevarlo a la potencia igual a 3
for entero in range(6):
    print(entero**3)

# 5) Crear una variable que contenga un número entero y realizar un ciclo for la misma cantidad de ciclos
entero = 4
for n in range(entero):
    print(n)

# 6) Utilizar un ciclo while para realizar el factorial de un número guardado en una variable, sólo si la variable contiene un número entero mayor a 0
entero = 6
n = 1
if type(entero) == int:
    if entero > 0:
        m = entero
        while entero > 1:
            n *= entero
            entero -= 1
        print("El factorial de", m, "es", n)
    else:
        print("El numero debe ser mayor a cero")
else:
    print("La variable de ser un entero")

# 7) Crear un ciclo for dentro de un ciclo while
print("******  Ejercicio 7 ******")
entero = 4
while entero > 0:
    for n in range(entero):
        print(n)
    entero -= 1

# 8) Crear un ciclo while dentro de un ciclo for
print("******  Ejercicio 8 ******")
veces = 4
for n in range(veces):
    entero = veces - n
    while entero > 0:
        print(entero)
        entero -= 1

# 9) Imprimir los números primos existentes entre 0 y 30
print("******  Ejercicio 9: PRIMOS ******")
Ciclos = 0
for m in range(2,31):
    for n in range(2,31):
        Ciclos += 1
        if m == n:
            print(n)
            break
        elif m%n == 0:
            break
print("Cantidad de ciclos:" ,Ciclos)

# 10) ¿Se puede mejorar el proceso del punto 9? Utilizar las sentencias break y/ó continue para tal fin
print("******  Ejercicio 10: Uso del break ******")
Ciclos = 0
for m in range(2,31):
    primo = True
    for n in range(2,m):
        Ciclos += 1
        if m%n == 0:
            primo = False
            break    
    if (primo):
        print(m)
print("Cantidad de ciclos:" ,Ciclos)

# 11) En los puntos 9 y 10, se diseño un código que encuentra números primos y además se lo optimizó. ¿Es posible saber en qué medida se optimizó?
print("******  Ejercicio 11: Optimizacion del break ******")
Ciclossb = 0
for m in range(2,31):
    primo = True
    for n in range(2,m):
        Ciclossb += 1
        if m%n == 0:
            primo = False        
    if (primo):
        print(m)
print("Cantidad de ciclos sin break:" ,Ciclossb)

Ciclos = 0
for m in range(2,31):
    primo = True
    for n in range(2,int(m/2)):
        Ciclos += 1
        if m%n == 0:
            primo = False
            break   
    if (primo):
        print(m)
print("Cantidad de ciclos con break:" ,Ciclos)
print("Se optimizo a un",int(Ciclos*100/Ciclossb),"% de los ciclos aplicando break")

# 12) Si la cantidad de números que se evalúa es mayor a treinta, esa optimización crece?
print("******  Ejercicio 12: Optimizacion en grandes cantidades ******")
Ciclossb = 0
for m in range(2,101):
    primo = True
    for n in range(2,m):
        Ciclossb += 1
        if m%n == 0:
            primo = False      
print("Cantidad de ciclos sin break:" ,Ciclossb)

Ciclos = 0
for m in range(2,101):
    primo = True
    for n in range(2,int(m/2)):
        Ciclos += 1
        if m%n == 0:
            primo = False
            break   
print("Cantidad de ciclos con break:" ,Ciclos)
print("Se optimizo a un",int(Ciclos*100/Ciclossb),"% de los ciclos aplicando break")

# 13) Aplicando continue, armar un ciclo while que solo imprima los valores divisibles por 12, dentro del rango de números de 100 a 300
print("******  Ejercicio 13: While ******")
m = 99
Ciclossb = 0
while m <= 300:
    Ciclossb += 1
    m += 1
    if m%12 != 0:
        continue
    print(m)
print("La cantidad de ciclos fue de",Ciclossb)

m = 100
Ciclos = 0
while m <= 300:
    Ciclos += 1
    if m%12 != 0:
        m += 1
        continue
    print(m)
    m = m + 12
print("La cantidad de ciclos fue de",Ciclos)
print("Se optimizo a un",int(Ciclos*100/Ciclossb),"% de los ciclos aplicando mejora")

# 14) Utilizar la función **input()** que permite hacer ingresos por teclado, para encontrar números primos y dar la opción al usario de buscar el siguiente
print("** EJERCICIO 14: Por favor, ingrese un numero para evaluar si es primo")
m = int(input())
sigue = True
primo = True
primera = True
while sigue == True:
    for n in range(2,m):
        if m%n == 0:
            primo = False
            break   
    if (primo):
        print("El numero ",m, "es primo")
        print("¿Desea buscar el siguiente numero primo? Pulse 1 para confirmar")
        if input() != "1":
            print("Hasta luego!")
            sigue = False
        else:
            primo = True
            m +=1
    elif (primera):
        print("El numero ",m, "NO es primo, encontremos el primo mas cercano.")
    else:
        primo = True
        m +=1
    primera = False

# 15) Crear un ciclo while que encuentre dentro del rango de 100 a 300 el primer número divisible por 3 y además múltiplo de 6
print("** EJERCICIO 15: Multiplos y divisibles")
n = 100
while n <= 300:
    if n % 6 == 0:
        print(n)
        break
    n +=1