import random

lista = []

def ordenamiento():
    señal = 1
    while señal == 1:
        señal = 0
        for i in range(len(lista)-1):
            if lista[i] > lista[i+1]:
                aux = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = aux
                señal = 1

#PP
for i in range (10):
    val = random.randint(0,100)

    if val != 0:
        lista.append(val)
print(lista)
ordenamiento()

print(lista)