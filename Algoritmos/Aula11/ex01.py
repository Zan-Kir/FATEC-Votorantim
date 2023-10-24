lista = []
i = 0

for i in range(0, 10):
    lista.append(int(input('Digite um numero: ')))

tupla = tuple(lista)
print(f'{tupla[::-1]}')
