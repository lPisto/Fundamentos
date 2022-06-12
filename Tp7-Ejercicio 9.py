import random

lista1 = []
lista2 = []

def burbujeoAs():
    señal = 1
    while señal == 1:
        señal = 0
        for i in range(len(lista1)-1):
            if lista1[i] > lista1[i+1]:
                aux = lista1[i+1]
                lista1[i+1] = lista1[i]
                lista1[i] = aux
                señal = 1

def burbujeoDes():
    señal = 1
    while señal == 1:
        señal = 0
        for i in range(len(lista1)-1):
            if lista1[i] < lista1[i+1]:
                aux = lista1[i+1]
                lista1[i+1] = lista1[i]
                lista1[i] = aux
                señal = 1

def seleccionAs():
    for j in range(len(lista2)-1):
        for i in range(j+1,len(lista1)):
            if lista2[j] > lista2[i]:
                aux = lista2[i]
                lista2[i] = lista2[j]
                lista2[j] = aux

def seleccionDes():
    for j in range(len(lista2)-1):
        for i in range(j+1,len(lista1)):
            if lista2[j] < lista2[i]:
                aux = lista2[i]
                lista2[i] = lista2[j]
                lista2[j] = aux

for i in range (20):
    lista1.append(random.randint(0,100))
    lista2.append(random.randint(0,100))

print(lista1)
print(lista2)

burbujeoAs()
print(lista1)
burbujeoDes()
print(lista1)
seleccionAs()
print(lista2)
seleccionDes()
print(lista2)
