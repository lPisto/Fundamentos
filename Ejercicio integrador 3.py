lista = [5]
listaPrimos = []

def primos():
    for i in range (len(lista)-1):
        noPrimo = 0
        for divisores in range (1, lista[i]+1):
            if (lista[i] % divisores) == 0:
                if divisores > 1 and divisores != lista[i]:
                    noPrimo += 1
        if noPrimo == 0:
            listaPrimos.append(lista[i])

def busqueda():
    min = 0 
    max = len(lista)-1
    pos = -1
    val = int(input("Ingrese un valor a buscar: "))
    while min <= max and pos == -1:
        med = (min + max) // 2
        if val == lista[med]:
            pos = med
        if val < lista[med]:
            max = med - 1
        else: 
            min = med + 1
    if pos != -1:
        print("El valor se encuentra en la posicion: ", pos)
    else:
        print("El valor no se encuentra")

#PP
cant = int(input("Ingrese la cantidad de valores a generar: "))

for i in range(cant-1):
    serie = (lista[i] * 2) - 3
    lista.append(serie)

primos()
busqueda()