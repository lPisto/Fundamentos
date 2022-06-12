legajo, apro, desa, cont, sumaNotas, señ  = 0, 0, 0, 0, 0, 0

legajos = []
notas = []
supProm = []

def ordenamiento():
    señal = 1
    while señal == 1:
        señal = 0
        for i in range(len(legajos)-1):
            if legajos[i] > legajos[i+1]:
                aux = legajos[i]
                legajos[i] = legajos[i+1]
                legajos[i+1] = aux 

def busqueda(val):
    señ = 0
    min = 0
    max = len(legajos)-1
    pos = -1
    while min <= max and pos == -1:
        med = (min + max) // 2
        if val == legajos[med]:
            pos = med 
        if val >= legajos[med]:
            min = med + 1
        else:
            max = med - 1
    if pos != -1:
        print("El legajo se encuentra en la posicion: ", pos)
        señ += 1
    else:
        print("El legajo no se encuentra")

    return señ

while legajo != -1:
    legajo = int(input("Ingrese el numero de legajo: "))
    if legajo != -1:
        nota = int(input("Ingrese la nota: "))
        if nota >= 1 and nota <= 10:
            legajos.append(legajo)
            notas.append(nota)
            cont += 1
        else:
            print("Ingrese una nota valida")    

for i in range (len(notas)):
    sumaNotas = sumaNotas + notas[i]
    if notas[i] >= 4:
        apro += 1
    else:
        desa += 1

prom = sumaNotas / cont
for i in range (len(notas)):
    if notas[i] > prom:
        supProm.append(legajos[i])       

print(apro, "alumnos aprobaron")
print(desa, "alumnos desaprobaron")
print("alumnos que superaron el promedio de notas", supProm)

print(legajos)

while señ == 0:
    if señ == 0:
        val = int(input("Ingrese un numero de legajo: "))
    señ = busqueda(val)
    
for i in range (len(legajos)-1):
    if legajos[i] == val:
        print("Su nota final es: ", notas[i])

ordenamiento()

