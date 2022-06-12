import random

listaA = []
listaB = []
listaC = []

def burbujeo():
    señalA = 1
    señalB = 1
    while señalA == 1:
        señalA = 0
        for i in range(len(listaA)-1):
            if listaA[i] > listaA[i+1]:
                aux = listaA[i]
                listaA[i] = listaA[i+1]
                listaA[i+1] = aux
                señalA = 1
    while señalB == 1:
        señalB = 0
        for i in range(len(listaB)-1):
            if listaB[i] > listaB[i+1]:
                aux = listaB[i]
                listaB[i] = listaB[i+1]
                listaB[i+1] = aux
                señalB = 1

def ordenamiento():
    posA = 0
    posB = 0
    while posA < len(listaA) and posB < len(listaB):
        if listaA[posA] <= listaB[posB]:
            listaC.append(listaA[posA])
            posA += 1
        elif listaA[posA] >= listaB[posB]:
            listaC.append(listaB[posB])
            posB += 1
        else:
            listaC.append(listaA[posA])
            listaC.append(listaB[posB])
            posA += 1
            posB += 1
    print(listaA, listaB, listaC)

for i in range(random.randint(1,10)):
    listaA.append(random.randint(1,10))
    burbujeo()
for i in range(random.randint(1,10)):
    listaB.append(random.randint(1,10))
    burbujeo()

ordenamiento()