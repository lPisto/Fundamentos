num, menor, mayor, igual, sumaMenores, sumaMayores = 0, 0, 0, 0, 0, 0

menores = []
mayores = []

while num != 999:
    num = int(input())
    if num > 0 and num < 100:
        if num < 18:
            menor = menor + 1
            menores.append(num)             
        elif num == 18:
            igual = igual + 1
            mayores.append(num)
        elif num > 18:
            mayor = mayor + 1
            mayores.append(num)

for i in menores:
    sumaMenores += i

for i in mayores:
    sumaMayores += i

if menor > 0:
    promedioMenor = sumaMenores/menor
if mayor > 0 or igual > 0:
    promedioMayor = sumaMayores/(mayor+igual)

print(f"Hay {menor} menores de 18 años")
print(f"Hay {igual} de 18 años")
print(f"Hay {mayor} mayores de 18 años")

print(f"El promedio de edad de los menores de 18 años es: {promedioMenor}")
print(f"El promedio de edad de los mayores de 18 años es: {promedioMayor}")

