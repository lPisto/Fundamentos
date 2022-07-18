import random

def burbujeo(lista):
    señal = 1
    while señal == 1:
        señal = 0
        for i in range(len(lista)-1):
            if lista[i] > lista[i+1]:
                aux = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = aux
                señal = 1

def seleccion(lista):
    for j in range(len(lista)):
        for i in range(j+1):
            if lista[i] > lista[j]:
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux

def busqueda(val, lista):
    min = 0
    max = len(lista)-1
    pos = -1
    while min <= max and pos == -1:
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
    for i in range(20):
        c = a + b 
        a = b
        b = c
        listaFibo.append(c)

def primos(lista):
    for i in range(len(lista)-1):
        noPrimo = 0
        for divisor in range(1, lista[i]+1):
            if lista[i] % divisor == 0:
                if divisor > 1 and divisor != lista[i]:
                    noPrimo += 1
        if noPrimo == 0:
            print(lista[i], "es primo")

def raiz(lista):
    for i in range(len(lista)):
        aux = lista[i]
        resto = 1
        while aux > 0:
            aux = aux - resto
            resto = resto + 2
        if aux == 0:
            print(lista[i], "tiene raiz")

def deficientes(lista):
    for i in range(len(lista)):
        suma = 0
        for divisor in range(1, lista[i]):
            if lista[i] % divisor == 0:
                suma = suma + divisor
        if suma < lista[i]:
            print(lista[i], "es deficiente")

def perfectos(lista):
    for i in range(len(lista)):
        suma = 0
        for divisor in range(1, lista[i]):
            if lista[i] % divisor == 0:
                suma = suma + divisor
        if suma == lista[i]:
            print(lista[i], "es perfecto")

def pares(lista):
    for i in range(len(lista)):
        if lista[i] % 2 == 0:
            print(lista[i], "es par")

def oblongos(lista):
    for i in range(len(lista)-1):
        for j in range(1, lista[i]):
            if j*(j+1) == lista[i]:
                print(lista[i], "es oblongo")

def amigos(lista):
    for i in range(len(lista)):
        for divisor in range(1,lista[i]):
            if lista[i] % divisor == 0:
                suma = suma + divisor
        if suma == lista[i+1]:
            for j in range(i+1):
                if lista[i] % j == 0:
                    suma2 = suma2 + j
            if suma2 == lista[i]:
                print(lista[i], lista[j], "son amigos")

lista = []
listaFibo = [0, 1]

for i in range(20):
    lista.append(random.randint(1,100))

# burbujeo(lista)

seleccion(lista)
print(lista)

# val = int(input("Ingrese un valor a buscar: "))

# busqueda(val, lista)

# fibo(listaFibo)
# print(listaFibo)

# primos(lista)

raiz(lista)