class Utilidades:
    
    def __init__(self, lista_numeros):
        self.lista = lista_numeros
        self.lista_sin_duplicados = []
        for elemento in lista_numeros:
            if not(elemento in self.lista_sin_duplicados):
                self.lista_sin_duplicados.append(elemento)

    def __es_primo(self, numero):
        primo = True
        for n in range(2,(numero//2+1)):
            if numero % n == 0:
                primo = False
                break
        return(primo)

    def es_primo(self):
        for elemento in self.lista_sin_duplicados:
            if (self.__es_primo(elemento)):
                print(f"El numero {elemento} SI es primo")
            else:
                print(f"El numero {elemento} NO es primo")

    def __moda(self, lista, orden=True):
        if len(lista) == 0:
            return (None)
        repeticiones = 0
        indice = 0
        if (orden):
            lista.sort(reverse=True)
        else:
            lista.sort()
        for elemento in lista:
            if lista.count(elemento) >= repeticiones:
                repeticiones = lista.count(elemento)
                indice = lista.index(elemento)
        return (lista[indice], repeticiones)

    def moda(self, orden=True):
        if (orden):
            nro, repes = self.__moda(self.lista)
            print(f"El valor modal minimo es {nro} y se repite {repes} veces")
        else:
            nro, repes = self.__moda(self.lista, False)
            print(f"El valor modal maximo es {nro} y se repite {repes} veces")

    def __conversor(self, valor, origen, destino):
        if (type(valor) != float and type(valor) != int):
            return ("El valor debe ser un numero")
        if (origen == "C"):
            if (destino == "C"):
                temperatura = valor
            elif (destino == "F"):
                temperatura = round(valor * 9 / 5 + 32, 2)
            elif (destino == "K"):
                temperatura = valor + 273.15
            else:
                return ("El parametro de destino debe ser C, F o K")
        elif (origen == "F"):
            if (destino == "F"):
                temperatura = valor
            elif (destino == "C"):
                temperatura = round((valor - 32) * 5 / 9,2)
            elif (destino == "K"):
                temperatura = round((valor - 32) * 5 / 9 + 273.15, 2)
            else:
                return ("El parametro de destino debe ser C, F o K")
        elif (origen == "K"):
            if (destino == "K"):
                temperatura = valor
            elif (destino == "F"):
                temperatura = round(valor * 9 / 5 + 305.15, 2)
            elif (destino == "C"):
                temperatura = valor - 273.15
            else:
                return ("El parametro de destino debe ser C, F o K")
        else:
            return ("El parametro de origen debe ser C, F o K")
        return temperatura

    def conversor(self, origen, destino):
        for elemento in self.lista_sin_duplicados:
            print(f"{elemento} grados {origen} son equivalentes a {self.__conversor(elemento, origen, destino)} grados {destino}")
                
    def __factorial(self, numero):
        if (type(numero) != int):
            return ("Se debe ingresar un numero entero positivo")
        elif (numero < 0):
            return ("El número debe ser un entero positivo")
        elif (numero > 1):
            numero = numero * self.__factorial(numero - 1)
        elif (numero == 0):
            numero = 1
        return (numero)
    
    def factorial(self):
        for elemento in self.lista_sin_duplicados:
            print(f"{elemento}! = {self.__factorial(elemento)}")