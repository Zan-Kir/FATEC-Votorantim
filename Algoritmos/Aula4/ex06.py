salario = float(input("Digite seu salário atual: R$ "))
aumento = float(input("Digite o valor percentual de aumento: "))
novo_sal = salario + (salario * (aumento / 100))
print(f"Seu novo salário é de R$ {novo_sal:.2f}.")
