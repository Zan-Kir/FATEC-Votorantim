valor= int(input(f"Insira um número: "))
total = 0
if valor > 0:
    for i in range(1, valor + 1):
        E = (2**i)
        total = total + E
    print(f"o valor de E é: {total}.")
else:
    print(f"O valor digitado deve ser positivo.")