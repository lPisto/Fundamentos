cont = 0
i = 0
cant = int(input("Ingrese la cantidad de valores a generar de la serie: "))
while cont != cant:
    if cont == cant:
        break
    i += 1
    if (i % 2) == 1:
        print(i)
        cont += 1
