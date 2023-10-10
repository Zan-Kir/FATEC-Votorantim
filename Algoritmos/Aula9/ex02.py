numeros = []

for i in range(0, 10):
    numeros.append(int(input(f'Digite o número {i + 1}: ')))

print(f'O maior valor é {max(numeros)}, está no indice {numeros.index(max(numeros))}')
