num = int(input(f"Digite um número inteiro: "))
ePrimo = 0
if num > 1:
    for i in range(1, num + 1):
        if (num % i) == 0:
            ePrimo += 1
    if ePrimo == 2:
        print(f"O número {num} é primo.")
    else:
        print(f"O número {num} não é primo.")
else:
    print(f"Número inválido")