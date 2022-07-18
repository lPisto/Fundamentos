import random

def burbujeoMejorado(lista):
    señal = 1
    while señal == 1:
        señal = 0
        for i in range(len(lista)-1):
            if lista[i] > lista[i+1]:
                aux = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = aux
                señal = 1


def burbujeo(lista):
    for j in range(len(lista)):
        for i in range(len(lista)-1):
            if lista[i] > lista[i+1]:
                aux = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = aux
                
def seleccion(lista):
    for i in range(len(lista)):
        for j in range(len(lista)-1):
            if lista[i] < lista[j]:
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux

def busquedaBinaria(lista, val):
    pos = -1 
    min = 0
    max = len(lista)-1

    while pos == -1 and min <= max:
        med = (min + max) // 2
        for i in range(len(lista)-1):
            if val == lista[med]:
                pos = med
            elif val > lista[med]:
                min = med + 1
            else:
                max = med - 1

    if pos != -1:
        print("El valor se encuentra en la posicion: ", pos)
    else:
        print("El valor no se encuentra")

def fibo(listaFibo):
    a = 0
    b = 1
    for i in range(15):
        c = a + b
        a = b
        b = c
        listaFibo.append(c)

def primos(listaPrimos, lista):
    for i in range(len(lista)-1):
        noPrimo = 0
        for divisores in range(1, len(lista)+1):
            if (lista[i] % divisores) == 0:
                if divisores > 1 and divisores != lista[i]:
                    noPrimo += 1
        if noPrimo == 0:
            listaPrimos.append(lista[i])

def raiz(lista):
    for i in range(len(lista)-1):
        resto = 1
        aux = lista[i]
        while aux > 0:
            aux = aux - resto
            resto = resto + 2
        if aux == 0:
            print(lista[i], " tiene raiz")

def pares(lista):
    for i in range(len(lista)-1):
        if lista[i] % 2 == 0:
            print(lista[i], "es par")

def deficientes(lista):
    for i in range(len(lista)-1):
        suma = 0
        for divisor in range(1, lista[i]):
            if lista[i] % divisor == 0:
                suma = suma + divisor
        if suma < lista[i]:
            print(lista[i], "es deficiente")

def perfectos(lista):
    for i in range(len(lista)-1):
        suma = 0
        for divisor in range(1, lista[i]):
            if lista[i] % divisor == 0:
                suma = suma + divisor
        if suma == lista[i]:
            print(lista[i], "es perfecto")

def oblongos(listaOblongos, lista):
    # oblongos a partir de numeros de la lista
    for i in range(len(lista)-1):
        oblongo = lista[i] * (lista[i] + 1)
    #oblongos dentro de la lista
    for i in range(len(lista)-1):
        for divisor in range(1, lista[i]):
            if lista[i] % divisor == 0:
                oblongo = divisor * (divisor + 1)
            if oblongo == lista[i]:
                print(lista[i], "es oblongo")
    # sucesion de oblongos
    for i in range(20):
        oblongo = i * (i+1)
        listaOblongos.append(oblongo)

# PP
lista = []
listaFibo = [0, 1]
listaPrimos = []
listaOblongos = []

for i in range(20):
    lista.append(random.randint(0, 100))

seleccion(lista)

#busquedaBinaria(lista, lista[5])

# fibo(listaFibo)

# primos(listaPrimos, lista)


# raiz(lista)

# pares(lista)

# deficientes(lista)

perfectos(lista)

oblongos(listaOblongos, lista)
print(lista)