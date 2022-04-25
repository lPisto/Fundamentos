val, suma = 1, 0

cantGen = int(input("Ingrese la cantidad de terminos a generar: "))

for i in range(1,cantGen+1):
    print(val)
    suma = suma + val
    val = (val * 2) + 5
        
print(f"La suma de los valores es: {suma}")
    
    
    
