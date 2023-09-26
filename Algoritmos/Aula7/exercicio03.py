totalPeso = 0
totalAltura = 0
maiorIMC = 0
menorIMC = 0
for i in range(1,6):
    peso = float(input(f"Digite o valor do Peso da Pessoa {i}: "))
    altura = float(input(f"Digite a altura da Pessoa {i}: "))
    totalPeso = totalPeso + peso
    totalAltura = totalAltura + altura
    imc = peso / (altura * altura)
    if maiorIMC == 0:
        menorIMC = imc
        maiorIMC = imc
    elif imc > maiorIMC:
        maiorIMC = imc
    elif imc < menorIMC:
        menorIMC = imc

pesoMedio = totalPeso / 5
alturaMedia = totalAltura / 5

print(f"A média de peso é {pesoMedio:.2f}. A média de altura {alturaMedia:.2f}. O menor IMC é {menorIMC:.2f}. O maior IMC é {maiorIMC:.2f}")

