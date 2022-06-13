import random 

lista = []

def seleccion():
    for j in range(len(lista)-1):
        for i in range(j+1,len(lista)):
            if lista[j] > lista[i]:
                aux = lista[j]
                lista[j] = lista[i]
                lista[i] = aux

def burbujeo():
    señal = 1
    while señal == 1:
        señal = 0
        for i in range(len(lista)-1):
            if lista[i] > lista[i+1]:
                aux = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = aux
                señal = 1

def raiz():
    for i in range (len(lista)-1):
        resto = 1
        aux = lista[i]
        while aux > 0:
            aux = aux - resto
            resto = resto + 2
        if aux == 0:
            print(lista[i],"tiene raiz cuadrada")

def primos():
    for i in range(len(lista)-1):
        noPrimo = 0
        for divisor in range(1, lista[i]+1):
            if (lista[i] % divisor) == 0:
                if divisor > 1 and divisor != lista[i]:
                    noPrimo += 1
        if noPrimo == 0:
            print(lista[i],"es primo")

def deficientes():
    for i in range(len(lista)-1):
        suma = 0
        for divisor in range(1, lista[i]):
            suma = suma + divisor
        if suma < lista[i]:
            print(lista[i], "es deficiente")

def par():
    for i in range(len(lista)-1):
        if lista[i] % 2 == 0:
            print(lista[i], "es par")
        elif lista[i] % 2 == 1:
            print(lista[i], "es impar")

def busqueda():
    min = 0
    max = len(lista)-1
    pos = -1
    val = int(input("Ingrese un valor a buscar: "))
    while min <= max and pos == -1:
        med = (min + max) // 2
        for i in range(len(lista)-1):
            if val == lista[med]:
                pos = med
            if val > lista[med]:
                min = med + 1
            else:
                max = med - 1
    if pos != -1:
        print("El valor se encuentra en la posicion: ", pos)
    else:
        print("El valor no se encuentra")

rango = int(input("Ingrese la cantidad de valores a generar: "))

for i in range(rango):
    lista.append(random.randint(1,100))

# seleccion()

burbujeo()

print(lista)

raiz()

primos()

deficientes()

par()

busqueda()