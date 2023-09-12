nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

if media >= 0 and media < 3:
    resultado = "Reprovado"
elif media >= 3 and media < 7:
    nota_exame = 12 - media
    resultado = f"Exame. Você precisa da nota minima de {nota_exame}"
elif media > 7 and media <= 10:
    resultado = "Aprovado"
else:
    resultado = "Média inválida"

print(f"A média foi {media:5.2f}. {resultado}.")
