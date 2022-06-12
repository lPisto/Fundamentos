import random

COD = []
STK = []
PRECIO = []
REPOS = []

def valStock():
    suma = 0
    for i in range(len(COD)-1):
       res = STK[i] * PRECIO[i]
       suma = suma + res
    return suma

def repos():
    for i in range(len(COD)-1):
        if len(REPOS) < 20:
            if STK[i] == 0:
                REPOS.append(COD[i])
    if len(REPOS) < 20:
        for i in range(20-len(COD)):
            REPOS.append(0)

def ordenamiento():
    señal = 1
    while señal == 1:
        señal = 0
        for i in range(len(REPOS)-1):
            if REPOS[i] > REPOS[i+1]:
                aux = REPOS[i]
                REPOS[i] = REPOS[i+1]
                REPOS[i+1] = aux
                señal = 1

def busqueda(val):
    min = 0
    max = len(REPOS)-1
    pos = -1

    while min <= max and pos == -1:
        med = (min + max) // 2
        if REPOS[med] == val:
            pos = med
        if val < REPOS[med]:
            max = med -1 
        else:
            min = med + 1
    if pos != -1:
        print("El valor se encuentra en la posicion: ", pos)
    else:
        print("El valor no se encuentra")

#PP
for i in range (150):
    COD.append(random.randint(1000, 10000))
    STK.append(random.randint(0, 50))
    PRECIO.append(random.randint(450, 3800))

stock = valStock()
repos()
ordenamiento()

print("Valorizacion de stock: ", "$", stock)

val = int(input("Ingrese un valor de reposicion: "))
busqueda(val)