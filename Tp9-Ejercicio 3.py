import random

juego = 1

top = []
dni = []

def play(secretVal):
    val, cont = 0, 0
    while val != secretVal:
        cont += 1
        val = int(input("Ingrese el valor secreto: "))
        if val == secretVal:
            top.append(cont)
            ordenamiento()
            correct(cont)
        elif val < secretVal:
            print("El valor secreto es Mayor..")
        else:
            print("El valor secreto es Menor..")
        if val == -1:
            val = secretVal

def ordenamiento():
    for j in range(len(top)-1):
        for i in range(j+1, len(top)):
            if top[j] > top[i]:
                aux = top[i]
                top[i] = top[j]
                top[j] = aux

def correct(cont):
    if cont <= top[0]:
        dniNum = int(input("Ingrese su dni: "))
        dni.append(dniNum)

            
while juego != 2:
    secretVal = random.randint(1000, 9999)
    print(secretVal)

    play(secretVal)

    print("Desea seguir jugando?")
    print("1 - Si", "2 - No")

    juego = int(input())

if len(top) >= 5:
    for i in range(4):
        print(i+1,"# ", "Dni - " ,dni[i], top[i], " intentos")
else:
    for i in range(len(top)-1):
        print(i+1,"# ", "Dni - " ,dni[i], top[i], " intentos")
