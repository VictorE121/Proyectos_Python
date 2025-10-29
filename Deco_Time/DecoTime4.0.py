# Proyecto: Deco_Time
# Descripción: Decorador para medir el tiempo de ejecución de una función, programa completo con suma y producto de un numero N.
# Idioma: Español
# Versión: 4.0

import time
import sys
sys.set_int_max_str_digits(0)

print(f"PRACTICE 003: DECORADOR PARA MEDIR TIEMPO DE EJECUCIÓN")
print(f"WARINING: Para numeros mayores a 1000, si imprimes el output de productos, este programa puede tardar muchooo tiempo.")
print(f"WARINING: Si tambien imprimes el output de sumas, este programa puede tardar aun mas tiempo.")
Num1 = int(input(f"Ingresa un Numero: "))

def Deco_Time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Tiempo de Ejecucion: {end_time - start_time} Segundos")
        return result
    return wrapper


#1RA OPCION DE LA FUNCION SUMA_NUM SIN IMPRESION DE PASOS INTERMEDIOS

#@Deco_Time
#def Suma_Num_0(Num1):
#    return sum(range(1, Num1 + 1))


#2DA OPCION DE LA FUNCION SUMA_NUM CON IMPRESION DE PASOS INTERMEDIOS

@Deco_Time
def Suma_Num_0(Num1):
    NumTemp = int(0)
    for i in range(Num1):
        #print(f"Sumando: {NumTemp} + 1")
        NumTemp += 1
        #print(f"Resultado: {NumTemp}")
        #time.sleep(1)
    return Num1

#FUNCTION PRODUCTO_NUM
#Desabilita la impresión de pasos intermedios en números grandes para evitar largos tiempos de ejecución y una salida limpia

@Deco_Time
def Producto_Num(Num1):
    Prod_Num = int(1)
    for i in range(1, Num1 + 1):
        #print(f"Multiplicando: {Prod_Num} * {i}")
        Prod_Num *= i
        #print(f"Resultado: {Prod_Num}")
        #time.sleep(1)
    return Prod_Num


Suma_Num_0(Num1)
Producto_Num(Num1)
