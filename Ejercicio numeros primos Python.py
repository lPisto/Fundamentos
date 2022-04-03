import random

contador, a, primo, con = 0, 0, 0, 0

while con < 100:
    numero = random.randint(0,36)
    if numero > 13 and numero < 24: 
        a = 0
        for divisor in range(1,numero+1):
            if (numero % divisor) == 0 :
                contador += 1
                if divisor > 1 and divisor != numero:
                    a = a + 1
        if a >= 1:
            # print(numero)
            # print("no es primo")
            b = 0
        if a == 0:
            # print(numero)
            # print("es primo")
            primo = primo + 1 
    con = con + 1
    
print("Salieron",primo,"numeros primos en la segunda docena")
        
