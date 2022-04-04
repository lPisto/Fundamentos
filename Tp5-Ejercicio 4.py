nCliente, totalFactura, dia, precioFinal, precioFinal1, precioFinal2, precioFinal3 = 0, 0, 0, 0, 0, 0, 0

nCliente = int(input("Ingrese el numero de cliente: "))
totalFactura = int(input("Ingrese el total de la factura: "))

dia = 5
if dia > 0 and dia <= 10:
    a = (2 * totalFactura) / 100
    if a > 120:
        precioFinal1 = totalFactura - a
    else:
        precioFinal1 = totalFactura - 120
dia = 15
if dia > 10 and dia <= 20:
    precioFinal2 = totalFactura
dia = 25
if dia > 20:
    b = (10 * totalFactura) / 100
    if b > 150:
        precioFinal3 = totalFactura + b
    else:
        precioFinal3 = totalFactura + 150
    
print("")
print(f"Numero de cliente: {nCliente}")
print("")
print(f"Total de la factura: {totalFactura}")
print(f"Si abona dentro de los primeros 10 dias, el importe es de: {precioFinal1}$")
print(f"Si abona dentro de los siguientes 10 dias, el importe es de: {precioFinal2}$")
print(f"Si abona luego de los 20 dias, el importe es de: {precioFinal3}$")
