valor_compra = float(input("Digite o valor da compra: "))

if (valor_compra <= 1000):
    desconto = valor_compra * 0.10
elif (valor_compra > 1000) and (valor_compra <= 5000):
    desconto = valor_compra * 0.20
else:
    desconto = valor_compra * 0.30

print(f"Para a compra de {valor_compra:.2f} o valor do desconto é de {desconto:.2f}")
print(f"O total a pagar é de {valor_compra - desconto:.2f}")


