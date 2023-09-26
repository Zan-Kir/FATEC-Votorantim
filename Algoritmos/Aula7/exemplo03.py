soma = 0
qntIdade = int(input(f"Entre com o número de idades a serem somadas: "))
for i in range(1, qntIdade + 1):
    n = int(input(f"Entre com o {i}º. idade: "))
    soma = soma + n
media = soma / qntIdade
print(f"A média das idades é {media:5.2f}")
