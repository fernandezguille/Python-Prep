# Funcion factorizar
# Parametro: Numero positivo
# Retorna: Lista de es_primos y exponentes

import sys

def factorizar(numero):
    #En la primer parte armamos una lista de primos hasta la mitad del numero
    listadeprimos = []
    for i in range(2,(numero//2+1)):
        es_primo = True
        for j in range(2,i):
            if i % j == 0:
                es_primo = False
                break
        if (es_primo):
            listadeprimos.append(i)
    #En la segunda parte buscamos dividir al numero por los primos
    lista_factores = []
    lista_exponentes = []
    i = 2
    while i <= listadeprimos[len(listadeprimos)-1]:
        if numero % i == 0:
            numero = numero / i
            if (i in lista_factores):
                lista_exponentes[lista_factores.index(i)] +=1
            else:
                lista_factores.append(i)
                lista_exponentes.append(1)
        else:
            i += 1
    if len(lista_factores) == 0:
        return [[numero],[1]]
    else:
        return [lista_factores, lista_exponentes]
         
print(factorizar(int(sys.argv[1])))