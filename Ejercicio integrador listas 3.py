import random

parcial1 = []
parcial2 = []
posFinal = []

def promedio():
    promociona, final, recursa, pos = 0, 0, 0, 0

    for i in range(len(parcial1)):
        promedio = (parcial1[i] + parcial2[i]) / 2
        if promedio >= 7:
            promociona += 1
            porcProm = (promociona * 100) // 30
        elif promedio >= 4 and promedio <= 6:
            posFinal.append(pos) 
        elif promedio < 4:
            recursa += 1
        pos += 1
    
    print("Promociona el", porcProm,"%", "de los alumnos")
    print(posFinal, end="     ")
    print()
    print(recursa, "alumnos recursan la materia")

for i in range(1,30+1):
    nota1 = random.randint(1,10)
    parcial1.append(nota1)
    nota2 = random.randint(1,10)
    parcial2.append(nota2)

promedio()