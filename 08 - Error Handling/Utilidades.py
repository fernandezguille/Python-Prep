class Utilidades:
    
    def __init__(self, lista_numeros):
        if (type(lista_numeros) == list):
            self.lista_sin_duplicados = []
            self.lista = []
            for elemento in lista_numeros:
                if (type(elemento) != int):
                    raise ValueError("Se ha encontrado un valor del tipo incorrecto. Se esperaba un numero entero")
                else:
                    self.lista.append(elemento)
                    if not(elemento in self.lista_sin_duplicados):
                        self.lista_sin_duplicados.append(elemento)
        else:
            raise TypeError("Se esperaba una lista de numeros")
                    

    def __es_primo(self, numero):
        primo = True
        for n in range(2,(numero//2+1)):
            if numero % n == 0:
                primo = False
                break
        return(primo)

    def es_primo(self):
        lista_primos = []
        for elemento in self.lista:
            if (self.__es_primo(elemento)):
                lista_primos.append(True)
            else:
                lista_primos.append(False)
        return lista_primos

    def calcular_moda(self, lista, orden=True):
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
            nro, repes = self.calcular_moda(self.lista)
            print(f"El valor modal minimo es {nro} y se repite {repes} veces")
        else:
            nro, repes = self.calcular_moda(self.lista, False)
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
        parametros_esperados = ['C','K','F']
        lista_conversion = []
        if str(origen) not in parametros_esperados:
            print('Los parametros esperados son:', parametros_esperados)
            return lista_conversion
        if str(destino) not in parametros_esperados:
            print('Los parametros esperados son:', parametros_esperados)
            return lista_conversion
        for i in self.lista:
            lista_conversion.append(self.__conversor(i, origen, destino))
        return lista_conversion
                
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
        lista = []
        for elemento in self.lista:
            lista.append(self.__factorial(elemento))
        return lista