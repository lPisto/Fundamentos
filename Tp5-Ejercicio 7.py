salarioTotal, legajo, may, men, salarioA, salarioB, salarioC, empleados = 0, 0, 0, 0, 0, 0, 0, 0
salarios = []
catA = []
catB = []
catC = []
while legajo != -1:
    legajo = int(input("Ingrese el numero de legajo: "))
    if legajo == -1:
        break
    categoria = input("Ingrese la categoria: ")
    if categoria == "a" or categoria == "b" or categoria == "c":
        salario = int(input("Ingrese el salario: "))
        salarios.append(salario)
        if categoria == "a":
            catA.append(salario)
        if categoria == "b":
            catB.append(salario)
        if categoria == "c":
            catC.append(salario)
            
        if salario > 20000:
            may = may + 1
        if salario < 5000 and categoria == "c":
            men = men + 1
    empleados = empleados + 1

salarioTotal = sum(salarios)
promedio = salarioTotal / empleados
salarioA = sum(catA)
salarioB = sum(catB)
salarioC = sum(catC)
salarios.sort()

print(f"El importe total de salarios es de: {salarioTotal}")
print(f"Cantidad de empleados que ganan mas de 20000$ {may}")
print(f"Cantidad de empleados que ganan menos de 5000$, cuya categoria es c: {men}")
print(f"El sueldo mas bajo es de: {salarios[0]}")
print(f"El importe total de salarios en la categoria a es de: {salarioA}")
print(f"El importe total de salarios en la categoria b es de: {salarioB}")
print(f"El importe total de salarios en la categoria c es de: {salarioC}")
print(f"El promedio de salarios es de: {promedio}")
