sumP1, sumP2, sumP3 = 1, 1, 1


p1 = int(input("Ingrese el monto de dinero invertido de la primer persona: "))
p2 = int(input("Ingrese el monto de dinero invertido de la segunda persona: "))
p3 = int(input("Ingrese el monto de dinero invertido de la tercera persona: "))
    
total = p1 + p2 + p3
    
porP1 = (p1 * 100) / total
porP2 = (p2 * 100) / total
porP3 = (p3 * 100) / total

print(f"La primer persona invirtio un {porP1}%")
print(f"La segunda persona invirtio un {porP2}%")
print(f"La tercera persona invirtio un {porP3}%")
