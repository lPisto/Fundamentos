may, men = 0, 0
for i in range (1, 3+1):
    dia = int(input("Ingrese el dia: "))
    if dia >= 1 and dia <= 30:
        gasto = int(input("Ingrese el gasto total: "))

        if gasto > may:
            may = gasto
            men = may
            diaMay = dia
        if gasto < men:
            men = gasto
            diaMen = dia

print(f"El dia de mayor gasto fue el dia: {diaMay}")
print(f"El dia de menor gasto fue el dia: {diaMen}")

           
    
