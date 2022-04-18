from random import randint

suma, numMay, numMen, men, may, cont, contador, noPrimo, primo, sumaDiv, perfecto = 0, 0, 10, 0, 0, 0, 0, 0, 0, 0, 0, 

for i in range (1, 20+1):   
    num = randint(1, 100)
    cont = cont + 1
    print(num)
    suma = num + suma
    if num > numMay:  
        numMay = num
        may = cont
    if num < numMen:
        numMen = num
        men = cont
    noPrimo = 0
    for divisor in range (1, num+1):
        if (num % divisor) == 0:
            contador = contador + 1
            if divisor != num:
                sumaDiv = divisor + sumaDiv
            if sumaDiv == num:
                perfecto = perfecto + 1
            if divisor > 1 and divisor != num:
                noPrimo = noPrimo + 1
    if noPrimo >= 1:
        b = 0
    if noPrimo == 0:
        primo = primo + 1   
                   
print("")
print(f"La suma de los numeros es: {suma}")
print(f"El numero mayor es: {numMay}, y esta en la posicion: {may}")
print(f"El numero menor es: {numMen}, y esta en la posicion: {men}")
print(f"Hay {primo} numeros primos")
print(f"Hay {perfecto} numeros perfectos")
