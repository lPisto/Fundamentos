tipo, sexo, animales, perrosHembra, conejosMachos, gatos = 0, 0, 0, 0, 0, 0
while tipo != -1 or sexo != -1:
    print('Tipos de animal: ', end="")
    print(' ')
    print('1 - Perro')
    print('2 - Gato')
    print('3 - Conejo')
    print(' ')
    tipo = int(input('Ingrese el tipo de animal: '))
    if tipo == -1:
        break
    if tipo >= 1 and tipo <= 3:
        print(' ')
        print('Sexo del animal: ', end="")
        print(' ')
        print('1 - Macho')
        print('2 - Hembra')
        print(' ')
        sexo = int(input('Ingrese el sexo del animal: '))
        if sexo >= 1 and sexo <= 2: 
            if tipo == 1 and sexo == 2:
                perrosHembra = perrosHembra + 1
            if tipo == 3 and sexo == 1:
                conejosMachos = conejosMachos + 1
            if tipo == 2:
                gatos = gatos + 1
            animales = animales + 1
        else:
            print('Ingrese un valor correcto')
    else:
        print('Ingrese un valor correcto')

porcentajeGatos = (gatos * 100) / animales

print(f"Se trataron {animales} animales")
print(f"Se trataron {perrosHembra} perros hembra")
print(f"Se trataron {conejosMachos} conejos machos")
print(f"{porcentajeGatos}% de los animales tratados fueron gatos")
