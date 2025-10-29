# Proyecto: Deco_Time
# Descripción: Decorador para medir el tiempo de ejecución de una función que suma dos números, pequeñas mejoras, incorporando Suma y Producto de dos numeros.
# Versión: 2.0

import time

Num1 = int(input("Ingrese el primer número: "))
Num2 = int(input("Ingrese el segundo número: "))

def suma_num(Num1, Num2):

    for i in range(Num2):
        print(f"Incrementando: {Num1}")
        Num1 += 1
        time.sleep(1)
    return Num1

def producto_num(Num1, Num2):

    Prod_Num = 1

    for i in range(Num2):
        Num1 += 1
        Prod_Num *=Num1
        print(f"Multiplicando: {Prod_Num}")
        print(f"Resolviendo producto: {Prod_Num}")
        time.sleep(1)

#suma_num(Num1, Num2)
producto_num(Num1, Num2)