import random

lista = []
raices = []
primos = []
deficientes = []
listaAmigos = []

def raiz():
    for i in range(len(lista)-1):
        resto = 1
        aux =  lista[i]
        while aux > 0:
            aux = aux - resto
            resto = resto + 2
        if aux == 0:
            raices.append(lista[i])

def primo():
    for i in range(len(lista)-1):
        noPrimo = 0
        for divisor in range (1, lista[i]+1):
            if (lista[i] % divisor) == 0:
                if divisor > 1 and divisor != lista[i]:
                    noPrimo += 1
        if noPrimo == 0:
            primos.append(lista[i])

def deficiente():
    for i in range(len(lista)-1):
        suma = 0
        for divisores in range(1, lista[i]):
            suma = suma + divisores
        if suma < lista[i]:
            deficientes.append(lista[i])

def amigos():
    for i in range(len(lista)-1):
        suma = 0
        for divisores in range (1,lista[i]):
            suma = suma + divisores
        if suma == lista[i+1]:
            listaAmigos.append(lista[i])

for i in range(random.randint(1,10)):
    lista.append(random.randint(1,100))

print(lista, raices, primos, deficientes, listaAmigos)

raiz()

primo()

deficiente()

amigos()