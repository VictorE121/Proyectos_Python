import time

Num1 = int(input("Enter a number: "))

def Deco_Time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time: {end_time - start_time} seconds")
        return result
    return wrapper

@Deco_Time
def Suma_Num(Num1):
    for i in range(1, Num1 + 1):
        print(f"Adding: {i}")
        #time.sleep(1)
    return Num1

@Deco_Time
def Producto_Num(Num1):
    Prod_Num = 1
    for i in range(1, Num1 + 1):
        print(f"Multiplying by: {i}")
        Prod_Num *= i
        print(f"Multiplying: {Prod_Num}")
        #time.sleep(1)
    return Prod_Num

Suma_Num(Num1)
Producto_Num(Num1)
