from ex02 import ePrimo
def qntPrimos(num):
    cont = 0
    for i in range(1, num+1):
        if ePrimo(i):
            cont = cont + 1
    return cont

numero = int(input("Digite um numero: "))

print(f"A quantidade de primos é {qntPrimos(numero)}")