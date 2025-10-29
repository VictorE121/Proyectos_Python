import time
import sys
sys.set_int_max_str_digits(0)

print(f"PRACTICE 003: DECORATOR TO MEASURE EXECUTION TIME")
print(f"WARINING: For numbers bigger than 1000, If you are printing the output of products, this program may take a looong time.")
print(f"WARINING: If also you print the output of sums, this program may take an extra looooong time.")
Num1 = int(input(f"Enter a number: "))

def Deco_Time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time: {end_time - start_time} Seconds")
        return result
    return wrapper

#1ST OPTION OF SUMA_NUM FUNCTION WITHOUT PRINTING INTERMEDIATE STEPS

#@Deco_Time
#def Suma_Num_0(Num1):
#    return sum(range(1, Num1 + 1))

#2ND OPTION OF FUNCION SUMA_NUM WITH PRINTING INTERMEDIATE STEPS

@Deco_Time
def Suma_Num_0(Num1):
    NumTemp = int(0)
    for i in range(Num1):
        #print(f"Adding: {NumTemp} + 1")
        NumTemp += 1
        #print(f"Result: {NumTemp}")
        #time.sleep(1)
    return Num1

#FUNCTION PRODUCTO_NUM
#Disabe printing intermediate steps for big numbers to avoid long execution times and clean output

@Deco_Time
def Producto_Num(Num1):
    Prod_Num = int(1)
    for i in range(1, Num1 + 1):
        #print(f"Multiplying: {Prod_Num} * {i}")
        Prod_Num *= i
        #print(f"Result: {Prod_Num}")
        #time.sleep(1)
    return Prod_Num


Suma_Num_0(Num1)
Producto_Num(Num1)
