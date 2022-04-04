n, cont = 0, 0

while n != -1:
    producto = 1
    n = int(input("Ingrese el valor: "))
    if n == -1:
        break
    if n > 0:
        for i in range(1, n+1):
            producto *= i
        print(f"El factorial de {n} es: {producto}")
        cont = cont + 1
        
print(f"Se ejecutaron {cont} factoriales")

        


