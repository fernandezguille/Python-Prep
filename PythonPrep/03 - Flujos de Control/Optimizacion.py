# 11) En los puntos 9 y 10, se diseño un código que encuentra números primos y además se lo optimizó. ¿Es posible saber en qué medida se optimizó?
print("******  Ejercicio 11: Optimizacion del break ******")
Ciclossb = 0
lista_de_primos = []
for m in range(2,1001):
    primo = True
    for n in range(2,m):
        Ciclossb += 1
        if m%n == 0:
            primo = False        
    if (primo):
        lista_de_primos.append(m)
print("Cantidad de ciclos sin break:" ,Ciclossb)

Cicloscb = 0
for m in range(2,1001):
    primo = True
    for n in range(2,int(m/2)):
        Cicloscb += 1
        if m%n == 0:
            primo = False
            break   
print("Cantidad de ciclos con break:" ,Cicloscb)
print("Se optimizo a un",int(Cicloscb*100/Ciclossb),"% de los ciclos aplicando break")

Ciclos = 0
lista_de_primos = []
for m in range(2,1001):
    primo = True
    for n in lista_de_primos:
        Ciclos += 1
        if m%n == 0:
            primo = False
            break   
    if (primo):
        lista_de_primos.append(m)
print("Cantidad de ciclos optimizada:" ,Ciclos)
print("Se optimizo a un",int(Ciclos*100/Ciclossb),"% de los ciclos optimizando aun mas")
print("Se optimizo a un",int(Ciclos*100/Cicloscb),"% comparando con el break")