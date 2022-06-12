import random 

val = 0
lista = []

def ordenamiento():
    for j in range(len(lista)-1):
        for i in range (j+1, len(lista)):
            if lista[j] > lista[i]:
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux

def busqueda(val):
    min = 0
    max = len(lista)-1
    pos = -1

    while min <= max and pos == -1:
        med = (min + max) // 2
        if val == lista[med]:
            pos = med
        if val > lista[med]:
            min = med + 1
        else:
            max = med - 1                   
    if pos != -1:
        print("El valor se encuentra en la posicion: ", pos)
    else:
        print("No se encontro ningun valor en la lista")

for i in range(20):
    lista.append(random.randint(1,100))

ordenamiento()

print(lista)

while val != -1:
    val = int(input("Ingrese un valor a buscar: "))
    if val != -1:
        busqueda(val)
