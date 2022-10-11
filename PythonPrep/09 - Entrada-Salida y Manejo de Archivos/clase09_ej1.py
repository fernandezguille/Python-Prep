# 1) Crear un script con el nombre "clase09_ej1.py" que reciba 3 parametros a elección, verificando que sean exactamente esa cantidad, y muestre como salida los parámetros recibidos
import sys
if len(sys.argv) == 4:
    print(f"El script {sys.argv[0]} tiene los siguientes parametros:")
    for i in range(1,4):
        print(sys.argv[i])
else:
    print("Se recibio una cantidad de parametros diferente a 3")