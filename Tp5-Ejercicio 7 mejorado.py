
legajo, sumaSal, mas20, men5, may, salMay, sumaA, sumaB, sumaC, salProm, cantSal = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0


while legajo != -1:
    legajo = int(input("Ingrese el numero de legajo: "))
    if legajo == -1:
        break;
    categoria = input("Ingrese la categoria: ")
    if categoria != "a" and categoria != "b" and categoria != "c":
        print("Ingrese una categoria valida")
    else:
        salario = int(input("Ingrese el salario: "))
        #salarios totales
        sumaSal = salario + sumaSal
        cantSal += 1

        #cantidad de empleados que ganan mas de $20000
        if salario > 20000:
            mas20 += 1

        #cantidad de empleados que ganan menos de $5000, cuya categoría sea “C”
        if categoria == "c":
            if salario < 5000:
                men5 += 1

        #legajo del empleado que más gana
        if salario > salMay:
            may = legajo
            salMay = salario
            men = salMay

        #sueldo más bajo
        if salario < men:
            men = salario

        #importe total de sueldos por cada categoría
        if categoria == "a":
            sumaA = salario + sumaA
        if categoria == "b":
            sumaB = salario + sumaB
        if categoria == "c":
            sumaC = salario + sumaC

        #salario promedio
        salProm = sumaSal / cantSal

print("")
print(f"El importe total de salarios pagados por la empresa es: ${sumaSal}")        
print(f"{mas20} empleados ganan mas de $20000")
print(f"{men5} empleados ganan menos de $5000, y su categoría es la “C”")
print(f"El legajo del empleado que mas gana es: {may}")
print(f"El sueldo mas bajo es: ${men}")
print(f"El importe total de sueldos en la categoria “A” es: ${sumaA}")
print(f"El importe total de sueldos en la categoria “B” es: ${sumaB}")
print(f"El importe total de sueldos en la categoria “C” es: ${sumaC}")
print(f"El salario promedio es: ${salProm}")
    
    
