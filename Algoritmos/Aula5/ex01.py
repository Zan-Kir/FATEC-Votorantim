num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))

if num1 < num2:
    print(f"O {num1} é o menor dos dois números.")
elif num2 < num1:
    print(f"O {num2} é o menor dos dois números.")
else:
    print(f"Os números são iguais.")
