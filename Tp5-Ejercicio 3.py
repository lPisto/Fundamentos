cantidad, precioBase, precioFinal, precioPromedio, ventasTotal, b, c = 0, 0, 0, 0, 0, 0, 0

while cantidad != -1:
    cantidad = int(input("Ingrese la cantidad: "))
    if cantidad == -1:
        break
    precioBase = int(input("Ingrese el precio base: "))
    if cantidad > 0 and cantidad < 12:
        precioFinal = precioBase * cantidad
        precioPromedio = precioFinal / cantidad
        ventasTotal = ventasTotal + 1
    elif cantidad >= 13 and cantidad <= 100:
        precioFinal = (precioBase * cantidad)-(10 * (precioBase * cantidad) / 100)
        precioPromedio = precioFinal / cantidad
        b = b + 1
        ventasTotal = ventasTotal + 1
    elif cantidad > 100:
        precioFinal = (precioBase * cantidad)-(25 * (precioBase * cantidad) / 100)
        precioPromedio = precioFinal / cantidad
        c = c + 1
        ventasTotal = ventasTotal + 1

    print("")
    print(f"El valor total de la venta es: {precioFinal}")
    print(f"El valor promedio de la venta es: {precioPromedio}")
print("")
print(f"Se realizaron un total de {ventasTotal} ventas")
print(f"Se aplico un 10% de descuento en {b} ventas")
print(f"En {b} ventas no se aplicaron descuentos")