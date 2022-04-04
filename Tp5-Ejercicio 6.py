sD = 0
a = int(input("Año: "))
m = int(input("Mes: "))
if m <= 12:    
    d = int(input("Dia: "))
else:
    print("Ingrese una fecha correcta")
if d <= 31:    
    n = int(input("Cantidad de dias: "))
else:
    print("Ingrese una fecha correcta")

sD = n + d
if sD > 30:
    d = n - 30 + d
    m = m + 1
elif m > 12:
    a = a + 1

print(f"{a}/{m}/{d}")