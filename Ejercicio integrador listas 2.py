import random 

a = 0
lista = []

cantVal = int(input("Ingrese la cantidad de valores a generar: "))

for i in range (1, cantVal+1):
    val = random.randint(20,80)
    for i in range(len(lista)):
        if lista[i] == val:
            a += 1
    if a == 0:
        lista.append(val)
    
    for i in range(len(lista)-1):
        for j in range(i+1, len(lista)):
            if lista[i] > lista[j]:
                aux = lista[i] 
                lista[i] = lista[j]
                lista[j] = aux
                
print(lista)