# 2) Crear un script con el nombre "clase09_ej2.py2" que reciba como un valor de temperatura en grados centígrados, un valor de humedad y por último si llovio (Con True o False). Y que cada vez que sea invocado, cargue en el archivo provisto "clase09_ej2.csv" una marca de tiempo y esa información.

# Para trabajar con tipos de datos relacionados con la medición del tiempo, como ser fechas, horarios o marcas de tiempo se puede utilizar la clase *datetime*

import sys

if len(sys.argv) == 4:
    import datetime
    import os
    archivo = open("clase09_ej2.csv", "a")
    marca_tiempo = datetime.datetime.now()
    marca_tiempo = int(datetime.datetime.timestamp(marca_tiempo))
    archivo.write(f"{marca_tiempo},{sys.argv[1]},{sys.argv[2]},{sys.argv[3]}\n")
else:
    print("Se recibio una cantidad de parametros diferente a 3")
    print("Se debe indicar un numero decimal para los grados, un entero para la humedad, y un booleano para la lluvia")