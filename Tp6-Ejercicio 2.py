import random

def mul(a,b):
    res = 1
    for i in range (b):
        res = res * a
    return res

#PP
desde = int(input("Ingresar el rango Desde: "))
hasta = int(input("Ingresar el rango Hasta: "))

a = random.randint(desde, hasta)
b = random.randint(desde, hasta)

resultado =  mul(a, b)

print(a,b,resultado)

