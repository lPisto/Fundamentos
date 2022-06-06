valI = 5

lista = [valI]
listaPrimos = []

def primos(val):
    noPrimo = 0
    for divisores in range (1,val+1):
        if (val % divisores) == 0:
            if (divisores != 1) and (divisores != val):
                noPrimo += 1
    if noPrimo == 0:
        listaPrimos.append(val)

cantVal = int(input("Ingrese la cantidad de valores a generar: ")) 

if cantVal < 30:
    for i in range (cantVal+1):
        valF = (valI * 2) - 3
        valI = valF
        
        lista.append(valF)

    print (lista)

    for i in lista:
        primos(i)

    print(listaPrimos)

    bbMin = 0
    bbMax = len(listaPrimos)-1
    pos = -1

    bbVal = int(input("Ingrese un valor a buscar: "))

    if bbVal < listaPrimos[len(listaPrimos)-1]:
        while bbMin <= bbMax and pos == -1:
            bbMed = (bbMin + bbMax) // 2
            if bbVal == listaPrimos[bbMed]:
                pos = bbMed
            if bbVal >= listaPrimos[bbMed]:
                bbMin = bbMed + 1
            else:
                bbMax = bbMed -1
        if pos != -1:
            print(bbVal, "se encuentra en la lista")
        else:    
            print(bbVal, "no se encuentra en la lista")
    else:
        print("Ingrese un valor comprendido en la lista")

