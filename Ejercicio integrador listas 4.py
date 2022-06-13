a = 0
b = 1

fibo = [a,b]

def busqueda():
    min = 0 
    max = len(fibo)-1
    pos = -1
    val = int(input("Ingrese un valor a buscar: "))
    while min <= max and pos == -1:
        med = (min + max) // 2
        for i in range(len(fibo)-1):
            if val == fibo[med]:
                pos = med
            if val > fibo[med]:
                min = med + 1
            else:
                max = med - 1
    if pos != -1:
        print("El valor se encuentra en la posicion: ", pos)
    else:
        print("El valor no se encuentra")

serie = int(input("Ingrese la cantidad de valores a generar: "))

for i in range(serie-2):
    c = a + b
    a = b
    b = c
    fibo.append(c)

print(fibo)

busqueda()