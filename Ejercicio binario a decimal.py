numBin, cont, suma = 0, 0, 0, 0
print("Elija la conversion")
print("")
print("1- Binario - Decimal")
print("2- Decimal - Binario")
conver = int(input())

if conver == 1: 
    while numBin == 0 or numBin == 1:
        numBin = int(input("Ingrese el valor binario: "))
        if numBin != 0 and numBin != 1:
            break
        
        pot = pow(2,cont)
        cont = cont + 1
        res = numBin * pot
        suma = res + suma
    print(suma)
elif conver == 2:
    numDec = int(input("Ingrese el valor decimal: "))

    # for i in range (1, numDec + 1):
    #     div = numDec // 2
    #     res = numDec % 2
    #     div = div // 2
    #     res = div % 2
elif conver != 1 and conver != 2:
    print("Ingrese un valor correcto")
