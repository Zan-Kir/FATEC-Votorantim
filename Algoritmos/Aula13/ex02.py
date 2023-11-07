def ePrimo(num):
    for i in range(2, num):
        if (num % i) == 0:
            return False
    return True

valor = int(input("Digite o valor: "))

if ePrimo(valor):
    print(f"O número {valor} é primo.")
else:
    print(f"O número {valor} não é primo.")
