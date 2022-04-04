res, suma = 1, 0
z = [1, 7, 19, 43, 91, 187, 379, 763, 1531, 3067, 6139]
series = []

n = int(input("Cantidad de terminos a generar: "))
for i in range(1, n+1):
    res = (res*2)+5
    series.append(res)
for a in series:
    suma += a
print(series)
print(f"La suma de los terminos generados es: {suma}")

