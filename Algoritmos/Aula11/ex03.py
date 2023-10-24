lista = []
numero = 100
while len(lista) < 10:
    primo = True
    for i in range(2, numero//2):
        if (numero % i) == 0:
            primo = False
            break
    if primo:
        lista.append(numero)
    numero +=1

tupla = tuple(lista)

print(tupla[::-1])

for i in range(len(tupla)):
    print(tupla[i], end=' ')
