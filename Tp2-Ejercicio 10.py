pos, suma = 0, 0
num = int(input("Ingrese el valor a convertir: "))
a = num // 1 % 10
resA = a * pow(2,pos)
b = num // 10 % 10
pos += 1
resB = b * pow(2,pos)
c = num // 100 % 10
pos += 1
resC = c * pow(2,pos)
d = num // 1000 % 10
pos += 1
resD = d * pow(2,pos)
suma = resA + resB + resC + resD
print(suma)
