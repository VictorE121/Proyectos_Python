# Proyecto: Deco_Time
# Descripción: Decorador para medir el tiempo de ejecución de una función que suma dos números.
# Versión: 1.0

import time

a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))

def deco_time(funcion):

    def funcion_decorada(a,b):
        inicio = time.time()
        resultado = funcion(a,b)
        final = time.time()
        print(f"Tiempo de ejecución: {final - inicio} segundos")
        return resultado
    return funcion_decorada

@deco_time
def suma(a, b):
    print(f"Calculando la suma...")  
    time.sleep(2)  # Simula una operación que toma tiempo
    Sumatoria = a + b
    print(f"La suma de {a} y {b} es: {Sumatoria}")
    return Sumatoria

suma(a, b)
