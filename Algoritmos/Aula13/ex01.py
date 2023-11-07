def eNumPar(num):
    if num % 2 == 0:
        return True
    else:
        return False

x = int(input("Digite um numero inteiro: "))
if eNumPar(x):
    print("O número é par!")
else:
    print("O número é impar!")