from random import randint

dado = [0] * 7

for i in range(6000):
    faceDado = randint(1, 6)
    dado[faceDado] += 1

totalFaces = [0] * 7

for i in range(1, 7):
    totalFaces[i] = (dado[i]/6000)*100
    print(f'{i}, caiu {dado[i]}x e tem o percentual de {totalFaces[i]:.2f}%')