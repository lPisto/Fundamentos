legajo, nota, aprobados, desaprobados, aplazados = 0, 0, 0, 0, 0

while legajo != -1:
    legajo = int(input("Legajo del alumno: "))
    if legajo == -1:
        break
    nota = int(input("Nota de examen final: "))
    if nota >= 1 and nota <= 10:
        if nota >= 4:
            aprobados = aprobados + 1
        elif nota < 4 and nota > 1:
            desaprobados = desaprobados + 1
        elif nota == 1:
            aplazados = aplazados + 1
        
        b = aprobados + desaprobados + aplazados
        porcentaje = (aplazados * 100) / b 

print(f"Hay {aprobados} alumnos aprobados")
print(f"Hay {desaprobados} alumnos desaprobados")
print(f"Hay un {porcentaje}% de alumnos aplazados")
    