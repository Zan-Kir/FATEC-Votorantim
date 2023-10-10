numeros = []

for i in range(0, 10):
    numeros.append(int(input(f'Digite o número {i + 1}: ')))


for i in numeros[::-1]:
    print(i, end=' ')
print()
print(numeros)
#numeros.reverse()
#print(f'{numeros}')
