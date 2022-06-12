def calcular(operacion, valor1, valor2):
    if operacion == 1:
        res = valor1 + valor2
    if operacion == 2:
        res = valor1 - valor2
    if operacion == 3:
        res = valor1 * valor2
    if operacion == 4:
        res = valor1 / valor2
    return res

#PP
operacion = -1

while operacion != 0:
    print("Que operacion desea realizar?")
    print("1-Sumar", "3-Multiplicar")
    print("2-Restar", "4-Dividir")
    print("0-Salir")

    operacion = int(input())

    if operacion != 0:
        valor1 = int(input("Ingrese el primer valor: "))
        valor2 = int(input("Ingrese el segundo valor: "))

        resultado = calcular(operacion, valor1, valor2)
        print("El resultado es: ",resultado)

