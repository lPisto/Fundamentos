a = 0
b = 1
pos = 0
noPrimo = 0
primo = 0
suma = 0
defi = 0
for i in range(1, 25+1):
    c = a + b
    a = b
    b = c
    print(c)
    pos += 1
    noPrimo = 0
    if pos >= 5:
        if (pos % 2) == 0:
            for divisores in range(1, c+1):              
                if (c % divisores) == 0:                   
                    if divisores != 1 and divisores != c:
                        noPrimo += 1
    
            if noPrimo == 0:
                primo += 1
    if (pos % 2) == 1:
        for divi in range(1, c+1):
            if (c % divi) == 0:
                if divi != c:
                    suma = suma + divi
        if suma < c:
            defi += 1
print(f"Hay {primo} numeros primos en posiciones pares a partir de la posicion 5")
print(f"Se encontraron {defi} numeros deficientes en posiciones impares")            
            
    
    
