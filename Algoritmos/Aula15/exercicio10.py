import random

quadrado = []
magico = False

for i in range(0, 9):
    quadrado.append(i)

def quadradoMagico():
    global magico
    if quadrado[0] + quadrado[1] + quadrado[2] == quadrado[0] + quadrado[3] + quadrado[6] == quadrado[0] + \
            quadrado[4] + quadrado[8] == quadrado[3] + quadrado[4] + quadrado[5] == quadrado[6] + quadrado[7] + \
            quadrado[8] == quadrado[6] + quadrado[4] + quadrado[2] == quadrado[2] + quadrado[5] + quadrado[8]:
        magico = True
    else:
        magico = False
    return magico

while magico == False:
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(9):
        numeroAleatorio = random.choice(numeros)
        quadrado[i] = numeroAleatorio
        naoRepetir = numeros.index(numeroAleatorio)
        numeros = numeros[:naoRepetir] + numeros[naoRepetir + 1:]
    quadradoMagico()
print(quadrado)
